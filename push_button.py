# pushing the button will light the led
from machine import Pin

button_pin = Pin(21, Pin.OUT)
led_pin = Pin(5, Pin.OUT)

print('starting loop')
def loop():
    while True:
        led_pin.value(button_pin.value())

loop()
