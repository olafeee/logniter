#!/usr/bin/python3
import os,signal,sys, time
from subprocess import call
import threading
import configparser
from collect import logHandler

class settings():
     def __init__(self):
         self.run = True
         self.config = configparser.ConfigParser()
         self.config.read('logniter.config')
          
def signal_handler(signal, frame):
    settings.run = False
    t.join()
    call(["touch", "/etc/logniter/exit.txt"])
    sys.exit(0)

def Collector():
    pal = logHandler(settings)
    pal.processAccesLog()

if __name__ == "__main__":
    settings = settings()

    collector = threading.Thread(target=Collector, args=())
    collector.start()
    
    signal.signal(signal.SIGTERM, signal_handler)
    signal.pause()