# Event.py
# Events, Event Handlers, and anything Event related

import Log


#Core event class
class Event(object):

    #check if handled
    handled = False
    #base class, pass on init
    def init(self):
        pass

    #base class, pass on fire
    def fire(self):
        if handled :
            return
        pass

    def isHandled():
        return handled

#------------------
#   Currently unused Events
#------------------
#class HostInitEvent(Event):
#class HostStartEvent(Event):
#class HostStopEvent(Event):
#class HostKillEvent(Event):
#class ClientHostConnectEvent(Event):
#class ClientHostConnectEvent(Event):
#class ClientHostDisconnectEvent(Event):
#class HostClientConnect(Event):
#class HostClientDisconnect(Event):


#------------------
#   Client log broadcast Events
#------------------
class ClientInfoBEvent(Event):
    ip = None
    message = None

    def __init__(self, ip, message):
        self.ip = ip
        self.message = message

    def fire(self):
        Log.info("[" + self.ip + "] INFO: " + self.message)
        isHandled = True

class ClientErrorBEvent(Event):
    ip = None
    message = None

    def __init__(self, ip, message):
        self.ip = ip
        self.message = message

    def fire(self):
        Log.info("[" + self.ip + "] ERROR: " + self.message)
        isHandled = True
class ClientWarnBEvent(Event):
    ip = None
    message = None

    def __init__(self, ip, message):
        self.ip = ip
        self.message = message

    def fire(self):
        Log.info("[" + self.ip + "] WARN: " + self.message)
        isHandled = True
class ClientFatalBEvent(Event):
    ip = None
    message = None

    def __init__(self, ip, message):
        self.ip = ip
        self.message = message

    def fire(self):
        Log.info("[" + self.ip + "] FATAL: " + self.message)
        isHandled = True
