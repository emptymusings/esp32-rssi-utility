# Aside from some minor changes to the way large font 4's display, all large font letters and numbers are as designed
# in the github above

from machine import SoftI2C, Pin
import ssd1306, time
import bigfont

class Display():

    def __init__(self, scl_pin=22, sda_pin=21, frequency=400000, width=128, height=64):
        i2c = SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin), freq=frequency)
        self.display = ssd1306.SSD1306_I2C(width, height, i2c)
        self.display.invert(True)
        self.display.fill(1)
        self.display.show()
        time.sleep(2)
        self.display.invert(False)
        self.display.fill(0)
        self.display.show()

    def display_text(self, label1=None,label2=None,text_line1=None,text_line2=None,text_line3=None,text_line4=None, text_line5=None, show_immediately=True):
        # Clear the screen        
        self.display.fill_rect(0, 0, 128, 16, 0)
        self.display.fill_rect(0, 17, 128, 64, 0)

        # Determine if there is a value for the first label line
        if not label1 == None:
            self.display.text(label1, 0, 0, 1)
        
        # Determine if there is a value for the second label line
        if not label2 == None:
            self.display.text(label2, 0, 9, 1)
        
        # Fill any assignments for the remaining lines
        if not text_line1 == None:
            self.display.text(text_line1, 0, 18, 1)
        
        if not text_line2 == None:
            self.display.text(text_line2, 0, 27, 1)

        if not text_line3 == None:
            self.display.text(text_line3, 0, 36, 1)

        if not text_line4 == None:
            self.display.text(text_line4, 0, 45, 1)

        if not text_line5 == None:
            self.display.text(text_line5, 0, 54, 1)

        if show_immediately:
            self.display.show()

    def display_clear(self):
        self.display_text()

    def display_wifi_signal(self, avg_rssi=-90):  

        if avg_rssi >= -80:
            self.display.fill_rect(85, 54, 6, 63, 1)
        
        if avg_rssi >= -70:
            self.display.fill_rect(95, 50, 6, 63, 1)
        
        if avg_rssi >= -60:
            self.display.fill_rect(105, 46, 6, 63, 1)

        if avg_rssi >= -50:
            self.display.fill_rect(115, 42, 6, 63, 1)

        self.display_avg_rssi(avg_rssi)
        self.display.show()
    
    def display_avg_rssi(self, avg_rssi=-90):
        rssi_text = str(avg_rssi)
        xval = 0
        yval = 48

        label_y = 30
        bigfont.text_large("RSSI", xval, label_y, self.display)
        bigfont.text_large(rssi_text, xval, yval, self.display)
        self.display.show()
