#!/usr/bin/env python3
# apache accesslog converter
# version 0.1
# devoleped in python v3.4                 
# made by Olaf Elzinga & Bas Alphenaar  
import os, sys, collections, time
import pygeoip
import httpagentparser
#import re
from time import gmtime, strftime
from datetime import datetime

log = open('olafelzinga.com-access_log','r')

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
			#self.getCountry(array[0])
			
			# os || platform || browser
			useragent = httpagentparser.detect(array[8])
			#print(useragent)
			#if not useragent['bot']:
			#print(useragent['bot'])

			##$$-----BOT-----$$##
			if 'bot' in useragent.keys():
				bot  = useragent['bot']
				#print(bot)
			else:
				bot = False

			##$$-----Time-----$$##
			x = time.strptime(array[3], "[%d/%b/%Y:%H:%M:%S %z]")
			
			##$$-----Page-----$$##
			hph = time.strftime('%Y-%m-%d %H:00:00 %z', x)
			hph+= ","+str(bot)
			self.fillDict(self.hPage, hph)  #hits per hour

			##$$-----Unique-----$$##
			if not bot:
				separation = ','
				# 0:ip , 1:datetime , 2:bot , 3:os , 4:platform_name , 5:platform_version,
				# 6:browser_nane , 7:browser_version , 8:country || 9: hits_day (but is not in query string) 
				query = array[0]+separation #ip
				query += time.strftime('%Y-%m-%d 00:00:00%z', x)+separation
				query += str(bot)+separation
				try:
					query+= str(useragent['os']['name'])+separation
				except:
					query+="no OS"+separation
				
				query+= str(useragent['platform']['name'])+separation
				query+= str(useragent['platform']['version'])+separation
				try:
					query+= str(useragent['browser']['name'])+separation
					query+= str(useragent['browser']['version'])+separation
				except:
					query+="No Browser"+separation+"1.0"+separation
				country = str(self.getCountry(array[0]))
				query+= country

				self.fillDict(self.countryDict, country)
				self.fillDict(self.uniqueVisi, query)
			
			spaceLength = 80-len(array[4])
			spaceLength2 = 60-len(array[7])
			line = array[4],''.ljust(spaceLength),":", array[7],''.ljust(spaceLength2),':',array[3]

		
		#print(strftime("[%d/%b/%Y:%H:%M:%S %z]", gmtime()))
		self.printList(self.countryDict)
		#self.printList(self.uniqueVisi)

	def send():
		for key, value in self.uniqueVisi:


	# getCountry will convert ip to coutryname
	# @param ip 
	def getCountry(self, ip):
		gi = pygeoip.GeoIP('GeoIP 2.dat')
		return gi.country_name_by_addr(ip)+","+gi.country_code_by_addr(ip)


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

class sendDict(object):
	
	def __init__(self):
		
		


if __name__ == "__main__":
	pal = logHandler()
	pal.processAccesLog()