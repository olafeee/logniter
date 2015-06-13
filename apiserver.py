import bottle
from bottle import route, request, post
from bottle.ext.sqlalchemy import SQLAlchemyPlugin
from accesslogschema import engine, Base, Dailypageviews, DailypageviewsPerCountry
from sqlalchemy.orm.session import sessionmaker
        
@post('/test')
def test(db):
	allDailypageviewsPerCountry = db.query(DailypageviewsPerCountry).all()
	
	startdate = request.json['startdate']
	enddate = request.json['enddate']
	
	alldpvDict = {'data' : []}
	
	for dailyPageviewsPerCountry in allDailypageviewsPerCountry:
		tempDict = {'id' : dailyPageviewsPerCountry.id,
				'pageviews' : dailyPageviewsPerCountry.pageviews,
				'countrycode' : dailyPageviewsPerCountry.countrycode,
				'startdate' : 'TODO',
				'enddate' : 'TODO'}
		alldpvDict['data'].append(tempDict)

	return alldpvDict

if __name__ == '__main__':
	bottle.install(SQLAlchemyPlugin(engine, Base.metadata, create=True))
	bottle.run(host='localhost', port=8080, debug=True, reloader=True)