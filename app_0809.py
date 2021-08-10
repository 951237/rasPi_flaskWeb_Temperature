from flask import Flask, render_template
import neopixel
import adafruit_dht as dht
import board

app = Flask(__name__)
pixels = neopixel.NeoPixel(board.D18, 8) # led 객체 생성

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

@app.route('/')
def main():
    def read_txtfile():
        FILE_PATH = 'result_temp.txt'
        with open(FILE_PATH, 'r') as f:
            body = f.read().split(',')
        date_time = body[0]
        temperature = body[1]
        humidity = body[2]
        return date_time, temperature, humidity

    date_time, temperature, humidity = read_txtfile()
    templateData = {
        'date_time' : date_time,
        'temperature' : temperature,
        'humidity' : humidity,
    }
    return render_template('main.html', **templateData)

@app.route('/<pin>/<action>')
def action(pin, action):
    if pin == 'blue_led' and action == 'on':
       show_led('b') 
    if pin == 'blue_led' and action == 'off':
       show_led('w') 
    if pin == 'red_led' and action == 'on':
       show_led('r') 
    if pin == 'red_led' and action == 'off':
       show_led('w') 
    if pin == 'green_led' and action == 'on':
       show_led('g') 
    if pin == 'green_led' and action == 'off':
       show_led('w') 

if __name__ == "__main__":
    app.run(debug=True, port=80, host='0.0.0.0')
