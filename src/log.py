# logger.py
#

import time
import datetime

def info(s):
    # dt = datetime.now().time()
    print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'), "INFO:", s)

def error(s):
    print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'), "ERROR:", s)

def warn(s):
    print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'), "WARN:", s)

def fatal(s):
    print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'), "FATAL:", s)
