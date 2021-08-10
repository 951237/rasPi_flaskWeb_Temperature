import board
import time
import adafruit_dht
from datetime import datetime

dhtDevice = adafruit_dht.DHT22(board.D4)
# k = 0
while True:
    # todo : 날짜 형식으로 변환하기
    today = datetime.now()
    date_time = today.strftime("%Y-%m-%d %H:%M:%S")
    try:
        temperature = dhtDevice.temperature
        humidity = dhtDevice.humidity
        result = "temp: {:.1f},Humidity: {}%".format(temperature, humidity)
        # 결과값 파일에 기록하기
        with open("result_temp.txt","w") as f:
            f.write(f'{date_time},{result}\n')
        k += 1
        print(f'{date_time} 기록!')
        time.sleep(5)
    except RuntimeError as error:
        print(error.args[0])
