from flask import Flask, render_template
import RPi.GPIO as GPIO
import neopixel
import adafruit_dht as dht
import board

app = Flask(__name__)
pixels = neopixel.NeoPixel(board.D18, 8) # led 객체 생성

# GPIO 설정값 기록하기

# GPIO setup 기록하기


# LED제어하기 
def led_color(r, g, b):
    pixels[0] = (int(r), int(g), int(b))
    pixels[1] = (int(r), int(g), int(b))
    pixels[2] = (int(r), int(g), int(b))
    pixels[3] = (int(r), int(g), int(b))
    pixels[4] = (int(r), int(g), int(b))
    pixels[5] = (int(r), int(g), int(b))
    pixels[6] = (int(r), int(g), int(b))
    pixels[7] = (int(r), int(g), int(b))
    pixels.show()

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/<pin>/<action>')
def action(pin, action):
    if pin == 'blue_led' and action == 'on':
        led_color(0, 0, 255)
    if pin == 'blue_led' and action == 'off':
        led_color(0, 0, 0)

    if pin == 'red_led' and action == 'on':
        led_color(255, 0, 0)
    if pin == 'red_led' and action == 'off':
        led_color(0, 0, 0)
    
    if pin == 'green_led' and action == 'on':
        led_color(0, 255, 0)
    if pin == 'green_led' and action == 'off':
        led_color(0, 0, 0)

    if pin == "dhtpin" and action == 'get':
        # 온습도 센서 객체 생성하기 
        dhtDevice = dht.DHT22(board.D4)
        
        temp = dhtDevice.temperature    # 온도
        humi = dhtDevice.humidity   # 습도 

        humi = '{0:0.1f}'.format(humi) 
        temp = '{0:0.1f}'.format(temp) 
        temperature = 'Temperature: ' + temp
        humidity = 'Humidity: ' + humi

    templateData = {
        'temperature' : temperature,
        'humidity' : humidity,
    }
    return render_template('main.html', **templateData)


if __name__ == "__main__":
    app.run(debug=True, port=80, host='0.0.0.0')