from machine import Pin
from time import sleep

led_builtin = Pin(2, Pin.OUT)
led_pin5 = Pin(5, Pin.OUT)
# blink the builtin LED
for x in range(10):
    led_builtin.value(0)
    sleep(0.5)
    led_builtin.value(1)
    sleep(0.5)

# Blink an external LED
for x in range(10):
    led_pin5.value(0)
    sleep(0.5)
    led_pin5.value(1)
    sleep(0.5)
# reset builtin LED
led_builtin.value(1)
# reset external LED
led_pin5.value(0)
