from gpiozero import LED
from time import sleep

led = LED(14)  # Adjust the pin number to match your setup

def turn_on():
    led.on()

def turn_off():
    led.off()
