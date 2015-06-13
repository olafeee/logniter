#!/usr/bin/python3
import os,signal,sys, time
from subprocess import call
import threading
import configparser

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
    while True:
        if settings.run is False: break
        #call(["touch", "/etc/logniter/while.txt"])
        print(settings.config['olafelzinga.com']['Path'])
        time.sleep(5)

if __name__ == "__main__":
    settings = settings()
    collector = threading.Thread(target=Collector, args=())
    collector.start()
    signal.signal(signal.SIGTERM, signal_handler)
    signal.pause()