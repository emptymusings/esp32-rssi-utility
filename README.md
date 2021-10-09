# esp32-rssi-utility
A very simple micropython utility to measure RSSI of the ESP-32's WiFi connection to find weak/dead spots in WiFi coverage.

It should be noted that this is not a full tutorial, but simply documents the wiring and method to load the software.

# Index
- [Meaningless Background](#meaningless-background)
- [Requirements](#requirements)
- [Assumptions](#assumptions)
- [Wiring](#wiring)
- [Loading the Software](#loading-the-software)
- [Resources](#resources)
## Meaningless Background
This is a rather simple project I started to familiarize myself with the ESP-32 and the maker space.

I recently decided to get into playing in the maker space.  I had messed around a little with Arduino in the past, mostly just tutorials, but nothing too involved (blinking LEDs, hooking up photoresistors, etc).  

My research brought me to the conclusion that the ESP-32 board was pretty amazing, and I should give it a try.  Once my board arrived, I found myself with a solution in search of a problem.

Then it struck me: there are spots in my house with poor WiFi reception.  Finding an accurate way to determine the best placement for an access point (AP) or range extender would be nice, and wouldn't require a complicated circuit outside of my limited skill level.

## Requirements
- ESP-WROOM-32 dev board (I used [this one](https://www.amazon.com/gp/product/B0718T232Z/ref=ppx_yo_dt_b_asin_title_o03_s00?ie=UTF8&psc=1), but any should do)
- SSD1306 128 x 64 OLED display (I used [this one](https://www.amazon.com/gp/product/B072Q2X2LL/ref=ppx_yo_dt_b_asin_title_o04_s00?ie=UTF8&psc=1))
- A USB-A to USB-micro data cable
- Micropython & IDE (I used VS Code with the Pymakr extension)
- A breadboard and 4 jumper wires
- A portable cell phone battery charger or similar method to power your ESP with external USB power or 5v

## Assumptions
This document will not cover certain requirements, and it is assumed that you have already:
- [Flashed the ESP-32 with micropython](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html#esp32-intro);
- Installed an IDE to code python and upload the project to your ESP-32 or know how to do so with a text editor and python package;

## Wiring 
![](./assets/RSSI%20Detector.png)
- The 3.3V from the ESP-32 connects to the display's VCC pin
- The GND from the ESP-32 connects to the display's GND pin
- Pin 22 from the ESP-32 connects to the display's SCL pin
- Pin 21 from the ESP-32 connects to the display's SDA pin
## Loading the Software
Before you load the software, you should use your favorite micropython IDE (I like VS Code, but uPyCraft or similar will work) to add a file named `secrets.py` to the application's root folder.  Inside the `secrets.py` file, add the following code (replacing the values within the quotes for SSID and password with your network connection information):
```
SSID = "MySSID"
password = "MySuperSecretPassword"
```
Use your favorite way to load a python project to your board, and the program should connect to your wireless network and be able to start displaying RSSI information now.
## Fin
That's it.

## Resources
- [Micorpython docs](https://docs.micropython.org/en/latest/esp32/quickref.html)
- [Installing micropython on ESP boards (and other useful tutorials)](https://randomnerdtutorials.com/getting-started-micropython-esp32-esp8266/)
- [VS Code](https://code.visualstudio.com/download)
- [Pymakr VS Code Extension](https://github.com/pycom/pymakr-vsc)
- [Foundation used for big fonts](https://github.com/nickpmulder/ssd1306big)
