import machine
from machine import Pin
import time, math

# create a PWM object
led_builtin = machine.PWM(machine.Pin(2), freq=1000)
led_pin5 = machine.PWM(machine.Pin(5), freq=1000)

# definea function to light the led with varying powersupply
def pulse(led, t):
    for i in range(20):
        on_ratio = math.sin(i / 10 * math.pi) * 500 + 500
        if (i == 19):
            print(on_ratio)
        else:
            print(on_ratio, end="|")
        led.duty(int(on_ratio))
        time.sleep_ms(t)

    led.duty(int(1500))
for i in range(10):
    pulse(led_builtin, 50)

for i in range(10):
    pulse(led_pin5, 50)
# Turn off the external led. set duty cycle to 0
led_pin5.duty(0)

