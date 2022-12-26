from machine import Pin
from time import sleep


def blink():
    led_builtin = Pin(2, Pin.OUT)

    # blink the builtin LED
    for x in range(10):
        led_builtin.on()
        sleep(0.5)
        led_builtin.off()
        sleep(0.5)

# blink()
