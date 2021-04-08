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
    display.fill_rect(0, 0, 128, 9, 0)
    if not label1 == None:
        display.text(label1, 0, 0, 1)
    
    display.fill_rect(0, 9, 128, 17, 0)
    if not label2 == None:
        display.text(label2, 0, 9, 1)

    display.fill_rect(0, 18, 128, 26, 0)
    if not text_line1 == None:
        display.text(text_line1, 0, 18, 1)
    
    display.fill_rect(0, 27, 128, 35, 0)
    if not text_line2 == None:
        display.text(text_line2, 0, 27, 1)

    display.fill_rect(0, 36, 128, 44, 0)
    if not text_line3 == None:
        display.text(text_line3, 0, 36, 1)

    display.fill_rect(0, 45, 128, 53, 0)
    if not text_line4 == None:
        display.text(text_line4, 0, 45, 1)

    display.fill_rect(0, 54, 128, 63, 0)
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

while True:
    if not wifi.isconnected():
        connect()
    
    is_connected = wifi.isconnected()

    if (is_connected):
        info = wifi.ifconfig()
        rssi = wifi.status('rssi')
        essid = wifi.config('essid')
        rssi_val = ''
        if rssi > -67:
            rssi_val = "Signal: Strong"
        elif rssi > -80:
            rssi_val = "Signal: So-So"
        elif rssi > -90:
            rssi_val = "Signal: Poor"
        else:
            rssi_val = "Signal: Unuseable"

        display_text('WIFI SIGNAL', 'SSID|%s' % essid, '%s' % info[0],'%s' % info[2],'%s' % info[3], '{}'.format(rssi_val), 'RSSI|%s dBm' % rssi)
    else:
        display_text('WIFI SIGNAL', 'STATUS: Not Connected', 'SSID|%s' % SSID)

    time.sleep(.5)
