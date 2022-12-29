# This file connects to wifi, creates an mqtt client and connects to the test mosquitto broker
# # It then waits for a message to appear on topic led/command.
# # On receipt of the command on, it turns on the leds and on receipt of off command, it turns
# off the leds

from umqtt.simple import MQTTClient
import machine
from machine import Pin
import ubinascii
import network
from time import sleep

# ESP8266 ESP-12 modules have blue, active-low LED on GPIO2, replace
# with something else if needed.
led_builtin = Pin(2, Pin.OUT)
led_gpio5 = Pin(5, Pin.OUT)
led_builtin.off()
led_gpio5.off()

# Default MQTT server to connect to
SERVER = "test.mosquitto.org"
CLIENT_ID = ubinascii.hexlify(machine.unique_id())
TOPIC = b"LED"


def get_credentials():
    f = open('credentials.txt')
    return f.read().split('|')


def connect_to_network(wlan):
    wlan.active(True)
    print('Connecting to network...')
    # may be enter this at the time of program execution?
    credentials = get_credentials()
    ssid = credentials[0]
    pwd = credentials[1]
    wlan.connect(ssid, pwd)
    while not wlan.isconnected():
        print('.', end='')
        sleep(3)

    # get the interface's IP/netmask/gw/DNS addresses
    print("ip config router: " + str(wlan.ifconfig()))


def blink(led):
    for i in range(10):
        led.on()
        sleep(0.5)
        led.off()
        sleep(0.5)


def sub_cb(topic, msg):
    print((topic, msg))
    if msg == b"blink":
        blink(led_builtin)
        blink(led_gpio5)
    elif msg == b"on":
        led_builtin.on()
        led_gpio5.on()
    elif msg == b"off":
        led_builtin.off()
        led_gpio5.off()


def main(server=SERVER):
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        connect_to_network(sta_if)
    c = MQTTClient(CLIENT_ID, server)
    # Subscribed messages will be delivered to this callback
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(TOPIC)
    print("Connected to %s, subscribed to %s topic" % (server, TOPIC))

    try:
        while 1:
            c.wait_msg()
    finally:
        c.disconnect()


main()
