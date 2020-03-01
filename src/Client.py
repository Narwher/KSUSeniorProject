# Client.py
# Entry point for client program

import Log
from Event import ClientFatalBEvent

import time

Log.info("Starting client")

#Event stack
e = []

#test code
testEvent = ClientFatalBEvent("127.0.0.1", "Test message")
e.append(testEvent)
#end test code

def loop():
    running = True
    while running:
        #execution goes here
        #Event handling
        for i in range(0, len(e)):
            e.pop(0).fire()

loop()
