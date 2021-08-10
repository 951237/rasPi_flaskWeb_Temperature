# 라이브러리 가져오기
import board
import adafruit_dht
import neopixel
import time

# led 센서 객체 생성
pixels = neopixel.NeoPixel(board.D18, 8)

def led_color(r, g, b):
    pixels[0] = (int(r), int(g), int(b))
    pixels[1] = (int(r), int(g), int(b))
    pixels[2] = (int(r), int(g), int(b))
    pixels[3] = (int(r), int(g), int(b))
    pixels[4] = (int(r), int(g), int(b))
    pixels[5] = (int(r), int(g), int(b))
    pixels[6] = (int(r), int(g), int(b))
    pixels[7] = (int(r), int(g), int(b))

# 5초동안 켜져있다가 꺼지기
def show_led(p):
    if p == 'r':
        for i in range(500):
            led_color(255, 0, 0)
            pixels.show
    elif p == 'g':
        for i in range(500):
            led_color(0, 255, 0)
            pixels.show
    elif p == 'b':
        for i in range(500):
            led_color(0, 0, 255)
            pixels.show
    elif p == 'w':
        for i in range(500):
            led_color(0, 0, 0)
            pixels.show

while True:
    val = input('값을 입력하세요.(r/g/b/w) : ')
    show_led(val)

    
    
