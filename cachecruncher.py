#!/usr/bin/env python3
import pymysql
from accesslogschema import engine, Dailypageview, Request
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.sql.expression import func


class cacheCruncher(object):

	def processDailypageviews(self):

		Session = sessionmaker(bind=engine)
		sess = Session()

		dailypageviews = sess.query(Request.datetime, func.count(Request.datetime)).filter_by(isPageview=True).order_by(Request.datetime).group_by(func.day(Request.datetime))
		
		for dailypageviewcount in dailypageviews:

			daystartdate = dailypageviewcount[0].replace(hour=0, minute=0, second=0, microsecond=0)
			dayenddate = dailypageviewcount[0].replace(hour=23, minute=59, second=59, microsecond=999)

			dailypageview = Dailypageview(daystartdate=daystartdate,
				dayenddate=dayenddate,
				pageviews=dailypageviewcount[1])

			sess.add(dailypageview)

		sess.commit()

if __name__ == "__main__":
	cc = cacheCruncher()
	cc.processDailypageviews()
