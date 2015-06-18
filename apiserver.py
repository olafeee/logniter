import bottle
from bottle import Bottle, run, request
from bottle.ext.sqlalchemy import SQLAlchemyPlugin
from accesslogschema import engine, Base, Dailypageviews, DailypageviewsPerCountry, Monthlypageviews, Weeklypageviews, Request
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.sql.expression import and_, func, between
from datetime import datetime
from calendar import month_name

class APIServer(object):

    app = Bottle()

    def startServer(self):
        self.app.install(SQLAlchemyPlugin(engine, Base.metadata, create=True))
        run(self.app, host='localhost', port=8080, debug=False, reloader=True)


    def closeServer(self):
        #print('app close')
        self.app.close()

    @app.post('/pageviewspercountry')
    def pageviewspercountry(db):
        
        startdatestring = request.json['startdate']
        enddatestring = request.json['enddate']
        dateformat = '%d-%m-%Y'
        
        startdate = datetime.strptime(startdatestring, dateformat)
        enddate = datetime.strptime(enddatestring, dateformat)
        
        selectedDailypageviewsPerCountry = db.query(DailypageviewsPerCountry.countrycode, func.count(DailypageviewsPerCountry.pageviews)).filter(
            and_(DailypageviewsPerCountry.startdate >= startdate,
            DailypageviewsPerCountry.enddate <= enddate)).group_by(DailypageviewsPerCountry.countrycode)
        
        returnDict = {'postdata' : request.json, 'returndata' : []}

        for dailyPageviewsPerCountry in selectedDailypageviewsPerCountry:
            
            tempDict = {'pageviews' : dailyPageviewsPerCountry[1],
                    'countrycode' : dailyPageviewsPerCountry[0]}

            returnDict['returndata'].append(tempDict)

        return returnDict

    @app.post('/pageviewspermonth')
    def pageviewspermonth(db):

        year = request.json['year']

        selectedPageviewsPerMonth = db.query(func.month(Monthlypageviews.startdate), Monthlypageviews.pageviews).filter(func.year(Monthlypageviews.startdate)==year).group_by(func.month(Monthlypageviews.startdate))

        returnDict = {'postdata' : request.json, 'returndata' : []}

        for pageviewsPerMonth in selectedPageviewsPerMonth:

            tempDict = {'monthnumber' : pageviewsPerMonth[0],
                    'montname' : month_name[pageviewsPerMonth[0]],
                    'pageviews' : pageviewsPerMonth[1]}

            returnDict['returndata'].append(tempDict)

        return returnDict

    @app.post('/pageviewsperweek')
    def pageviewsperweek(db):

        year = request.json['year']

        selectedPageviewsPerWeek = db.query(func.week(Weeklypageviews.startdate), Weeklypageviews.pageviews).filter(func.year(Weeklypageviews.startdate)==year).group_by(func.week(Weeklypageviews.startdate))

        returnDict = {'postdata' : request.json, 'returndata' : []}

        for pageviewsPerWeek in selectedPageviewsPerWeek:
            tempDict = {'weeknumber' : pageviewsPerWeek[0],
                    'pageviews' : pageviewsPerWeek[1]}

            returnDict['returndata'].append(tempDict)
            print(returnDict)

        return returnDict

    @app.post('/clientstats')
    def clientstats(db):
        startdatestring = request.json['startdate']
        enddatestring = request.json['enddate']
        dateformat = '%d-%m-%Y'

        startdate = datetime.strptime(startdatestring, dateformat)
        enddate = datetime.strptime(enddatestring, dateformat)

        selectedRequestsBrowser = db.query(Request.browsername, func.count(Request.browsername)).filter_by(isPageview=True).filter(Request.datetime.between(startdate, enddate)).group_by(Request.browsername)
        selectedRequestsPlatform = db.query(Request.platformname, func.count(Request.platformname)).filter_by(isPageview=True).filter(Request.datetime.between(startdate, enddate)).group_by(Request.platformname)

        returnDict = {'postdata' : request.json, 'returndata' : {'browserstats' : [], 'platformstats' : []}}

        for selectedRequestBrowser in selectedRequestsBrowser:
            tempDict = {'browser' : selectedRequestBrowser[0],
            'pageviews' : selectedRequestBrowser[1]}

            returnDict['returndata']['browserstats'].append(tempDict)

        for selectedRequestPlatform in selectedRequestsPlatform:
            tempDict = {'platform' : selectedRequestPlatform[0],
            'pageviews' : selectedRequestPlatform[1]}

            returnDict['returndata']['platformstats'].append(tempDict)

        return returnDict

if __name__ == "__main__":
    apiserver = APIServer()

    