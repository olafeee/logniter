#!/usr/bin/python3
import os,signal,sys, time
from subprocess import call
import threading
import configparser
from time import sleep
from multiprocessing.pool import ThreadPool

from collect import logHandler
#from cachecruncher import cacheCruncher

class settings():
     def __init__(self):
         self.run = True
         self.config = configparser.ConfigParser()
         self.config.read('logniter.config')
         self.poolrun = False
         self.hsr = int(time.strftime("%M"))-1 #hour of last run
          
def signal_handler(signal, frame):
    settings.run = False
    try:
        pool.join()
    except:
        x = 1
    collector.join()
    call(["touch", "/etc/logniter/exit.txt"])
    sys.exit(0)

def Collector():
    while settings.run is True:
        if settings.hsr != time.strftime("%M"):
            pool_size = 1
            pool = ThreadPool(pool_size)
            for i in range(pool_size):
                pool.apply_async(Consumer, args=(time.strftime("%M"),))
            pool.close()
            settings.hsr = time.strftime("%M")
            #sommen = open('x.log',"w")
            #sommen.close()
        call(["touch", "/etc/logniter/exit.txt"])
        time.sleep(5)

def Consumer(x):
    #pal.processAccesLog() 
    #cc.processDailypageviews()
    #cc.processDailypageviewsPerCountry()
    call(["touch", "/etc/logniter/test12312312polzei.txt"])

if __name__ == "__main__":
    #load classes
    settings = settings() 
    #no
    call(["touch", "/etc/logniter/voordat henkie klapt.txt"])
    pal = logHandler(settings)
    #cc = cacheCruncher()
    #start thread
    collector = threading.Thread(target=Collector, args=())
    collector.start()
    #signal
    signal.signal(signal.SIGTERM, signal_handler)
    signal.pause()