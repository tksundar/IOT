# pushing the button will light the led
from machine import Pin

button_pin = Pin(21, Pin.OUT)
led_pin = Pin(5, Pin.OUT)

while True:
    led_pin.value(button_pin.value())
