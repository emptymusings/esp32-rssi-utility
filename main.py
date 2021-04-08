from machine import Pin
import network, socket, time # import micropython items

import secrets
from display import Display


SSID = secrets.SSID
password = secrets.password

wifi = network.WLAN(network.STA_IF)
wifi.active(True)

display = Display()

def connect():
    wifi.connect(SSID, password)
    pending = ''
    
    while not wifi.isconnected():
        pending += '.'
        display.display_text("WiFi STRENGTH", "Connecting...", "SSID: {}".format(SSID), None, "Connecting", "{}".format(pending))
        time.sleep(.5)
        pass

    status = "Not Connected"
    
    if wifi.isconnected():
        status = "Connected!"

    display.display_text("WiFi STRENGTH", "{}".format(status), "SSID: {}".format(SSID))

def get_rssi_strength(rssi):
    rssi_val = ''
        
    if rssi > -67:
        rssi_val = "Signal:Strong"
    elif rssi > -80:
        rssi_val = "Signal:So-So"
    elif rssi > -90:
        rssi_val = "Signal:Poor"
    else:
        rssi_val = "Signal:Unuseable"

    return rssi_val

def show_rssi(rssis):
    info = wifi.ifconfig()
    rssi = wifi.status('rssi')
    essid = wifi.config('essid')
            
    if len(rssis) > 20:
        rssis.pop(0)

    rssis.append(rssi)
    avg_rssi = round(sum(rssis) / len(rssis))

    rssi_val = get_rssi_strength(rssi)

    #display.display_text('WiFi STRENGTH', 'SSID|%s' % essid, '{}'.format(rssi_val), 'RSSI: %s dBm' % rssi, "Avg:  %s dBm" % avg_rssi)
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
            display.display_text('WiFi STRENGTH', 'STATUS: Not Connected', '%s' % SSID)

        time.sleep(.5)

get_rssi()