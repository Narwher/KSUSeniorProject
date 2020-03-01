# Host.py
# Entry point for host program

import log

log.info("Starting host")

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
