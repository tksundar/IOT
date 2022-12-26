import math
import time

import machine

# create a PWM object
led_builtin = machine.PWM(machine.Pin(2), freq=1000)
led_pin5 = machine.PWM(machine.Pin(5), freq=1000)
led_builtin.duty_ns(0)
led_pin5.duty_ns(0)


# define a function to light the led with varying powersupply
def pulse(led, t):
    for i in range(10):
        on_ratio = math.sin(i / 10 * math.pi) * 500 + 500

        if i == 19:
            print(on_ratio*1000,end="")
        else:
            print(on_ratio, end="|")
        led.duty_ns(int(on_ratio*1000))
        time.sleep_ms(t)


for i in range(10):
    pulse(led_builtin, 50)

for i in range(10):
    pulse(led_pin5, 100)

led_builtin.duty_ns(0)
led_pin5.duty_ns(0)
