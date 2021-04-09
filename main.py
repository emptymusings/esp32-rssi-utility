from machine import Pin
import network, socket, time # import micropython items

import secrets
from display import Display

connection_pin = Pin(2, Pin.OUT)
connection_pin.value(0)

# Initialize the display
display = Display()

# Get the Super Secret SSID and network password
SSID = secrets.SSID
password = secrets.password

# Initialize the wireless NIC
wifi = network.WLAN(network.STA_IF)
wifi.active(True)


def connect():
    """Function to connect to the wireless network."""
    print("Connecting to WiFi")
    wifi.connect(SSID, password)
    attempt = 1
    pending = ''
    print("Connecting to %s" % SSID)
    while not wifi.isconnected() and attempt <= 60:        
        cnx = connection_pin.value()
        cnx = 1 - cnx
        connection_pin.value(cnx)
        pending += '.'
        display.display_text("WiFi STRENGTH", "Connecting...", "SSID: {}".format(SSID), None, "Connecting", "{}".format(pending))
        print("{}".format( pending), end='')
        time.sleep(.5)
        attempt += 1

        if len(pending) > 15:
            pending = ''

        pass

    print()
    status = "Not Connected"
    
    if wifi.isconnected():
        connection_pin.value(1)
        status = "Connected!"
        print("Connected after {} attempts".format(attempt))
    else:
        connection_pin.value(0)
        print("Failed after {} attempts".format(attempt))

    display.display_text("WiFi STRENGTH", "{}".format(status), "SSID: {}".format(SSID))
    print("{} {}".format(SSID, status))


def get_rssi_strength(rssi):
    rssi_val = ''    
    if rssi > -50:
        rssi_val = "Signal:Great!"
    elif rssi > -60:
        rssi_val = "Signal:OK"
    elif rssi > -70:
        rssi_val = "Signal:Weak"
    else:
        rssi_val = "Signal:Not Good"

    return rssi_val

def show_rssi(rssis):
    rssi = wifi.status('rssi')
    essid = wifi.config('essid')
            
    if len(rssis) >= 20:
        rssis.pop(0)

    rssis.append(rssi)
    avg_rssi = round(sum(rssis) / len(rssis))

    rssi_val = get_rssi_strength(rssi)
    
    display.display_text('WiFi STRENGTH', '%s' % essid, '{}'.format(rssi_val), show_immediately=False)
    display.display_wifi_signal(avg_rssi)

def get_rssi():
    rssis = []

    while True:
        if not wifi.isconnected():
            connect()
        
        is_connected = wifi.isconnected()

        if (is_connected):            
            show_rssi(rssis)
        else:
            print("Not connected, not retrieving RSSI info")
            display.display_text('WiFi STRENGTH', 'STATUS: Not Connected', '%s' % SSID)

        time.sleep(.5)

get_rssi()