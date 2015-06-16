#!/usr/bin/env python3
import pymysql
from accesslogschema import engine, Dailypageviews, Monthlypageviews, Request, DailypageviewsPerCountry, MonthlypageviewsPerCountry
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.sql.expression import func
from calendar import monthrange


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

	def processMonthlypageviews(self):
		
		monthlypageviews = self.sess.query(Request.datetime, func.count(Request.datetime)).filter_by(isPageview=True).order_by(Request.datetime).group_by(func.month(Request.datetime))

		for monthlypageviewcount in monthlypageviews:

			startdate = monthlypageviewcount[0].replace(day=1, hour=0, minute=0, second=0, microsecond=0)
			enddateday = monthrange(monthlypageviewcount[0].year, monthlypageviewcount[0].month)[1]
			enddate = monthlypageviewcount[0].replace(day=enddateday, hour=23, minute=59, second=59, microsecond=999)
			pageviews = monthlypageviewcount[1]
			
			monthlypageview = Monthlypageviews(startdate=startdate,
				enddate=enddate,
				pageviews=pageviews)

			self.sess.add(monthlypageview)

		self.sess.commit()

	def processMonthlypageviewsPerCountry(self):
		monthlypageviewspercountry = self.sess.query(Request.datetime, Request.countrycode, func.count(Request.datetime)).filter_by(isPageview=True).order_by(Request.datetime).group_by(func.month(Request.datetime), Request.countrycode)

		for monthlypageviewsforcountry in monthlypageviewspercountry:
			startdate = monthlypageviewsforcountry[0].replace(day=1, hour=0, minute=0, second=0, microsecond=0)
			enddateday = monthrange(monthlypageviewsforcountry[0].year, monthlypageviewsforcountry[0].month)[1]
			enddate = monthlypageviewsforcountry[0].replace(day=enddateday, hour=23, minute=59, second=59, microsecond=999)

			countrycode = monthlypageviewsforcountry[1]
			pageviews = monthlypageviewsforcountry[2]

			monthlypageviewspercountry_orm = MonthlypageviewsPerCountry(startdate=startdate,
				enddate=enddate,
				countrycode=countrycode,
				pageviews=pageviews)

			self.sess.add(monthlypageviewspercountry_orm)

		self.sess.commit()

if __name__ == '__main__':
	cc = cacheCruncher()
	cc.processDailypageviews()
	cc.processDailypageviewsPerCountry()
	cc.processMonthlypageviews()
	cc.processMonthlypageviewsPerCountry()