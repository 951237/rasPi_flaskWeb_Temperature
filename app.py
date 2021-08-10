from flask import Flask, render_template
import board
import adafruit_dht
import datetime
import time

app = Flask(__name__)

# 온습도 센서 결과값 리턴
def check_temp():
    dhtDevice = adafruit_dht.DHT22(board.D4)
    
    result = []
    for i in range(10):
        try:
            # Print the values to the serial port
            temperature_c = dhtDevice.temperature
            temperature_f = temperature_c * (9 / 5) + 32
            humidity = dhtDevice.humidity
            result_temp= "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                    temperature_f, temperature_c, humidity )
            result.append(result_temp)
            time.sleep(0.5)

        except RuntimeError as error:
            bot.send_message(message.chat.id, error.args[0])
            # detDevice.exit()
    return result

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
def hello():
    result = check_temp()
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')

