# Aside from some minor changes to the way large font 4's display, all large font letters and numbers are as designed
# in the github above

from machine import SoftI2C, Pin
import ssd1306, time
import connection

class Display():

    def __init__(self, scl_pin=22, sda_pin=21, frequency=400000, width=128, height=64):
        i2c = SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin), freq=frequency)
        self.display = ssd1306.SSD1306_I2C(width, height, i2c)
        
        self.display_width = width
        self.display_height = height
        self.is_inverted = True
        self.clear()
        self.display.fill(1)
        self.display.show()
        self.clear()
        self.is_inverted = False

    def clear(self):
        self.display.fill_rect(0, 0, self.display_width, self.display_height, self.is_inverted)

    def color(self):
        if (self.is_inverted):
            return 0
        
        return 1

    def display_text(self, label1=None,label2=None,text_line1=None,text_line2=None,text_line3=None,text_line4=None, text_line5=None, show_immediately=True):
        # Clear the screen        
        self.clear()

        font_color = self.color()

        # Determine if there is a value for the first label line
        if not label1 == None:
            self.display.text(label1, 0, 0, font_color)
        
        # Determine if there is a value for the second label line
        if not label2 == None:
            self.display.text(label2, 0, 9, font_color)
        
        # Fill any assignments for the remaining lines
        if not text_line1 == None:
            self.display.text(text_line1, 0, 18, font_color)
        
        if not text_line2 == None:
            self.display.text(text_line2, 0, 27, font_color)

        if not text_line3 == None:
            self.display.text(text_line3, 0, 36, font_color)

        if not text_line4 == None:
            self.display.text(text_line4, 0, 45, font_color)

        if not text_line5 == None:
            self.display.text(text_line5, 0, 54, font_color)

        if show_immediately:
            self.display.show()

    def display_clear(self):
        self.display_text()

    def display_wifi_signal(self, avg_rssi=-90):  
        rssi_quality = connection.rssi_quality(avg_rssi)
        self.draw_wifi_radial(rssi_quality)       

        self.display_avg_rssi(avg_rssi)
        self.display.show()
    
    def draw_wifi_bars(self, rssi_quality):        
        font_color = self.color()
        
        if rssi_quality >= 1:
            self.display.fill_rect(85, 54, 6, 63, font_color)
        
        if rssi_quality >= 2:
            self.display.fill_rect(95, 50, 6, 63, font_color)
        
        if rssi_quality >= 3:
            self.display.fill_rect(105, 46, 6, 63, font_color)

        if rssi_quality >= 4:
            self.display.fill_rect(115, 42, 6, 63, font_color)

    def draw_wifi_radial(self, rssi_quality):
        font_color = self.color()
        base_y = 60
        base_x = 98

        if rssi_quality >= 1:
            self.display.fill_rect(base_x, base_y, 2, 2, font_color)
        
        if rssi_quality >= 2:
            self.display.line(base_x - 3, base_y - 2, base_x - 1, base_y - 3, font_color)
            self.display.line(base_x - 1, base_y - 3, base_x + 1, base_y - 3, font_color)
            self.display.line(base_x + 3, base_y - 2, base_x + 1, base_y - 3, font_color)

        if rssi_quality >= 3:
            self.display.line(base_x - 6, base_y - 5, base_x - 2, base_y - 7, font_color)
            self.display.line(base_x - 2, base_y - 7, base_x + 2, base_y - 7, font_color)
            self.display.line(base_x + 3, base_y - 7, base_x + 6, base_y - 5, font_color)

        if rssi_quality >= 4:
            self.display.line(base_x - 9, base_y - 8, base_x - 3, base_y - 11, font_color)
            self.display.line(base_x - 3, base_y - 11, base_x + 3, base_y - 11, font_color)
            self.display.line(base_x + 4, base_y - 11, base_x + 9, base_y - 8, font_color)

    def display_avg_rssi(self, avg_rssi=-90):        
        import bigfont

        rssi_text = str(avg_rssi)
        xval = 0
        yval = 48

        label_y = 30
        bigfont.text_large("RSSI", xval, label_y, self.display, self.color())
        bigfont.text_large(rssi_text, xval, yval, self.display, self.color())
        self.display.text("(avg)", 50, 38, 1)
        self.display.show()
