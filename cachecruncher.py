#!/usr/bin/python3
import pymysql
from accesslogschema import engine, Dailypageviews, Monthlypageviews, Weeklypageviews, WeeklypageviewsPerCountry, Request, DailypageviewsPerCountry, MonthlypageviewsPerCountry, Yearlypageviews, DBTools
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.sql.expression import func
from calendar import monthrange
from datetime import timedelta


class cacheCruncher(object):

	def __init__(self):
		Session = sessionmaker(bind=engine)
		self.sess = Session()
		self.dbtools = DBTools()	

	def processDailypageviews(self):

		dailypageviews = self.sess.query(Request.datetime, func.count(Request.datetime)).filter_by(isPageview=True).order_by(Request.datetime).group_by(func.day(Request.datetime))
		
		for dailypageviewcount in dailypageviews:

			startdate = dailypageviewcount[0].replace(hour=0, minute=0, second=0, microsecond=0)
			enddate = dailypageviewcount[0].replace(hour=23, minute=59, second=59, microsecond=999)
			pageviews = dailypageviewcount[1]
			
			self.dbtools.get_or_create(self.sess, Dailypageviews,
				startdate=startdate,
				enddate=enddate,
				pageviews=pageviews)

		self.sess.commit()

	def processDailypageviewsPerCountry(self):
		dailypageviewspercountry = self.sess.query(Request.datetime, Request.countrycode, func.count(Request.datetime)).filter_by(isPageview=True).order_by(Request.datetime).group_by(func.day(Request.datetime), Request.countrycode)

		for dailypageviewsforcountry in dailypageviewspercountry:
			
			startdate = dailypageviewsforcountry[0].replace(hour=0, minute=0, second=0, microsecond=0)
			enddate = dailypageviewsforcountry[0].replace(hour=23, minute=59, second=59, microsecond=999)
			countrycode = dailypageviewsforcountry[1]
			pageviews = dailypageviewsforcountry[2]

			self.dbtools.get_or_create(self.sess, DailypageviewsPerCountry,
				startdate=startdate,
				enddate=enddate,
				countrycode=countrycode,
				pageviews=pageviews)
		
		self.sess.commit()

	def processMonthlypageviews(self):
		
		monthlypageviews = self.sess.query(Request.datetime, func.count(Request.datetime)).filter_by(isPageview=True).order_by(Request.datetime).group_by(func.month(Request.datetime))

		for monthlypageviewcount in monthlypageviews:

			startdate = monthlypageviewcount[0].replace(day=1, hour=0, minute=0, second=0, microsecond=0)
			enddateday = monthrange(monthlypageviewcount[0].year, monthlypageviewcount[0].month)[1]
			enddate = monthlypageviewcount[0].replace(day=enddateday, hour=23, minute=59, second=59, microsecond=999)
			pageviews = monthlypageviewcount[1]

			self.dbtools.get_or_create(self.sess, Monthlypageviews,
				startdate=startdate,
				enddate=enddate,
				pageviews=pageviews)

		self.sess.commit()

	def processMonthlypageviewsPerCountry(self):
		monthlypageviewspercountry = self.sess.query(Request.datetime, Request.countrycode, func.count(Request.datetime)).filter_by(isPageview=True).order_by(Request.datetime).group_by(func.month(Request.datetime), Request.countrycode)

		for monthlypageviewsforcountry in monthlypageviewspercountry:
			startdate = monthlypageviewsforcountry[0].replace(day=1, hour=0, minute=0, second=0, microsecond=0)
			enddateday = monthrange(monthlypageviewsforcountry[0].year, monthlypageviewsforcountry[0].month)[1]
			enddate = monthlypageviewsforcountry[0].replace(day=enddateday, hour=23, minute=59, second=59, microsecond=999)

			countrycode = monthlypageviewsforcountry[1]
			pageviews = monthlypageviewsforcountry[2]

			self.dbtools.get_or_create(self.sess, MonthlypageviewsPerCountry,
				startdate=startdate,
				enddate=enddate,
				countrycode=countrycode,
				pageviews=pageviews)

		self.sess.commit()

	def processWeeklypageviews(self):
		weeklypageviews = self.sess.query(Request.datetime, func.count(Request.datetime)).filter_by(isPageview=True).order_by(Request.datetime).group_by(func.week(Request.datetime))

		for weeklypageviewscount in weeklypageviews:

			fetchedDate = weeklypageviewscount[0]

			startdate = (fetchedDate - timedelta(days = fetchedDate.weekday())).replace(hour=0, minute=0, second=0, microsecond=0)
			enddate = (startdate + timedelta(days = 6)).replace(hour=23, minute=59, second=59, microsecond=999)
			pageviews = weeklypageviewscount[1]

			self.dbtools.get_or_create(self.sess, Weeklypageviews,
				startdate=startdate,
				enddate=enddate,
				pageviews=pageviews)

		self.sess.commit()

	def processWeeklypageviewsPerCountry(self):
		weeklypageviewspercountry = self.sess.query(Request.datetime, Request.countrycode, func.count(Request.datetime)).filter_by(isPageview=True).order_by(Request.datetime).group_by(func.week(Request.datetime), Request.countrycode)

		for weeklypageviewsforcountry in weeklypageviewspercountry:

			fetchedDate = weeklypageviewsforcountry[0]
			
			startdate = (fetchedDate - timedelta(days = fetchedDate.weekday())).replace(hour=0, minute=0, second=0, microsecond=0)
			enddate = (startdate + timedelta(days = 6)).replace(hour=23, minute=59, second=59, microsecond=999)
			countrycode = weeklypageviewsforcountry[1]
			pageviews = weeklypageviewsforcountry[2]

			self.dbtools.get_or_create(self.sess, WeeklypageviewsPerCountry,
				startdate=startdate,
				enddate=enddate,
				countrycode=countrycode,
				pageviews=pageviews)

		self.sess.commit()

	def processYearlypageviews(self):
		yearlypageviews = self.sess.query(Request.datetime, func.count(Request.datetime)).filter_by(isPageview=True).order_by(Request.datetime).group_by(func.year(Request.datetime))

		for yearlypageviewscount in yearlypageviews:

			fetchedDate = yearlypageviewscount[0]

			startdate = fetchedDate.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
			enddate = fetchedDate.replace(month=12, day=31, hour=23, minute=59, second=59, microsecond=999)
			pageviews = yearlypageviewscount[1]

			self.dbtools.get_or_create(self.sess, Yearlypageviews,
				startdate=startdate,
				enddate=enddate,
				pageviews=pageviews)

		self.sess.commit()

if __name__ == '__main__':
	cc = cacheCruncher()
	cc.processDailypageviews()
	cc.processDailypageviewsPerCountry()
	cc.processMonthlypageviews()
	cc.processMonthlypageviewsPerCountry()
	cc.processWeeklypageviews()
	cc.processWeeklypageviewsPerCountry()
	cc.processYearlypageviews()