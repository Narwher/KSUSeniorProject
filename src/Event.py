# Event.py
# Events, Event Handlers, and anything Event related

class EventCategory(Enum):
    None = 0
    EventCategoryHostOrigin = 1
    EventCategoryClientOrigin = 2
    EventCategoryNetwork = 4
    EventCategoryAI = 8
    EventCategoryML = 16

class EventType(Enum):
    #Host general events
    HostInit                #HostInit - Event triggers when the host is initializing, attempts to load required resources before fully starting
    HostStart               #HostStart - Event triggers when the host is started, attempts to start the host, if failed will fatally log and trigger a HostStop event
    HostStop                #HostStop - Event triggers when the host is stopped, attempts to stop the host safely, if failed will report a warning log and attempt to resume
    HostKill                #HostKill - Event triggers when the host is killed, attempts to shut down the host quickly ignoring safety
    #Connection network events
    ClientHostConnect           #ClientConnect - Event triggers when a new client connects
    ClientHostDisconnect        #ClientDisconnect - Event triggers when a client disconnects
    HostClientConnect           #HostClientConnect - Event triggers when a host connects to a client, should only be called if a client loses connection unexpectedly
    HostClientDisconnect        #HostClientDisconnect - Event triggers when host disconnects a client connection
    #Client related events

    #Client log broadcast events
    ClientInfoB             #ClientInfoB - Event triggers when a info broadcast is recieved from a client
    ClientErrorB            #ClientErrorB - Event triggers when an error broadcast is recieved from a client
    ClientWarnB             #ClientWarnB - Event triggers when a warn broadcast is recieved from a client
    ClientFatalB            #ClientFatalB - Event triggers when a fatal broadcast is recieved from a client

    #TODO: Machine learning and Neural Network related events, data storage events, management UI events, emulator error events
