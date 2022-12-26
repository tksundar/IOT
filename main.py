import Blinker
from machine import Pin

if __name__ == "__main__":
    pin5 = Pin(5, Pin.OUT)
    pin5.off()
    Blinker.blink()

