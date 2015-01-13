#!/usr/bin/env python3
# apache accesslog converter
# version 0.1
# devoleped in python v3.4                 
# made by Olaf Elzinga & Bas Alphenaar  
import os, sys, collections, time
import pygeoip
import httpagentparser
import pymysql
import string, random
import ipaddress
#import re
from time import gmtime, strftime
from datetime import datetime

log = open('/Applications/MAMP/logs/apache_access.log','r')
connection = pymysql.connect(host='localhost', port=8889, user='root', passwd='root', db='accesslog')
cursor = connection.cursor()

class logHandler(object):
	pVisit={} # page visits
	hPage={} # hits per hour inc. bot boolean
	uniqueVisi={} #unique vistors + os & browser + country
	countryDict={}

	# processAccesLog
	def processAccesLog(self):

		for line in log:
			# 0:host || 1:l || 2:user || 3:time || 4:request || 5:status || 6:bytes || 7:referer || 8:user-agent|| 
			array = (line.split('||'))
			
			#Host
			host = array[0]

			#Datetime

			#Request
			request = array[4]

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
				countryCode = country[1]
			except ValueError:	
				countryName = ''
				countryCode = ''


			##$$-----BOT-----$$##
			if 'bot' in httpagentDict.keys():
				bot  = httpagentDict['bot']
			else:
				bot = False

			##$$-----Time-----$$##
			x = time.strptime(array[3], "[%d/%b/%Y:%H:%M:%S %z]")
			
			##$$-----Page-----$$##
			hph = time.strftime('%Y-%m-%d %H:00:00 %z', x)
			hph+= ","+str(bot)
			self.fillDict(self.hPage, hph)  #hits per hour

			##$$-----Unique-----$$##
			# if not bot:
			# 	separation = ','
			# 	# 0:ip , 1:datetime , 2:bot , 3:os , 4:platform_name , 5:platform_version,
			# 	# 6:browser_nane , 7:browser_version , 8:country || 9: hits_day (but is not in query string) 
			# 	query = array[0]+separation #ip
			# 	query += time.strftime('%Y-%m-%d 00:00:00%z', x)+separation
			# 	query += str(bot)+separation
			# 	try:
			# 		query+= str(httpagentDict['os']['name'])+separation
			# 	except:
			# 		query+="no OS"+separation
				
			# 	query+= str(httpagentDict['platform']['name'])+separation
			# 	query+= str(httpagentDict['platform']['version'])+separation
			# 	try:
			# 		query+= str(httpagentDict['browser']['name'])+separation
			# 		query+= str(httpagentDict['browser']['version'])+separation
			# 	except:
			# 		query+="No Browser"+separation+"1.0"+separation
			# 	country = str(self.getCountry(array[0]))
			# 	query+= country

			# 	self.fillDict(self.countryDict, country)
			# 	self.fillDict(self.uniqueVisi, query)
			
			spaceLength = 80-len(array[4])
			spaceLength2 = 60-len(array[7])
			line = array[4],''.ljust(spaceLength),":", array[7],''.ljust(spaceLength2),':',array[3]

		
			#print(strftime("[%d/%b/%Y:%H:%M:%S %z]", gmtime()))
			#self.printList(self.countryDict)
			#self.printList(self.uniqueVisi)

			#Construct the SQL query
			sql = ("INSERT INTO request (host, datetime, request, statuscode, bot, os, platformname, platformversion, browsername, browserversion, countryname, countrycode, isPageview) VALUES "
				"('{host}', "
				"NOW(), "
				"'{request}', "
				"'{statuscode}', "
				"{bot}, "
				"'{os}', "
				"'{platformname}', "
				"'{platformversion}', "
				"'{browsername}', "
				"'{browserversion}', "
				"'{countryname}', "
				"'{countrycode}', "
				"'{isPageview}');"
			)

			formattedSql = sql.format(host=host,
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
				isPageview='1')

			#print(formattedSql)
			cursor.execute(formattedSql)
		
		connection.commit()
		connection.close()

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


	# fillDict
	# @param x name of the dictiornary
	# @param y name of the key
	def fillDict(self, x, y):
		if y not in x:
			x[y] = 1
		else:
			x[y] += 1

	# printList is a test function and will not be included in final version
	def printList(self, item):
		for key, value in item.items():
			spaceLength = 40-len(key)
			line = key,''.ljust(spaceLength),":", value

			print(key,''.ljust(spaceLength),":", value)    
			#filex.write(str(line)+"\n")

if __name__ == "__main__":
	pal = logHandler()
	pal.processAccesLog()