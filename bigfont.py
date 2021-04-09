# The large letters and numbers here are based on work done by nickpmulder's SSD1306big for larger fonts with SSD1306.
# Unfortunately, because nickpmulder's work was based on the RPi Pico, it doesn't look like his driver
# would work on the ESP32 due to memory constraints.  So I borrowed the the "fonts" laid out, 
# and put them as functions here. I made a few adjustments to better fit my preferences.
# The github for nickpmulder's project is https://github.com/nickpmulder/ssd1306big

xincrement = 12

def text_large(text, x, y, display):
    xval = 0
    for i in range(len(text)):
        if (text[i] == "a" or text[i] == "A"): A(xval, y, display)
        elif (text[i] == "b" or text[i] == "B"): B(xval, y, display)
        elif (text[i] == "c" or text[i] == "C"): C(xval, y, display)
        elif (text[i] == "d" or text[i] == "D"): D(xval, y, display)
        elif (text[i] == "e" or text[i] == "E"): E(xval, y, display)
        elif (text[i] == "f" or text[i] == "F"): F(xval, y, display)
        elif (text[i] == "g" or text[i] == "G"): G(xval, y, display)
        elif (text[i] == "h" or text[i] == "H"): H(xval, y, display)
        elif (text[i] == "i" or text[i] == "I"): I(xval, y, display)
        elif (text[i] == "j" or text[i] == "J"): J(xval, y, display)
        elif (text[i] == "k" or text[i] == "K"): K(xval, y, display)
        elif (text[i] == "l" or text[i] == "L"): L(xval, y, display)
        elif (text[i] == "m" or text[i] == "M"): M(xval, y, display)
        elif (text[i] == "n" or text[i] == "N"): N(xval, y, display)
        elif (text[i] == "o" or text[i] == "O"): O(xval, y, display)
        elif (text[i] == "p" or text[i] == "P"): P(xval, y, display)
        elif (text[i] == "q" or text[i] == "Q"): Q(xval, y, display)
        elif (text[i] == "r" or text[i] == "R"): R(xval, y, display)
        elif (text[i] == "s" or text[i] == "S"): S(xval, y, display)
        elif (text[i] == "t" or text[i] == "T"): T(xval, y, display)
        elif (text[i] == "u" or text[i] == "U"): U(xval, y, display)
        elif (text[i] == "v" or text[i] == "V"): V(xval, y, display)
        elif (text[i] == "w" or text[i] == "W"): W(xval, y, display)
        elif (text[i] == "x" or text[i] == "X"): X(xval, y, display)
        elif (text[i] == "y" or text[i] == "Y"): Y(xval, y, display)
        elif (text[i] == "z" or text[i] == "Z"): Z(xval, y, display)
        elif (text[i] == "."): period(xval, y, display)
        elif (text[i] == "-"): minus(xval, y, display)
        elif (text[i] == "="): equal(xval, y, display)
        elif (text[i] == ","): comma(xval, y, display)
        elif (text[i] == ":"): colon(xval, y, display)
        elif (text[i] == "/"): slash(xval, y, display)
        elif (text[i] == "?"): question(xval, y, display)
        elif (text[i] == "&"): amp(xval, y, display)
        elif (text[i] == "0"): zero(xval, y, display)
        elif (text[i] == "1"): one(xval, y, display)
        elif (text[i] == "2"): two(xval, y, display)
        elif (text[i] == "3"): three(xval, y, display)
        elif (text[i] == "4"): four(xval, y, display)
        elif (text[i] == "5"): five(xval, y, display)
        elif (text[i] == "6"): six(xval, y, display)
        elif (text[i] == "7"): seven(xval, y, display)
        elif (text[i] == "8"): eight(xval, y, display)
        elif (text[i] == "9"): nine(xval, y, display)

        xval += xincrement

#The Alphabet
def A(x, y, display):
    display.line((x)+1,(y)+15,(x)+5,(y)+1,1)
    display.line((x)+5,(y)+1,(x)+10,(y)+15,1)
    display.line((x)+3,(y)+11,(x)+8,(y)+11,1)
    
def B(x, y, display):
    display.line((x)+1,(y)+15,(x)+1,(y)+1,1)
    display.line((x)+1,(y)+1,(x)+6,(y)+1,1)
    display.line((x)+6,(y)+1,(x)+8,(y)+3,1)
    display.line((x)+8,(y)+3,(x)+8,(y)+4,1)
    display.line((x)+8,(y)+4,(x)+6,(y)+7,1)
    display.line((x)+5,(y)+7,(x)+1,(y)+7,1)
    display.line((x)+6,(y)+7,(x)+9,(y)+10,1)
    display.line((x)+9,(y)+10,(x)+9,(y)+12,1)
    display.line((x)+9,(y)+12,(x)+6,(y)+15,1)
    display.line((x)+6,(y)+15,(x)+1,(y)+15,1)

def C(x, y, display):
    display.line((x)+10,(y)+2,(x)+9,(y)+1,1)
    display.line((x)+9,(y)+1,(x)+4,(y)+1,1)
    display.line((x)+4,(y)+1,(x)+2,(y)+3,1)
    display.line((x)+2,(y)+3,(x)+1,(y)+7,1)
    display.line((x)+1,(y)+7,(x)+1,(y)+12,1)
    display.line((x)+1,(y)+12,(x)+4,(y)+15,1)
    display.line((x)+4,(y)+15,(x)+8,(y)+15,1)
    display.line((x)+8,(y)+15,(x)+10,(y)+13,1)

def D(x, y, display):
    display.line((x)+1,(y)+15,(x)+1,(y)+1,1)
    display.line((x)+1,(y)+1,(x)+6,(y)+1,1)
    display.line((x)+6,(y)+1,(x)+9,(y)+3,1)
    display.line((x)+9,(y)+3,(x)+9,(y)+12,1)
    display.line((x)+9,(y)+12,(x)+6,(y)+15,1)
    display.line((x)+6,(y)+15,(x)+1,(y)+15,1)
    
    
def E(x, y, display):
    display.line((x)+1,(y)+15,(x)+1,(y)+1,1)
    display.line((x)+1,(y)+1,(x)+9,(y)+1,1)
    display.line((x)+1,(y)+7,(x)+7,(y)+7,1)
    display.line((x)+1,(y)+15,(x)+9,(y)+15,1)   
    
def F(x, y, display):
    display.line((x)+1,(y)+15,(x)+1,(y)+1,1)
    display.line((x)+1,(y)+1,(x)+9,(y)+1,1)
    display.line((x)+1,(y)+7,(x)+6,(y)+7,1)    
    
def G(x, y, display):
    display.line((x)+9,(y)+2,(x)+8,(y)+1,1)
    display.line((x)+8,(y)+1,(x)+4,(y)+1,1)
    display.line((x)+4,(y)+1,(x)+2,(y)+3,1)
    display.line((x)+2,(y)+3,(x)+1,(y)+7,1)
    display.line((x)+1,(y)+7,(x)+1,(y)+12,1)
    display.line((x)+1,(y)+12,(x)+4,(y)+15,1)
    display.line((x)+4,(y)+15,(x)+8,(y)+15,1)
    display.line((x)+8,(y)+15,(x)+10,(y)+13,1)
    display.line((x)+10,(y)+13,(x)+10,(y)+9,1)
    display.line((x)+10,(y)+9,(x)+6,(y)+9,1)

def H(x, y, display):
    display.line((x)+1,(y)+15,(x)+1,(y)+1,1)
    display.line((x)+1,(y)+7,(x)+9,(y)+7,1)
    display.line((x)+9,(y)+15,(x)+9,(y)+1,1)    

def I(x, y, display):
    display.line((x)+1,(y)+1,(x)+9,(y)+1,1)
    display.line((x)+1,(y)+15,(x)+9,(y)+15,1)
    display.line((x)+5,(y)+15,(x)+5,(y)+1,1)    

def J(x, y, display):
    display.line((x)+9,(y)+1,(x)+9,(y)+10,1)
    display.line((x)+9,(y)+10,(x)+7,(y)+15,1)
    display.line((x)+7,(y)+15,(x)+3,(y)+15,1)
    display.line((x)+3,(y)+15,(x)+1,(y)+10,1)    
    
def K(x, y, display):
    display.line((x)+1,(y)+15,(x)+1,(y)+1,1)
    display.line((x)+1,(y)+9,(x)+8,(y)+1,1)
    display.line((x)+4,(y)+7,(x)+9,(y)+15,1)    

def L(x, y, display):
    display.line((x)+1,(y)+15,(x)+1,(y)+1,1)
    display.line((x)+1,(y)+15,(x)+9,(y)+15,1)    
    
def M(x, y, display):
    display.line((x)+1,(y)+15,(x)+1,(y)+1,1)
    display.line((x)+1,(y)+1,(x)+5,(y)+7,1)
    display.line((x)+9,(y)+1,(x)+5,(y)+7,1)
    display.line((x)+9,(y)+15,(x)+9,(y)+1,1)    

def N(x, y, display):
    display.line((x)+1,(y)+15,(x)+1,(y)+1,1)
    display.line((x)+1,(y)+1,(x)+9,(y)+15,1)
    display.line((x)+9,(y)+15,(x)+9,(y)+1,1)    

def O(x, y, display):
    display.line((x)+10,(y)+5,(x)+8,(y)+1,1)
    display.line((x)+8,(y)+1,(x)+4,(y)+1,1)
    display.line((x)+4,(y)+1,(x)+2,(y)+3,1)
    display.line((x)+2,(y)+3,(x)+1,(y)+7,1)
    display.line((x)+1,(y)+7,(x)+1,(y)+12,1)
    display.line((x)+1,(y)+12,(x)+4,(y)+15,1)
    display.line((x)+4,(y)+15,(x)+7,(y)+15,1)
    display.line((x)+7,(y)+15,(x)+10,(y)+12,1)
    display.line((x)+10,(y)+12,(x)+10,(y)+5,1)

def P(x, y, display):
    display.line((x)+1,(y)+15,(x)+1,(y)+1,1)
    display.line((x)+1,(y)+1,(x)+7,(y)+1,1)
    display.line((x)+7,(y)+1,(x)+9,(y)+4,1)
    display.line((x)+9,(y)+4,(x)+9,(y)+6,1)
    display.line((x)+9,(y)+6, (x)+6,(y)+9,1)
    display.line((x)+5,(y)+9,(x)+1,(y)+9,1)

def Q(x, y, display):
    display.line((x)+10,(y)+5,(x)+8,(y)+1,1)
    display.line((x)+8,(y)+1,(x)+4,(y)+1,1)
    display.line((x)+4,(y)+1,(x)+2,(y)+3,1)
    display.line((x)+2,(y)+3,(x)+1,(y)+7,1)
    display.line((x)+1,(y)+7,(x)+1,(y)+12,1)
    display.line((x)+1,(y)+12,(x)+4,(y)+15,1)
    display.line((x)+4,(y)+15,(x)+7,(y)+15,1)
    display.line((x)+7,(y)+15,(x)+10,(y)+12,1)
    display.line((x)+10,(y)+12,(x)+10,(y)+5,1)
    display.line((x)+6,(y)+10,(x)+10,(y)+15,1)

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

def T(x, y, display):
    display.line((x)+5,(y)+15,(x)+5,(y)+1,1)
    display.line((x)+1,(y)+1,(x)+9,(y)+1,1)    
    
def U(x, y, display):
    display.line((x)+1,(y)+1,(x)+1,(y)+13,1)
    display.line((x)+1,(y)+13,(x)+3,(y)+15,1)
    display.line((x)+3,(y)+15,(x)+7,(y)+15,1)
    display.line((x)+7,(y)+15,(x)+9,(y)+13,1)
    display.line((x)+9,(y)+13,(x)+9,(y)+1,1)    

def V(x, y, display):
    display.line((x)+1,(y)+1,(x)+5,(y)+15,1)
    display.line((x)+5,(y)+15,(x)+9,(y)+1,1)    

def W(x, y, display):
    display.line((x)+1,(y)+1,(x)+3,(y)+15,1)
    display.line((x)+3,(y)+15,(x)+5,(y)+8,1)
    display.line((x)+5,(y)+8,(x)+8,(y)+15,1)
    display.line((x)+8,(y)+15,(x)+10,(y)+1,1)
    
def X(x, y, display):
    display.line((x)+1,(y)+1,(x)+9,(y)+15,1)
    display.line((x)+9,(y)+1,(x)+1,(y)+15,1)
    
def Y(x, y, display):
    display.line((x)+5,(y)+15,(x)+5,(y)+7,1)
    display.line((x)+5,(y)+7,(x)+1,(y)+1,1)
    display.line((x)+5,(y)+7,(x)+10,(y)+1,1)

def Z(x, y, display):
    display.line((x)+1,(y)+1,(x)+9,(y)+1,1)
    display.line((x)+1,(y)+15,(x)+9,(y)+1,1)
    display.line((x)+1,(y)+15,(x)+9,(y)+15,1)

def period(x, y, display):
    display.line((x)+1,(y)+14,(x)+2,(y)+14,1)
    display.line((x)+1,(y)+15,(x)+2,(y)+15,1)

def minus(x, y, display):
    display.line((x)+2,(y)+8,(x)+8,(y)+8,1)
           
def equal(x, y, display):
    display.line((x)+2,(y)+6,(x)+8,(y)+6,1)
    display.line((x)+2,(y)+9,(x)+8,(y)+9,1)

def comma(x, y, display):
    display.line((x)+1,(y)+13,(x)+1,(y)+14,1)
    display.line((x)+2,(y)+13,(x)+2,(y)+17,1)
    display.line((x)+1,(y)+17,(x)+2,(y)+17,1)

def colon(x, y, display):
    display.line((x)+1,(y)+14,(x)+2,(y)+14,1)
    display.line((x)+1,(y)+15,(x)+2,(y)+15,1)
    display.line((x)+1,(y)+6,(x)+2,(y)+6,1)
    display.line((x)+1,(y)+5,(x)+2,(y)+5,1)

def slash(x, y, display):
    display.line((x)+9,(y)+1,(x)+1,(y)+15,1)
        
def question(x, y, display):
    display.line((x)+5,(y)+14,(x)+6,(y)+14,1)
    display.line((x)+5,(y)+15,(x)+6,(y)+15,1)
    display.line((x)+5,(y)+10,(x)+5,(y)+8,1)
    display.line((x)+5,(y)+8,(x)+8,(y)+6,1)
    display.line((x)+8,(y)+6,(x)+9,(y)+2,1)
    display.line((x)+8,(y)+1,(x)+4,(y)+1,1)

def amp(x, y, display):
    #&
    display.line((x)+4,(y)+7,(x)+2,(y)+5,1)
    display.line((x)+2,(y)+5,(x)+2,(y)+3,1)
    display.line((x)+2,(y)+3,(x)+3,(y)+2,1)
    display.line((x)+3,(y)+2,(x)+4,(y)+1,1)
    display.line((x)+4,(y)+1,(x)+6,(y)+1,1)
    display.line((x)+6,(y)+1,(x)+7,(y)+2,1)
    display.line((x)+7,(y)+2,(x)+8,(y)+3,1)
    display.line((x)+8,(y)+3,(x)+8,(y)+4,1)
    display.line((x)+8,(y)+4,(x)+6,(y)+6,1)
    display.line((x)+6,(y)+6,(x)+1,(y)+10,1)
    display.line((x)+1,(y)+10,(x)+1,(y)+13,1)
    display.line((x)+1,(y)+13,(x)+3,(y)+15,1)
    display.line((x)+3,(y)+15,(x)+6,(y)+15,1)
    display.line((x)+6,(y)+15,(x)+9,(y)+9,1)
    display.line((x)+4,(y)+8,(x)+10,(y)+15,1)

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
