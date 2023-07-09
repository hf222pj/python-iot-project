import network
import uasyncio as asyncio

class WiFi:
    def __init__(self, ssid, password):
        self.ssid = ssid
        self.password = password
        self.wlan = network.WLAN(network.STA_IF)
        self.loop = asyncio.get_event_loop()
        self.loop.create_task(self.connect())

    async def connect(self):
        if not self.wlan.isconnected():
            print("Connecting to WiFi...")
            self.wlan.active(True)
            self.wlan.connect(self.ssid, self.password)
            while not self.wlan.isconnected():
                await asyncio.sleep_ms(100)
            print("WiFi connected!")
            print(self.wlan.ifconfig())
        else:
            print("Already connected to WiFi.")

    def reconnect(self):
        self.wlan.active(False)
        self.loop.create_task(self.connect())

    def is_connected(self):
        return self.wlan.isconnected()