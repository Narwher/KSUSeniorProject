# emulator.py
# Talks to emulator software and core application, receives data from MLNN

import log
import mlnn

import numpy
import pyvjoy

from mss import mss

class Emulator():

    # Integer assigned to Xinput value
    buttonID = None

    # Gathered pixel data via MSS, piped to MLNN
    getPixels = []

    # intialize emulator class
    def __init__(self):
        pass

    # check if button pressed
    def checkButtonPressed(buttonID):
        pass

    # check if button released
    def checkButtonReleased(buttonID):
        pass
