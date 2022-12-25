# This file connects to wifi, creates an mqtt client and connects to the test mosquitto broker
# # It then waits for a message to appear on topic led/command.
# # On receipt of the command on, it turns on the leds and on receipt of off command, it turns
# off the leds

import umqtt
import machine
from machine import Pin
import ubinascii
import network
import time

# ESP8266 ESP-12 modules have blue, active-low LED on GPIO2, replace
# with something else if needed.
led_builtin = Pin(2, Pin.OUT, value=0)
led_gpio5 = Pin(5, Pin.OUT, value=0)

# Default MQTT server to connect to
SERVER = "test.mosquitto.org"
CLIENT_ID = ubinascii.hexlify(machine.unique_id())
TOPIC = b"LED"
SSID = "<SSID>"
PASSWORD = "PAS$$WORD"


def connect_to_network(wlan):
    wlan.active(True)
    print('Connecting to network...')
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        print('.', end='')
        time.sleep(3)
    print()
    print('Connected:', wlan.isconnected())

    # get the interface's IP/netmask/gw/DNS addresses
    print("ip config router: " + str(wlan.ifconfig()))


def sub_cb(topic, msg):
    print((topic, msg))
    if msg == b"on":
        led_builtin.value(0)
        led_gpio5.value(1)
    elif msg == b"off":
        led_builtin.value(1)
        led_gpio5.value(0)


def main(server=SERVER):
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        connect_to_network(sta_if)
    c = umqtt.MQTTClient(CLIENT_ID, server)
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


main("test.mosquitto.org")
