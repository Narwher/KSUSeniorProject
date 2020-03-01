# Client.py
# Entry point for client program

import Log
from Event import ClientFatalBEvent

Log.info("Starting client")

testEvent = ClientFatalBEvent("127.0.0.1", "Test message")
testEvent.fire()
