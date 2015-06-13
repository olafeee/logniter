#!/usr/bin/env python3
import pymysql
from accesslogschema import engine, Dailypageviews, Request, DailypageviewsPerCountry
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.sql.expression import func


class cacheCruncher(object):

	def __init__(self):
		Session = sessionmaker(bind=engine)
		self.sess = Session()		

	def processDailypageviews(self):

		dailypageviews = self.sess.query(Request.datetime, func.count(Request.datetime)).filter_by(isPageview=True).order_by(Request.datetime).group_by(func.day(Request.datetime))
		
		for dailypageviewcount in dailypageviews:

			startdate = dailypageviewcount[0].replace(hour=0, minute=0, second=0, microsecond=0)
			enddate = dailypageviewcount[0].replace(hour=23, minute=59, second=59, microsecond=999)
			pageviews = dailypageviewcount[1]
			
			dailypageview = Dailypageviews(startdate=startdate,
				enddate=enddate,
				pageviews=pageviews)

			self.sess.add(dailypageview)

		self.sess.commit()

	def processDailypageviewsPerCountry(self):
		dailypageviewspercountry = self.sess.query(Request.datetime, Request.countrycode, func.count(Request.datetime)).filter_by(isPageview=True).order_by(Request.datetime).group_by(func.day(Request.datetime), Request.countrycode)
		
		for dailypageviewsforcountry in dailypageviewspercountry:
			
			startdate = dailypageviewsforcountry[0].replace(hour=0, minute=0, second=0, microsecond=0)
			enddate = dailypageviewsforcountry[0].replace(hour=23, minute=59, second=59, microsecond=999)
			countrycode = dailypageviewsforcountry[1]
			pageviews = dailypageviewsforcountry[2]
			
			dailypageviewspercountry_orm = DailypageviewsPerCountry(startdate=startdate,
			enddate=enddate,
			countrycode=countrycode,
			pageviews=pageviews)
			
			self.sess.add(dailypageviewspercountry_orm)
		
		self.sess.commit()

if __name__ == "__main__":
	cc = cacheCruncher()
	cc.processDailypageviews()
	cc.processDailypageviewsPerCountry()
