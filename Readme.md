This repository is created to store my working experiments with various IOT development boards like 
ESP 8266, ESP32 , Raspberry PI etc

**ESP32 examples**
<p>
1. Blinker.py<br>
   This program turns the on board led(GPIO 2) and an external LED(GPIO 5) on and off 10 times
<p>
2. fading_led.py<br>
   This program fades the on board and external led with a pwm signal that varies its strength modulated by a sine wave
<p>
3. push_button.py<br>
   This prgram turns on the external led every time the push button is pressed
<p>
4.  mqtt_client<br>
    This file connects to wifi, creates an mqtt client and connects to the test mosquitto broker
    It then waits for a message to appear on topic led/command.
    On receipt of the command on, it turns on the leds and on receipt of off command, it turns
    off the leds

