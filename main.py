
import uasyncio as asyncio
from umqtt.simple import MQTTClient
import json
import utime
import pins
from server import Server
from wifi import WiFi
from machine import Timer

# Define the main variables
WLAN_SSID = "Tele2_#######"
WLAN_PASS = "########"

MQTT_BROKER = "192.168.0.22"
MQTT_PORT = 1883

mqtt_ready = False
alert = False
button_pressed = False

# Define servers
SERVERS = [
    Server("192.168.1.1", "none", 0),
    Server("192.168.1.2", "none", 1),
    Server("192.168.1.3", "none", 2),
    Server("192.168.1.4", "none", 3),
]

# Initialize pins
pin_led, pin_red_1, pin_button, data, leds = pins.initialize_pins()

# Initialise wifi
wifi = WiFi(WLAN_SSID, WLAN_PASS)


# Initialize button action
def button_action(t):
    global button_pressed, pin_button, alert
    if pin_button.value() == 0:
        if not button_pressed:
            button_pressed = True
            for server in SERVERS:
                if server.status == "error":
                    print(f"Publish restart signal")
                    mqtt.publish("servers", json.dumps({"command": "restart", "server": server.name}))
            alert = False
    else:
        button_pressed = False


button_timer = Timer()
button_timer.init(period=200, mode=Timer.PERIODIC, callback=button_action)

# Create MQTT client
mqtt = MQTTClient("iot", MQTT_BROKER, port=MQTT_PORT, user=None, password=None, keepalive=300, ssl=False, ssl_params={})


def mqtt_sub_cb(topic, msg):
    global SERVERS, alert
    print("Topic: ", topic.decode('utf-8'))
    print("Received message: ", msg.decode('utf-8'))

    if topic.decode('utf-8') == "server":
        try:
            message = json.loads(msg.decode('utf-8'))
            for server in SERVERS:
                if server.name == message["server"]:
                    if message["status"] == 'error':
                        if server.status != 'error':
                            alert = True
                    server.set_status(message["status"])

        except Exception as e:
            print(e)
            return


def mqtt_connect_and_subscribe():
    global mqtt_ready
    # Connect to MQTT broker
    mqtt.set_callback(mqtt_sub_cb)
    mqtt.connect()
    mqtt.subscribe('server')
    mqtt_ready = True



def mqtt_send_temperature(t):
    global data
    try:
        temperature = data.temperature
        humidity = data.humidity
        print("Publishing: Temperature: {}°C Humidity: {:.0f}% ".format(temperature, humidity))
        mqtt.publish("temperature", json.dumps({"temperature": temperature, "humidity": humidity}))
    except:
        pass


temperature_timer = Timer()
temperature_timer.init(period=60000, mode=Timer.PERIODIC, callback=mqtt_send_temperature)

# Network connection and mqtt connection
async def network():
    global mqtt_ready
    while True:
        if not wifi.is_connected():
            mqtt_ready = False
            print("WiFi connection lost. Reconnecting...")
            wifi.reconnect()
            await asyncio.sleep(5)
        else:
            try:
                if not mqtt_ready:
                    # Connect to MQTT broker
                    mqtt_connect_and_subscribe()
            except Exception as e:
                print(e)

        await asyncio.sleep(0.5)  # Delay between checks

# Blinker Jobber
async def blinker():
    global pins, alert
    while True:
        #Turning leds on
        for server in SERVERS:
            if server.status != "none":
                leds[server.led].value(1)
        pin_led.on()
        if alert:
            pin_red_1.value(1)

        await asyncio.sleep(.6)

        #Turning leds off
        has_error = False
        for server in SERVERS:
            pin_red_1.value(0)
            if server.status == 'error':
                has_error = True
                leds[server.led].value(0)
        if not wifi.is_connected():
            pin_led.off()
        if not has_error:
            alert = False
        await asyncio.sleep(.6)

async def mttq_listener():
    global mqtt_ready
    while True:
        if mqtt_ready:
            try:
                mqtt.check_msg()
            except:
                pass
        await asyncio.sleep(0.3)  # Delay between checks

loop = asyncio.get_event_loop()
loop.create_task(network())
loop.create_task(blinker())
loop.create_task(mttq_listener())
loop.run_forever()


