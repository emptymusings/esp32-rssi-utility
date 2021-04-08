import ssd1306
from machine import SoftI2C, Pin
import time
import network, socket
import secrets

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=400000)
display = ssd1306.SSD1306_I2C(128, 64, i2c)

display.fill(1)
display.show()

def display_text(label1=None,label2=None,text_line1=None,text_line2=None,text_line3=None,text_line4=None, text_line5=None):
    display.fill_rect(0, 0, 128, 64, 0)
    if not label1 == None:
        display.text(label1, 0, 0, 1)
    
    if not label2 == None:
        display.text(label2, 0, 9, 1)
    
    if not text_line1 == None:
        display.text(text_line1, 0, 18, 1)
    
    if not text_line2 == None:
        display.text(text_line2, 0, 27, 1)

    if not text_line3 == None:
        display.text(text_line3, 0, 36, 1)

    if not text_line4 == None:
        display.text(text_line4, 0, 45, 1)

    if not text_line5 == None:
        display.text(text_line5, 0, 54, 1)

    display.show()

def display_clear():
    display_text()

SSID = secrets.SSID
password = secrets.password

wifi = network.WLAN(network.STA_IF)
wifi.active(True)

def connect():
    wifi.connect(SSID, password)
    pending = ''
    
    while not wifi.isconnected():
        pending += '.'
        display_text("WIFI SIGNAL", "Connecting...", "SSID: {}".format(SSID), None, "Connecting", "{}".format(pending))
        time.sleep(.5)
        pass

    status = "Not Connected"
    
    if wifi.isconnected():
        status = "Connected!"

    display_text("WIFI SIGNAL", "{}".format(status), "SSID: {}".format(SSID))

def get_rssi():
    rssis = []

    while True:
        if not wifi.isconnected():
            connect()
        
        is_connected = wifi.isconnected()

        if (is_connected):
            info = wifi.ifconfig()
            rssi = wifi.status('rssi')
            essid = wifi.config('essid')
            
            if len(rssis) > 10:
                rssis.pop(0)

            rssis.append(rssi)
            avg_rssi = round(sum(rssis) / len(rssis))

            rssi_val = ''
            if rssi > -67:
                rssi_val = "Signal:Strong"
            elif rssi > -80:
                rssi_val = "Signal:So-So"
            elif rssi > -90:
                rssi_val = "Signal:Poor"
            else:
                rssi_val = "Signal:Unuseable"

            display_text('WIFI SIGNAL', 'SSID|%s' % essid, '{}'.format(rssi_val), 'RSSI: %s dBm' % rssi, "Avg:  %s dBm" % avg_rssi)
        else:
            display_text('WIFI SIGNAL', 'STATUS: Not Connected', 'SSID|%s' % SSID)

        time.sleep(.5)

get_rssi()