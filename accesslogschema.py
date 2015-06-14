import configparser
from sqlalchemy import create_engine, Column, String, Integer, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import LONGTEXT, TINYTEXT
from sqlalchemy.orm import relationship, backref

config = configparser.ConfigParser()
config.read('logniter.config')

dbconfig = config['dbconfig']

enginestring = 'mysql+pymysql://%s:%s@%s:%s/%s' % (
	dbconfig['User'],
	dbconfig['Password'],
	dbconfig['Host'],
	dbconfig['Port'],
	dbconfig['DBName']
)

echo = dbconfig.getboolean('Debug')

engine = create_engine(enginestring, echo=echo)
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

class Dailypageviews(Base):
	__tablename__ = "dailypageviews_cache"

	id = Column(Integer, primary_key=True)
	startdate = Column(DateTime)
	enddate = Column(DateTime)
	pageviews = Column(Integer)

class Weeklypageviews(Base):
	__tablename__ = "weeklypageviews_cache"

	id = Column(Integer, primary_key=True)
	startdate = Column(DateTime)
	enddate = Column(DateTime)
	pageviews = Column(Integer)

class Monthlypageviews(Base):
	__tablename__ = "monthlypageviews_cache"

	id = Column(Integer, primary_key=True)
	startdate = Column(DateTime)
	enddate = Column(DateTime)
	pageviews = Column(Integer)

class Yearlypageviews(Base):
	__tablename__ = "yearlypageviews_cache"

	id = Column(Integer, primary_key=True)
	startdate = Column(DateTime)
	enddate = Column(DateTime)
	pageviews = Column(Integer)

class DailypageviewsPerCountry(Base):
	__tablename__ = "dailypageviewspercountry_cache"

	id = Column(Integer, primary_key=True)
	startdate = Column(DateTime)
	enddate = Column(DateTime)
	countrycode = Column(String(2))
	pageviews = Column(Integer)
	totaldailypageviews_id = Column(Integer, ForeignKey("dailypageviews_cache.id"))
	
	totaldailypageviews = relationship("Dailypageviews", backref=backref("dailypageviewspercountry", order_by=id))

class WeeklypageviewsPerCountry(Base):
	__tablename__ = "weeklypageviewspercountry_cache"

	id = Column(Integer, primary_key=True)
	startdate = Column(DateTime)
	enddate = Column(DateTime)
	countrycode = Column(String(2))
	pageviews = Column(Integer)
	totalweeklypageviews_id = Column(Integer, ForeignKey("weeklypageviews_cache.id"))
	
	totalweeklypageviews = relationship("Weeklypageviews", backref=backref("weeklypageviewspercountry", order_by=id))

class MonthlypageviewsPerCountry(Base):
	__tablename__ = "monthlypageviewspercountry_cache"

	id = Column(Integer, primary_key=True)
	startdate = Column(DateTime)
	enddate = Column(DateTime)
	countrycode = Column(String(2))
	pageviews = Column(Integer)
	totalmonthlypageviews_id = Column(Integer, ForeignKey("monthlypageviews_cache.id"))
	
	totalmonthlypageviews = relationship("Monthlypageviews", backref=backref("monthlypageviewspercountry", order_by=id))

class YearlypageviewsPerCountry(Base):
	__tablename__ = "yearlypageviewspercountry_cache"

	id = Column(Integer, primary_key=True)
	startdate = Column(DateTime)
	enddate = Column(DateTime)
	countrycode = Column(String(2))
	pageviews = Column(Integer)
	totalyearlypageviews_id = Column(Integer, ForeignKey("yearlypageviews_cache.id"))
	
	totalyearlypageviews = relationship("Yearlypageviews", backref=backref("yearlypageviewspercountry", order_by=id))

Base.metadata.create_all(engine)