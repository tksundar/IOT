import sys,time,network
from machine import Pin
from umqtt.robust import MQTTClient

def connect_to_network(wlan, ssid, password):
    wlan.active(True)
    if not wlan.isconnected():
        print('Connecting to network...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            print('.', end='')
            time.sleep(3)
        print()
        print('Connected:', wlan.isconnected())

    # get the interface's IP/netmask/gw/DNS addresses
    print("ip config router: " + str(wlan.ifconfig()))

def do_blink(led, off_value):
    for x in range(10):
        led.off()
        time.sleep(0.5)
        led.on()
        time.sleep(0.5)
    led.value(off_value)

def blink():
    led_builtin = Pin(2, Pin.OUT)
    led5 = Pin(5, Pin.OUT)
    do_blink(led_builtin, 1)
    do_blink(led5, 0)
    client.disconnect()
    sys.exit()

def on_message(topic, msg):
    command = msg.decode()
    if command == "BLINK":
        print("received message " + command)
        blink()

def subscribe(topic):
    while not done:
        client.subscribe(topic)
        time.sleep(3)

def connect_to_broker():
    if sta_if.isconnected():
        client.connect()
        print("subscribing to topic " + topic.decode())
        subscribe(topic)
    else:
        print("No network")

SSID = "WIFI_ID";
password = "PASSWORD"
sta_if = network.WLAN(network.STA_IF)
if sta_if.isconnected():
    sta_if.disconnect()
client_id = "ESP8266"
client = MQTTClient(client_id, "test.mosquitto.org", port=1883)
topic = 'led/command'.encode()
client.set_callback(on_message)
connect_to_network(sta_if, SSID, password)
connect_to_broker()
