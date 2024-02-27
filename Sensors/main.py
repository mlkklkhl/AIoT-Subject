# Board: Cucumber RIS ESP32-S2
# Firmware: ESP32_GENERIC_S2-20231005-v1.21.0

from machine import Pin, ADC, reset, RTC
import time
import network
import ufirebase as firebase
import ntptime

pir = ADC(Pin(3))
pir.atten(ADC.ATTN_11DB)

Light = ADC(Pin(4))
Light.atten(ADC.ATTN_11DB)

Mic = ADC(Pin(5))
Mic.atten(ADC.ATTN_11DB)

global pir_value
global converted_pir_value
global light_value
global converted_light_value
global mic_value
global converted_mic_value

# config
WIFIssid = "Engineering IOT"
WIFIpsw = "coeai123"

sensorID = 'Test'

URL = 'https://aiot-405605-default-rtdb.asia-southeast1.firebasedatabase.app/'

def connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...', WIFIssid)
        sta_if.active(True)
        sta_if.connect(WIFIssid, WIFIpsw)
        count = 0
        while not sta_if.isconnected():
             if(count > 60):
               print('Cannot connect to network...')
               time.sleep(180)
               reset()
             else: 
               print('.', end = '')
               time.sleep(1)
               count = count + 1
               pass
    print()
    print('network config: {}'.format(sta_if.ifconfig()))

def set_time():
    ntptime.settime()
    tm = time.localtime()
    tm = tm[0:3] + (0,) + tm[3:6] + (0,)
    RTC().datetime(tm)
    print('current time: {}'.format(time.localtime()))

def read_motion_sensor():
    global pir_value 
    pir_value = 0
    global converted_pir_value

    for i in range(1, 1000):
        pir_value += pir.read()
    
    pir_value = pir_value / 1000

    print("[PIR] Raw Value: {}".format(pir_value), end="")
    if pir_value > 1000:
        converted_pir_value = 1
        print("   - Ah Motion Detected")
    else:
        converted_pir_value = 0
        print("   - No Motion Detected")
    return pir_value

def read_light_sensor():
    global light_value
    global converted_light_value
    light_value = Light.read()
    print("Light Raw Value: {}".format(light_value), end="")
    percent_of_max = (((light_value - 8191)* -1) / 2) / 4095
    converted_light_value = percent_of_max * 100
    print(" - {}%".format(converted_light_value))
    return light_value
    
def convert_to_dB(sensor_value):
    percent_of_max = (sensor_value / 2) / 4095 
    dB = (percent_of_max * 4) + 48
    return dB

def read_mic_sensor():
    global mic_value
    mic_value = 0
    global converted_mic_value

    # mic_value = Mic.read()

    for i in range(1, 1000):
        mic_value += Mic.read()
    
    mic_value = mic_value / 1000

    print("[Mic] Raw Value: {}".format(mic_value), end="")
    converted_mic_value = convert_to_dB(mic_value)
    print("  - {} dB".format(converted_mic_value))

    return mic_value
    
try:

    label = 'human - light'
    print('starting...', label)

    connect()
    set_time()

    time.sleep(2)

    rtc = RTC()
    utc_shift = 7
    (year, month, day, weekday, hours, minutes, seconds, subseconds) = rtc.datetime()
    rtc.init((year, month, day, weekday, hours + utc_shift, minutes, seconds, subseconds))

    firebase.setURL(URL)

    while True:

        t = rtc.datetime()
        now = '{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}'.format(t[0], t[1], t[2], t[4], t[5], t[6])

        pir_value = read_motion_sensor()
        light_value = read_light_sensor()
        mic_value = read_mic_sensor()

        message = {
            "Timestamp": now,
            "PIR": pir_value,
            "Light": light_value,
            "Mic": mic_value,
            "Label": label
        }

        print('message: ', message)

        time.sleep(0.5)

        try:
            # Publish to Firebase Realtime Database
            path = "TestRoom/" + sensorID + "/" + now +  "/"
            firebase.put(path, message, bg=0)
            time.sleep(0.5)

        except Exception as e:               
            print('Cannot Publish to Google Cloud ...', e)
            time.sleep(30)
            reset()

        time.sleep(0.5)

except Exception as e:
    print("An error occurred: {}".format(e))
    time.sleep(5)
    reset()