from machine import Pin
from time import sleep

led_builtin = Pin(2, Pin.OUT)
led_pin5 = Pin(5, Pin.OUT)


def blink(led):
    # blink the builtin LED
    for x in range(10):
        led.on()
        sleep(0.5)
        led.off()
        sleep(0.5)


blink(led_builtin)
blink(led_pin5)
