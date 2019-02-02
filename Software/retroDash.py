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

def printd(text):
    image = Image.new('1', (disp.width, disp.height));
    font = ImageFont.load_default()
    draw = ImageDraw.Draw(image)
    draw.text((0,0),text, font=font, fill=255)
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
printd("IP: %s" % (getOwnIp()))
