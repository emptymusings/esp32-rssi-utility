# Fonts for RSSI label and its average value based on work done by nickpmulder's SSD1306big for larger fonts with SSD1306.
# Unfortunately, because nickpmulder's work was based on the RPi Pico, it doesn't look like his driver
# would work on the ESP32 due to memory constraints.  So I borrowed the the "fonts" laid out for numbers,
# minus, and the 3 letters, and put them as functions here/made a few adjustments to better fit my limited needs.
# The github for nickpmulder's project is https://github.com/nickpmulder/ssd1306big

# Aside from some minor changes to the way large font 4's display, all large font letters and numbers are as designed
# in the github above

from machine import SoftI2C, Pin
import ssd1306

class Display():

    def __init__(self, scl_pin=22, sda_pin=21, frequency=400000, width=128, height=64):
        i2c = SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin), freq=frequency)
        self.display = ssd1306.SSD1306_I2C(width, height, i2c)
        
        self.display.fill(1)
        self.display.show()

    def display_text(self, label1=None,label2=None,text_line1=None,text_line2=None,text_line3=None,text_line4=None, text_line5=None, show_immediately=True):
        # Clear the screen
        self.display.fill_rect(0, 0, 128, 64, 0)

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
        xincrement = 12

        R(0, 30, self.display)
        S(12, 30, self.display)
        S(24, 30, self.display)
        I(36, 30, self.display)
        
        for i in range(len(rssi_text)):
            if rssi_text[i] == "-":
                minus(xval, yval, self.display)
            elif rssi_text[i] == "1":
                one(xval, yval, self.display)
            elif rssi_text[i] == "2":
                two(xval, yval, self.display)
            elif rssi_text[i] == "3":
                three(xval, yval, self.display)
            elif rssi_text[i] == "4":
                four(xval, yval, self.display)
            elif rssi_text[i] == "5":
                five(xval, yval, self.display)
            elif rssi_text[i] == "6":
                six(xval, yval, self.display)
            elif rssi_text[i] == "7":
                seven(xval, yval, self.display)
            elif rssi_text[i] == "8":
                eight(xval, yval, self.display)
            elif rssi_text[i] == "9":
                nine(xval, yval, self.display)
            else:
                zero(xval, yval, self.display)
            
            xval += xincrement


def I(x, y, display):
    display.line((x)+1,(y)+1,(x)+9,(y)+1,1)
    display.line((x)+1,(y)+15,(x)+9,(y)+15,1)
    display.line((x)+5,(y)+15,(x)+5,(y)+1,1)    
    
def R(x, y, display):
    display.line((x)+1,(y)+15,(x)+1,(y)+1,1)
    display.line((x)+1,(y)+1,(x)+7,(y)+1,1)
    display.line((x)+7,(y)+1,(x)+9,(y)+4,1)
    display.line((x)+9,(y)+4,(x)+9,(y)+6,1)
    display.line((x)+9,(y)+6, (x)+6,(y)+9,1)
    display.line((x)+5,(y)+9,(x)+1,(y)+9,1)
    display.line((x)+5,(y)+9,(x)+9,(y)+15,1)    
    
def S(x, y, display):
    display.line((x)+9,(y)+2,(x)+7,(y)+1,1)
    display.line((x)+7,(y)+1,(x)+3,(y)+1,1)
    display.line((x)+3,(y)+1,(x)+2,(y)+2,1)
    display.line((x)+3,(y)+1,(x)+2,(y)+2,1)    
    display.line((x)+2,(y)+2,(x)+1,(y)+5,1)
    display.line((x)+1,(y)+5,(x)+5,(y)+7,1)
    display.line((x)+5,(y)+7,(x)+9,(y)+8,1)
    display.line((x)+9,(y)+8,(x)+10,(y)+11,1)
    display.line((x)+10,(y)+11,(x)+10,(y)+13,1)
    display.line((x)+10,(y)+13,(x)+7,(y)+15,1)
    display.line((x)+7,(y)+15,(x)+4,(y)+15,1)
    display.line((x)+4,(y)+15,(x)+1,(y)+13,1)        

def minus(x, y, display):
    display.line((x)+2, (y)+8, (x)+8, (y)+8, 1)

def zero(x, y, display):
    display.line((x)+10,(y)+5,(x)+8,(y)+1,1)
    display.line((x)+8,(y)+1,(x)+4,(y)+1,1)
    display.line((x)+4,(y)+1,(x)+2,(y)+3,1)
    display.line((x)+2,(y)+3,(x)+1,(y)+7,1)
    display.line((x)+1,(y)+7,(x)+1,(y)+12,1)
    display.line((x)+1,(y)+12,(x)+4,(y)+15,1)
    display.line((x)+4,(y)+15,(x)+7,(y)+15,1)
    display.line((x)+7,(y)+15,(x)+10,(y)+12,1)
    display.line((x)+10,(y)+12,(x)+10,(y)+5,1)
    display.line((x)+9,(y)+4,(x)+2,(y)+12,1)
    

def one(x, y, display):
    display.line((x)+5,(y)+15,(x)+5,(y)+1,1)
    display.line((x)+5,(y)+1,(x)+2,(y)+3,1)
    

def two(x, y, display):
    display.line((x)+1,(y)+3,(x)+2,(y)+1,1)
    display.line((x)+2,(y)+1,(x)+7,(y)+1,1)    
    display.line((x)+7,(y)+1,(x)+9,(y)+3,1)
    display.line((x)+9,(y)+3,(x)+9,(y)+6,1)
    display.line((x)+9,(y)+6,(x)+2,(y)+13,1)
    display.line((x)+2,(y)+13,(x)+1,(y)+15,1)
    display.line((x)+1,(y)+15,(x)+10,(y)+15,1)
    
    

def three(x, y, display):
    display.line((x)+1,(y)+3,(x)+2,(y)+1,1)
    display.line((x)+2,(y)+1,(x)+7,(y)+1,1)    
    display.line((x)+7,(y)+1,(x)+9,(y)+3,1)
    display.line((x)+9,(y)+3,(x)+9,(y)+5,1)
    display.line((x)+9,(y)+5,(x)+7,(y)+7,1)
    display.line((x)+7,(y)+7,(x)+4,(y)+7,1)    
    display.line((x)+7,(y)+8,(x)+9,(y)+9,1)
    display.line((x)+9,(y)+9,(x)+9,(y)+12,1)
    display.line((x)+9,(y)+12,(x)+7,(y)+15,1)
    display.line((x)+7,(y)+15,(x)+3,(y)+15,1)
    display.line((x)+3,(y)+15,(x)+1,(y)+13,1)    

    

def four(x, y, display):
    display.line((x)+8,(y)+1,(x)+8,(y)+15,1)
    display.line((x)+8,(y)+1,(x)+1,(y)+9,1)
    display.line((x),(y)+10,(x)+10,(y)+10,1)
    

def five(x, y, display):
    display.line((x)+9,(y)+1,(x)+1,(y)+1,1)
    display.line((x)+1,(y)+1,(x)+1,(y)+7,1)
    display.line((x)+7,(y)+7,(x)+1,(y)+7,1)    
    display.line((x)+7,(y)+8,(x)+9,(y)+9,1)
    display.line((x)+9,(y)+9,(x)+9,(y)+12,1)
    display.line((x)+9,(y)+12,(x)+7,(y)+15,1)
    display.line((x)+7,(y)+15,(x)+3,(y)+15,1)
    display.line((x)+3,(y)+15,(x)+1,(y)+13,1)
    

def six(x, y, display):
    display.line((x)+10,(y)+3,(x)+8,(y)+1,1)
    display.line((x)+8,(y)+1,(x)+4,(y)+1,1)
    display.line((x)+4,(y)+1,(x)+2,(y)+3,1)
    display.line((x)+2,(y)+3,(x)+1,(y)+7,1)
    display.line((x)+1,(y)+7,(x)+1,(y)+12,1)
    display.line((x)+1,(y)+12,(x)+4,(y)+15,1)
    display.line((x)+4,(y)+15,(x)+7,(y)+15,1)
    display.line((x)+7,(y)+15,(x)+10,(y)+13,1)
    display.line((x)+10,(y)+13,(x)+10,(y)+9,1)
    display.line((x)+10,(y)+9,(x)+8,(y)+7,1)
    display.line((x)+8,(y)+7,(x)+4,(y)+7,1)
    display.line((x)+4,(y)+7,(x)+2,(y)+9,1)
    
    

def seven(x, y, display):
    display.line((x)+1,(y)+1,(x)+10,(y)+1,1)
    display.line((x)+10,(y)+1,(x)+3,(y)+15,1)
    
    
def eight(x, y, display):
    display.line((x)+4,(y)+7,(x)+2,(y)+5,1)
    display.line((x)+2,(y)+5,(x)+2,(y)+3,1)
    display.line((x)+2,(y)+3,(x)+3,(y)+2,1)
    display.line((x)+3,(y)+2,(x)+4,(y)+1,1)
    display.line((x)+4,(y)+1,(x)+6,(y)+1,1)
    display.line((x)+6,(y)+1,(x)+7,(y)+2,1)
    display.line((x)+7,(y)+2,(x)+8,(y)+3,1)
    display.line((x)+8,(y)+3,(x)+8,(y)+5,1)
    display.line((x)+8,(y)+5,(x)+6,(y)+7,1)
    display.line((x)+1,(y)+10,(x)+1,(y)+13,1)
    display.line((x)+1,(y)+13,(x)+3,(y)+15,1)
    display.line((x)+3,(y)+15,(x)+7,(y)+15,1)
    display.line((x)+7,(y)+15,(x)+9,(y)+13,1)
    display.line((x)+9,(y)+13,(x)+9,(y)+10,1)
    display.line((x)+9,(y)+10,(x)+6,(y)+7,1)
    display.line((x)+6,(y)+7,(x)+4,(y)+7,1)
    display.line((x)+4,(y)+7,(x)+2,(y)+9,1)
    
    

def nine(x, y, display):
    display.line((x)+10,(y)+6,(x)+8,(y)+8,1)
    display.line((x)+8,(y)+8,(x)+3,(y)+8,1)
    display.line((x)+3,(y)+8,(x)+1,(y)+5,1)
    display.line((x)+1,(y)+5,(x)+1,(y)+3,1)
    display.line((x)+1,(y)+3,(x)+3,(y)+1,1)
    display.line((x)+3,(y)+1,(x)+8,(y)+1,1)
    display.line((x)+8,(y)+1,(x)+10,(y)+3,1)
    display.line((x)+10,(y)+3,(x)+10,(y)+10,1)
    display.line((x)+10,(y)+10,(x)+9,(y)+13,1)
    display.line((x)+9,(y)+13,(x)+7,(y)+15,1)
    display.line((x)+7,(y)+15,(x)+3,(y)+15,1)
    display.line((x)+3,(y)+15,(x)+1,(y)+13,1)
