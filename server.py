from machine import ADC, Pin
from dht import DHT11

class Server:
    def __init__(self, name, status, led):
        self.name = name
        self.status = status
        self.led = led

    def set_status(self, status):
        self.status = status