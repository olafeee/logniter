import bottle
from bottle import Bottle, run, request
from bottle.ext.sqlalchemy import SQLAlchemyPlugin
from accesslogschema import engine, Base, Dailypageviews, DailypageviewsPerCountry
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.sql.expression import and_, func
from datetime import datetime

class APIServer(object):

    app = Bottle()
    
    def __init__(self):
        print('api app started')
        self.app.install(SQLAlchemyPlugin(engine, Base.metadata, create=True))
        run(self.app, host='localhost', port=8080, debug=True, reloader=True)

    def closeServer(self):
        print('app close')
        self.app.close()

    @app.post('/pageviewspercountry')
    def pageviewspercountry(db):
        
        startdatestring = request.json['startdate']
        enddatestring = request.json['enddate']
        dateformat = '%d-%m-%Y'
        
        startdate = datetime.strptime(startdatestring, dateformat)
        enddate = datetime.strptime(enddatestring, dateformat)
        
        selectedDailypageviewsPerCountry = db.query(DailypageviewsPerCountry, func.count(DailypageviewsPerCountry.pageviews)).filter(
            and_(DailypageviewsPerCountry.startdate >= startdate,
            DailypageviewsPerCountry.enddate <= enddate)).group_by(DailypageviewsPerCountry.countrycode)
        
        returnDict = {'postdata' : request.json, 'returndata' : []}

        for dailyPageviewsPerCountry in selectedDailypageviewsPerCountry:
            
            tempDict = {'pageviews' : dailyPageviewsPerCountry[1],
                    'countrycode' : dailyPageviewsPerCountry[0].countrycode}

            returnDict['returndata'].append(tempDict)

        return returnDict
    