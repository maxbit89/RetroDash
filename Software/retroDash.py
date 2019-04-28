#!/bin/python3
import time
import math
import socket

#init display:
import SSD1306
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

disp=SSD1306.SSD1306_128_32(rst=24) #TODO: remove RST is not used on HW
disp.begin()
disp.clear()
disp.display()

MENUE_NETWORK = 0
MENUE_RADIO   = 1
MENUE_BLUETOOTH_MAIN = 2
MENUE_BLUETOOTH_PAIR = 3

menue_selection = MENUE_RADIO

def printd(text, pos=(0,0)):
    image = Image.new('1', (disp.width, disp.height));
    font = ImageFont.load_default()
    draw = ImageDraw.Draw(image)
    draw.text(pos,text, font=font, fill=255)
    disp.image(image)
    disp.display()

def getOwnIp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

while 1:
    if menue_selection ==  MENUE_NETWORK:
        disp.clear()
        printd("IP: %s" % (getOwnIp()))
    elif menue_selection == MENUE_RADIO:
        disp.clear()
        printd("Radio: %3.2f MHz" % (100.2))
    elif menue_selection == MENUE_BLUETOOTH_MAIN:
        disp.clear()
        printd("Bluetooth")
    elif menue_selection == MENUE_BLUETOOTH_PAIR:
        disp.clear()
        printd("Bluetooth Pairing...")
    time.sleep(0.2)
