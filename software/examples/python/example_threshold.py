#!/usr/bin/env python
# -*- coding: utf-8 -*-  

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change to your UID

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_sound_intensity import SoundIntensity

# Callback for intensity greater than 2000
def cb_reached(intensity):
    print('Intensity: ' + str(intensity))

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    si = SoundIntensity(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get threshold callbacks with a debounce time of 1 seconds (1000ms)
    si.set_debounce_period(1000)

    # Register threshold reached callback to function cb_reached
    si.register_callback(si.CALLBACK_INTENSITY_REACHED, cb_reached)

    # Configure threshold for "greater than 2000"
    si.set_intensity_callback_threshold('>', 2000, 0)

    raw_input('Press key to exit\n') # Use input() in Python 3
    ipcon.disconnect()
