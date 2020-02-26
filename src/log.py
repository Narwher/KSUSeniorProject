# logger.py
# A general purpose logger

import time
import datetime

# General info logging
def info(s):
    print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'), "INFO:", s)

# General info logging which broadcasts to the host
def binfo(s):
    info(s)

# Error logging
# General non critical errors
def error(s):
    print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'), "ERROR:", s)

# Error log which broadcasts to the host
def berror(s):
    error(s)

# Warning logging
# Will be called for critical errors not detrimental enough to kill the client or those what may damage data integrity
def warn(s):
    print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'), "WARN:", s)

# Warning log which broadcasts to the host
def bwarn(s):
    warn(s)

# Fatal log
# Will only be called for program errors critical enough to kill the client
def fatal(s):
    bfatal(s)

#Fatal log which broadcasts to the host
def bfatal(s):
    print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'), "FATAL:", s)
