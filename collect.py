#!/usr/bin/env python3
# apache accesslog converter
# version 0.1
# developed in python v3.4          
# made by Olaf Elzinga & Bas Alphenaar
import os, sys, collections, time
import pygeoip
import httpagentparser
import pymysql
import string, random
import ipaddress
import configparser
from accesslogschema import engine, Request, DBTools
from sqlalchemy.orm.session import sessionmaker
from time import gmtime, strftime
from datetime import datetime



debugcountrycodelist = ['NL', 'UK', 'US', 'DE', 'AU', 'FR', 'RU', 'CA', 'SP', 'JP', 'CH', 'IT']

requestblacklist = [".png", ".jpeg", ".jpg", ".js", ".xml"]
contenttypewhitelist = ["text/html"]

class logHandler(object):
    def __init__(self, settings = None):

        self.dbtools = DBTools()

        # When running standalone
        if settings is None:
            config = configparser.ConfigParser()
            config.read('logniter.config')
            self.log = open(config['olafelzinga.com']['Path'],'r')
        # When created as an object from another module
        else:
            self.settings = settings
            self.log = open(settings.config['olafelzinga.com']['Path'],'r')

    # processAccesLog
    def processAccesLog(self):

        Session = sessionmaker(bind=engine)
        sess = Session()

        for line in self.log:
            # 0:host || 1:l || 2:user || 3:time || 4:request || 5:status || 6:bytes || 7:referer || 8:user-agent|| 9:contenttype
            array = (line.split('||'))
            
            #Host
            host = array[0]

            #Datetime
            parsedTime = time.strptime(array[3], "[%d/%b/%Y:%H:%M:%S %z]")
            datetime = time.strftime('%Y-%m-%d %H:%M:%S', parsedTime)

            #Request
            request = array[4][1:-1]

            #Statuscode
            statuscode = array[5]

            #Httpagent stuff
            httpagentDict = httpagentparser.detect(array[8])

            #OS
            try:
                os = httpagentDict['flavor']['name']
            except:
                os = ''
            

            #Platformname
            try:
                platformname = httpagentDict['platform']['name']
            except:
                platformname = ''

            #Platformversion

            try:
                platformversion = httpagentDict['platform']['version']
            except:
                platformversion = ''

            #Browsername
            try:
                browsername = httpagentDict['browser']['name']
            except:
                browsername = ''

            #Browserversion
            try:
                browserversion = httpagentDict['browser']['version']
            except:
                browserversion = ''

            #country
            try:
                country = self.getCountry(host)
                countryName = country[0]
#               countryCode = country[1]
                #Choose a random country code for debugging purposes
                countryCode = random.choice(debugcountrycodelist)
                
            except ValueError:  
                countryName = ''
                countryCode = ''

            #contenttype
            contenttype = array[9][1:-2]

            #bot
            if 'bot' in httpagentDict.keys():
                bot  = httpagentDict['bot']
            else:
                bot = False 

            if self.isPageview(bot, statuscode, contenttype, request):
                pageview = True
            else:
                pageview = False

            self.dbtools.get_or_create(
                )

            request = Request(host=host,
                datetime=datetime,
                request=request, 
                statuscode=statuscode, 
                bot=bot, 
                os=os, 
                platformname=platformname, 
                platformversion=platformversion, 
                browsername=browsername, 
                browserversion=browserversion, 
                countryname=countryName, 
                countrycode=countryCode,
                contenttype=contenttype,
                isPageview=pageview
                )

            sess.add(request)
        
        sess.commit()

    def isPageview(self, bot, statuscode, contenttype, request):
        if not bot and statuscode == "200":
            # Continue the evaluation if content-type is pageview suspect
            if any(contenttype in s for s in contenttypewhitelist):
                strippedRequest = request[4:-9]
                # Mark as non-pageview when the request matches the blacklist
                if any(s in strippedRequest for s in requestblacklist):
                    return False
                else:
                    return True
            else:
                return False

    # getCountry will convert ip to coutryname
    # @param ip 
    def getCountry(self, ip):
        ipaddressObj = ipaddress.ip_address(ip)
        try:
            if isinstance(ipaddressObj, ipaddress.IPv4Address):
                gi = pygeoip.GeoIP('GeoIP.dat')
            elif isinstance(ipaddressObj, ipaddress.IPv6Address):
                gi = pygeoip.GeoIP('GeoIPv6.dat')
            return gi.country_name_by_addr(ip), gi.country_code_by_addr(ip)
        except ValueError:
            raise ValueError('Not a valid IP')

'''
if __name__ == '__main__':
    print('hahah main is loaded')
    lh = logHandler()
    lh.processAccesLog()'''