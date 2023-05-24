# Complete project details at https://RandomNerdTutorials.com

import machine, onewire, ds18x20, time
import urequests
import ujson

def make_request(temperature):
    url = 'http://192.168.1.151:8080'
    headers = {'Content-Type': 'application/json'}
    data = {'name': 'NAVE_1_MONTE', 'data': temperature}
    response = urequests.post(url, headers=headers, data=ujson.dumps(data))
    print('HTTP status code:', response.status_code)
    print('Response text:', response.text)
    
ds_pin = machine.Pin(4)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

roms = ds_sensor.scan()
print('Found DS devices : ', roms)

while True:
    ds_sensor.convert_temp()
    time.sleep_ms(750)

    for rom in roms:
        temperature = ds_sensor.read_temp(rom)
        make_request(temperature)
        print(temperature)

    
    time.sleep(5)
