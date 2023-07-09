from machine import ADC, Pin
from dht import DHT11

def initialize_pins():
    leds = [
        Pin(18, Pin.OUT),
        Pin(19, Pin.OUT),
        Pin(20, Pin.OUT),
        Pin(21, Pin.OUT),
    ]

    pin_led = Pin("LED", Pin.OUT)
    pin_red_1 = Pin(22, Pin.OUT)
    pin_button = Pin(15, Pin.IN, Pin.PULL_UP)
    pin_data = Pin(16, Pin.OUT, Pin.PULL_DOWN)
    data = DHT11(pin_data)

    leds[0].value(0)
    leds[1].value(0)
    leds[2].value(0)
    leds[3].value(0)
    pin_red_1.value(0)

    return pin_led, pin_red_1, pin_button, data, leds
