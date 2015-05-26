#!/usr/bin/env python3
import pymysql
from accesslogschema import engine, Dailypageviews, Request
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

			dailypageview = Dailypageviews(startdate=startdate,
				enddate=enddate,
				pageviews=dailypageviewcount[1])

			self.sess.add(dailypageview)

		self.sess.commit()

#	def processDailypageviewsPerCountry(self):

if __name__ == "__main__":
	cc = cacheCruncher()
	cc.processDailypageviews()
