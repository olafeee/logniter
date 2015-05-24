from sqlalchemy import create_engine, Column, String, Integer, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import LONGTEXT, TINYTEXT

engine = create_engine('mysql+pymysql://root:root@localhost:8889/accesslog-orm', echo=True)
Base = declarative_base()

class Request(Base):
	__tablename__ = 'requests'

	id = Column(Integer, primary_key=True)
	host = Column(String(20))
	datetime = Column(DateTime)
	request = Column(LONGTEXT)
	statuscode = Column(String(3))
	bot = Column(Boolean)
	os = Column(TINYTEXT)
	platformname = Column(TINYTEXT)
	platformversion = Column(TINYTEXT)
	browsername = Column(TINYTEXT)
	browserversion = Column(TINYTEXT)
	countryname = Column(TINYTEXT)
	countrycode = Column(String(2))
	contenttype = Column(TINYTEXT)
	isPageview = Column(Boolean)

	def __repr__(self):
		return "<Request(request=%s, datetime=%s, isPageview=%s)" % (self.request, self.datetime, self.isPageview)

class Dailypageview(Base):
	__tablename__ = 'dailypageviews_cache'

	id = Column(Integer, primary_key=True)
	daystartdate = Column(DateTime)
	dayenddate = Column(DateTime)
	pageviews = Column(Integer)

Base.metadata.create_all(engine)
