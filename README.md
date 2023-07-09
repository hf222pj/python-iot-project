
*Project by Henry Fisher, hf222pj.* 

Handy control panel for a server-room. This paper details an IoT project that uses market-available microcontrollers to develop a control panel for server rooms. Assembly and setup time 2-3 hour

[TOC]


## Abstract

This paper delineates an innovative IoT-based project aimed at developing a physical control panel for server rooms using commercially available microcontrollers. The meticulously designed hardware setup not only provides a real-time overview of the health status of each individual server but also collects and analyzes environmental data from the server room. It further includes a feature to manage servers via transmitted commands. The project encompasses detailed instructions for both hardware assembly and software development, offering a comprehensive guide for implementation.

## Objective

Monitoring server health within server rooms is of paramount importance due to a variety of reasons, most crucially to maintain optimal system performance and to prevent data loss or service interruptions. Servers operate best in controlled environmental conditions. Factors such as temperature and humidity, if not monitored and maintained within specific thresholds, can lead to hardware malfunction or failure. Elevated temperature can cause overheating, reducing server lifespan, while high humidity levels can lead to condensation, potentially causing short circuits and other hardware damages. Conversely, too low humidity can increase static electricity, posing another risk to server health. Therefore, simultaneous monitoring of server health and environmental conditions like temperature and humidity ensures the stable, efficient, and sustainable operation of server rooms, ultimately safeguarding an organization's vital data assets and uptime.

Homemade server rooms, often set up by individuals or small businesses to save costs, are indeed more susceptible to various risks due to the absence of sophisticated monitoring systems often found in professionally managed data centers. One of the most severe risks is overheating, which can potentially lead to disastrous outcomes, such as fires. As servers continuously work, they generate substantial heat, which in the absence of a dedicated cooling system, can quickly lead to overheating. This not only jeopardizes the server's performance and lifespan but also poses a serious fire hazard, especially in environments where the heat can't disperse efficiently. Moreover, without advanced monitoring systems in place, the early signs of overheating may go unnoticed until the situation escalates to a critical level. Hence, the risks associated with homemade server rooms, especially those lacking proper cooling and monitoring systems, are serious and must be mitigated with diligent attention to equipment setup, routine maintenance, and environmental control.

The primary objective of this project is to address the existing deficit of monitoring and control systems specifically designed for homemade server rooms. Recognizing the heightened vulnerability of these setups, our solution offers a cost-effective and efficient means to improve server management and environmental monitoring. The proposed system leverages market-available microcontrollers to deliver a comprehensive yet affordable tool, enabling users to monitor server health and control environmental parameters in real time. This not only enhances server performance and longevity but also mitigates potential risks such as overheating and humidity-related issues, ultimately contributing to the overall safety and reliability of homemade server rooms.


### Material

As a foundation for this project, we utilized the "Start Kit – Applied IoT" from Linnaeus University (2023), costing 399.00 SEK. This kit provided a basic framework and essential components to kickstart our IoT endeavor. To further enhance our system's capability and facilitate a more interactive user experience, we acquired an additional button controller. 


| Image                                                                                       	| Product              	|   Qt 	| Description                                                                                                                                                                                                                                      	| Suplier    	| Price                 	|
|---------------------------------------------------------------------------------------------	|----------------------	|----	|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|------------	|-----------------------	|
| ![PicoWH!](https://www.electrokit.com/uploads/productimage/41019/PICO-WH-HERO-1024x768.jpg) 	| Raspberry Pi Pico WH 	| 1  	| Raspberry Pi Pico W adds on-board single-band 2.4GHz wireless interfaces (802.11n) using the Infineon CYW43439 while retaining the Pico form factor.                          	| Elektrokit 	| included into 399-kit 	|
| ![Breadboard!](https://www.electrokit.com/uploads/productimage/10160/10160840.jpg)          	| Breadboard 840       	| 1  	| 840 Pin, ABS (Acrylonitrile Butadiene Styrene), 8.5mm, 8.5mm x 66mm                                                                                                                                                                              	| Elektrokit 	| included into 399-kit 	|
| ![DHT11!](https://www.electrokit.com/uploads/productimage/41015/41015728-1-1024x768.jpg)    	| DHT11                	| 1  	| Digital temperature and humidity sensor. Module with a DHT11 digital temperature- and humidity sensor.   	| Elektrokit 	| included into 399-kit 	|
| ![Jumpers!](https://www.electrokit.com/uploads/productimage/41012/41012684-1024x804.jpg)    	| Jumpers wires        	| 12 	| Jumper wires 20-pin 30cm male/male. 20-pin jumper wire with connectors in both ends for use with breadboards and headers.                                                                                                                        	| Elektrokit 	| included into 399-kit 	|
| ![LoPy!](https://www.electrokit.com/uploads/productimage/40300/5mm-r%C3%B6d-diffus.jpg)     	| LED 5mm red          	| 1  	| diffus 1500mcd                                                                                                                                                                                                                                   	| Elektrokit 	| included into 399-kit 	|
| ![LoPy!](https://www.electrokit.com/uploads/productimage/41000/5mm-gr%C3%B6n-diffus.jpg)    	| LED 5mm green        	| 4  	| diffus 80mcd                                                                                                                                                                                                                                     	| Elektrokit 	| included into 399-kit 	|
| ![LoPy!](https://www.electrokit.com/uploads/productimage/41016/41016089.jpg)                	| Button               	| 1  	| 12x12mm                                                                                                                                                                                                                                          	| Elektrokit 	| 19                    	|
| ![LoPy!](https://www.electrokit.com/uploads/productimage/40810/40810233.png)                	| Resistor             	| 1  	| 0.25W 330ohm (330R)                                                                                                                                                                                                                              	| Elektrokit 	| included into 399-kit 	|
| ![LoPy!](https://www.electrokit.com/uploads/productimage/41003/41003290.jpg)                	| USB-kabel            	| 1  	| A-type – micro-B 5p type 1.8m                                                                                                                                                                                                                    	| Elektrokit 	| included into 399-kit 	|
|                                                                                             	|                      	|    	|                                                                                                                                                                                                                                                  	| Total      	| 419 sek               	|



## Computer setup

### Hardware-part progrming environment setup
For the development of the software portion of this project, we utilized a computer running macOS, along with PyCharm 2022.3.2 (Community Edition) as our primary programming environment.

To enable support for MicroPython, a lean and efficient implementation of Python 3, we installed the MicroPython plugin in PyCharm. This can be achieved by following these steps:

1. After installing and launching PyCharm, navigate to File > Settings > Plugins > Marketplace.
1. Search for "MicroPython" and click on the Install button.

Upon successful installation of the plugin, we are ready to initiate our MicroPython project:

1. Go to File > New Project and assign a name to your project.
1. Under the project interpreter, the Python installation is detected automatically. Simply click CREATE to establish a new project in Python.

For our project to run on the Raspberry Pi Pico, we needed to activate MicroPython support. Here's how:


1. In PyCharm, navigate to File > Preferences > Languages and Platforms > MicroPython.
1. Check the "Enable MicroPython support" box.
1. Select "Raspberry Pi Pico" from the dropdown list for the device type.
1. Check the "Auto-detect device path" box so that the IDE automatically identifies which port the Raspberry Pi Pico is connected to. If the IDE fails to detect the port, open the Device Manager, identify the port manually, and enter it in the Device path line.
Lastly, to prevent unnecessary files from being copied to the Raspberry Pi Pico, navigate to Project:YourName > Project Structure in the settings. Right-click the .idea folder and mark it as Excluded. This folder contains specific settings for PyCharm, and excluding it prevents these files, which are redundant on the Raspberry Pi Pico, from occupying valuable space.

### Server-part progrming environment setup
The software development phase of this project was conducted on a computer running either macOS or Ubuntu, with JetBrains' WebStorm 2022 serving as the primary Integrated Development Environment (IDE).

As the server part of our solution is implemented in JavaScript, it was necessary to install Node.js version 16.20. Node.js is an open-source, cross-platform, back-end JavaScript runtime environment that runs on the V8 engine and executes JavaScript code outside a web browser. There are various tutorials available detailing the installation process for Node.js across different macOS versions, such as the guide found on the following link: https://nodesource.com/blog/installing-nodejs-tutorial-mac-os-x/

In addition to the Node.js environment, several additional libraries were needed to ensure proper functionality. These libraries were installed from the Node Package Manager (NPM) repository:

"async-mqtt": "^2.6.3" - A library for handling MQTT (Message Queuing Telemetry Transport), a lightweight messaging protocol for small sensors and mobile devices.
"axios": "^1.4.0" - A popular, promise-based HTTP client that makes it easy to send asynchronous HTTP requests.
"node-app-settings": "^0.0.5" - This library allows for easy management of application settings in a Node.js environment.
"uuid": "^9.0.0" - A library to generate universally unique identifiers, which are used to uniquely identify information in computer systems.
Each of these libraries plays a vital role in the functionality of our server system, enhancing its capabilities and efficiency in server health and environmental monitoring.

### MQTT Broker

In our project, we utilize a Message Queuing Telemetry Transport (MQTT) Broker as the central, communicative hub or 'gateway' software. The server, running Ubuntu 20.04, employs Mosquitto as the MQTT broker.

Mosquitto is a widely recognized MQTT broker that offers high performance and reliability. It is lightweight and suitable for all types of systems, from low power single board computers to full servers. It also supports the latest MQTT 5.0 protocol in addition to older versions for wider compatibility.

Installing Mosquitto on Ubuntu is a straightforward process. Below are the commands you'll need to enter in your terminal:

```bash 
sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa
sudo apt-get update
sudo apt-get install mosquitto
sudo apt-get install mosquitto-clients
sudo apt clean
```

## Putting everything together
![](https://hackmd.io/_uploads/HJh2vK-K3.jpg)

The connectivity process for this setup revolves around the central Raspberry Pi Pico microcontroller which is assembled on a breadboard. It's important to maintain careful attention to the specific connections, as incorrect wiring can lead to a malfunctioning system or potential damage to the components. Here is a step-by-step breakdown:

**Power Connection:** The Raspberry Pi Pico is powered by a 5V power supply. This power is provided to the microcontroller's USB connector.

**Green LED:** The Green LED is connected to the GPIO pins GP18-21 (pins 24-27). The cathode (shorter leg) of the LED is connected to the GND, and the anode (longer leg) is connected to the GPIO pin 

**Red LED:** The Red LED is connected to GPIO pin GP22 (pin 29). As with the green LED, a 330 ohm resistor is used to connect the anode of the LED to the GPIO pin through a 330 ohm (330R) resistor which is essential to limit the current flow and prevent the LED from burning out. The cathode is connected to the GND.

**DHT11 Sensor:** The DHT11 temperature and humidity sensor is connected to GPIO pin GP16 (pin 21). The DHT11 sensor has three pins: VCC (power), GND (ground), and DATA. The VCC is connected to the 3.3V power supply, GND to the ground, and DATA to the GP16 pin.

**Button:** The button is connected to GPIO pin GP15 (pin 20). One terminal of the button is connected to the GPIO pin, and the other terminal is connected to the GND. It's advisable to use a pull-up resistor with the button to ensure a well-defined input when the button is not pressed.


## Platform

To expedite the project's implementation and ensure seamless integration with existing systems, I leveraged my own previously developed platform. This platform boasts a robust HTTP API and is interconnected with various databases, providing a rich ecosystem to build upon. The decision to use this pre-existing platform substantially reduced development time, promoting a higher degree of congruity with the current software environment. An additional advantage of this choice was the elimination of extra costs, given that utilizing my own platform didn't incur any additional expenditures. Therefore, it not only provided a cost-effective solution but also facilitated a streamlined, efficient development process, maintaining the integrity and coherence of the existing program environment.

The central method deployed for this project is a data logging approach that works via a specific API endpoint "/monitor/10/record/". This method accepts two parameters: the ID of the indicator (a unique identifier for each server health or environmental parameter being monitored) and the respective value of the indicator. This strategy enables efficient tracking of multiple variables simultaneously, by recording their values at regular intervals. By collecting and logging this data, we're able to observe patterns and trends over time, providing valuable insights into the operational status of the servers and the environment within the server room.

## The code
### Raspberry Pi Pico microprogramm
* main.py: This is the main script that automatically executes upon boot. It is the entry point for the program and controls the high-level flow of the program's operation.
* pins.py: This script is responsible for initializing the pins of the Raspberry Pi Pico. It imports the required classes from the machine and dht modules and defines a function initialize_pins() that sets up the GPIO pins for the LEDs, the button, and the DHT11 sensor. The function also initializes the state of the LEDs.
* servery.py: This script defines a class Server that represents a server with a name, status, and associated LED. The set_status() method allows changing the status of the server.
* wifi.py: This script contains the WiFi class that manages the connection to a WiFi network using the network and uasyncio modules. The class includes methods to connect, reconnect, and check the connection status to the WiFi network. The connect() method is defined as an asynchronous method, meaning it can run concurrently with other parts of your program without blocking them. This is useful because WiFi operations can take some time, and using asynchronous functions ensures your program remains responsive.


This script describes a system that uses a Raspberry Pi Pico microcontroller to monitor the health of servers in a network. It communicates the server statuses via MQTT (a lightweight messaging protocol for small sensors and mobile devices), and can report temperature and humidity conditions of the server room.

Key details of the main.py script:

Main variables and pin initialization: The script starts by defining key variables such as WLAN credentials and MQTT broker details. It defines the server list and initializes the GPIO pins for the LEDs and DHT11 sensor. It also creates a WiFi object to manage the network connection.

```python 
WLAN_SSID = "Tele2"
WLAN_PASS = "gj0000rw"

MQTT_BROKER = "192.168.0.22"
MQTT_PORT = 1883
#...
SERVERS = [
    Server("192.168.1.1", "none", 0),
    Server("192.168.1.2", "none", 1),
    Server("192.168.1.3", "none", 2),
    Server("192.168.1.4", "none", 3),
#...
pin_led, pin_red_1, pin_button, data, leds = pins.initialize_pins()
#...
wifi = WiFi(WLAN_SSID, WLAN_PASS)
]
```

Button setup: It then defines a function button_action() that gets triggered periodically via a hardware timer (button_timer). This function checks whether the button has been pressed and, if so, it publishes a "restart" command to any server with an "error" status.

MQTT client: The script creates an MQTT client and defines a callback function (mqtt_sub_cb) that gets triggered whenever a message is received on the subscribed topic "server". The callback function updates the status of the corresponding server in the SERVERS list and sets an alert flag if a server status is 'error'.

```python 
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
```

Temperature reporting: It also sets up a second hardware timer (temperature_timer) that periodically publishes temperature and humidity readings to the "temperature" topic.

Network monitoring and connection maintenance: The script contains an asynchronous function network() that continuously checks WiFi and MQTT connection statuses and reconnects if necessary. This function is registered as an asyncio task to run concurrently with the rest of the script.

LED alert system: Another asynchronous function blinker() toggles the LEDs to reflect server statuses and network connection state. LEDs corresponding to servers with an "error" status or when the WiFi is disconnected, blink every 0.6 seconds. This function is also registered as an asyncio task.

MQTT Listener: The mttq_listener() function is an asyncio task that continuously checks for incoming MQTT messages when the MQTT connection is active.

Asynchronous event loop: Lastly, the script creates an asyncio event loop and adds the network(), blinker(), and mttq_listener() tasks to it, before starting the loop with loop.run_forever(). This sets up a concurrency model where the three tasks run simultaneously, providing a responsive system that can manage network connections, alert LEDs, and MQTT message handling at the same time.

```python
loop = asyncio.get_event_loop()
loop.create_task(network())
loop.create_task(blinker())
loop.create_task(mttq_listener())
loop.run_forever()
```
### Server gateway/client code
The server software, implemented in Node.js, serves dual purposes: it can act as either a gateway or a client node, depending on a specific configuration parameter. This parameter is set in a configuration file, making the server code flexible and reusable.

````json 
{
  "serverName": "192.168.1.1",
  "serverRole": "slave",
  "mqttBrokerAddress": "tcp://192.168.0.22:1883",
  "databaseAPIEndpoint": "https://api.behind.ai:6002/api"
}
````

**Library Imports:** The script starts by importing necessary libraries. node-app-settings to handle configuration settings, async-mqtt for asynchronous MQTT functionalities, uuid for creating unique identifiers, axios for making HTTP requests, https for working with HTTPS, child_process for running commands in a shell, and Server is a custom class that defines methods to interact with the server.

**Configuration Loading:** The config object is created by reading data from a settings.json file using node-app-settings.

**MQTT Client Initialization:** An MQTT client is created and connected to the broker using the address specified in the configuration (config.mqttBrokerAddress).

**Server Status Publishing:** A repeating interval is set up that checks the status of the server every 3 seconds. The status is then published to the server topic on the MQTT broker. The message includes the server's name, its status, and a unique message ID.

```javascript 
client.publish("server", 
               JSON.stringify({
                    server: config.serverName, 
                    status: status, 
                    msgId:v4()})
              );
```

**Subscription and Message Handling:** The script then subscribes to the servers topic on the MQTT broker. It sets up a callback function to handle incoming messages. When a message arrives, it is parsed and checked:

```javascript 
    await client.subscribe("servers")
    if(config.serverRole == "master"){
        await client.subscribe("temperature")
    }
    client.on("message", function (topic, message) {
        // message is Buffer
        let msg = JSON.parse(message.toString())

        if(topic == "temperature"){

        }

        if(topic == "servers"){
            
        }
    });
````

If the topic is temperature, it triggers an HTTPS request to a database API endpoint (defined in the config) to store temperature and humidity data.

```javascript 
const url_temp = config.databaseAPIEndpoint + 
      `/monitor/10/record/add?alias=iot.temperature.minutely&value=${msg.temperature}`
axios.get(url_temp);

const url_humidity = config.databaseAPIEndpoint + 
      `/monitor/10/record/add?alias=iot.humidity.minutely&value=${msg.humidity}`
axios.get(url_humidity);
```

If the topic is servers, it checks if the message's server name matches its own and then acts on commands like shutdown or restart, using the exec function from child_process to execute system-level commands.

**Temperature limits and control**
The gateway checks this data against predefined acceptable ranges (TEMP_MAX, HUM_MIN, HUM_MAX) for temperature and humidity in the server room. If the temperature exceeds TEMP_MAX, or the humidity is outside the HUM_MIN to HUM_MAX range, it means the conditions in the server room are not optimal.

Once it determines that these conditions are exceeded, the gateway takes corrective action. In this scenario, it sends a 'shutdown' command to all servers in the server room.
```javascript
if(parseFloat(msg.temperature)>TEMP_MAX ||
   parseFloat(msg.humidity) < HUM_MIN ||
   parseFloat(msg.humidity) > HUM_MAX){
    servers.forEach((s)=>{
        client.publish("servers", 
                       JSON.stringify({
                            command: "shutdown", 
                            server: s, 
                            msgId:v4()}
                        )
                      );
    })
}
```

**Master Server Handling:** If the server role specified in the settings file is "master", the server also subscribes to the temperature topic to receive temperature data updates.

The script is wrapped in an asynchronous immediately invoked function expression (IIFE) to allow for top-level await, ensuring that the MQTT client is connected before the rest of the script is executed.

## Transmitting the data / connectivity


The connectivity network map for this project can be broken down into three integral parts, each serving a crucial role in ensuring efficient data transmission and interaction between devices.

1. Local Server Network: The servers in the server room are interconnected through a hub using wired LAN connections. These servers are also linked to a gateway, over which they communicate using the MQTT protocol, broadcasting their operational status every 10 seconds.
1. Raspberry Pi Pico WH Connection: The Raspberry Pi Pico WH is wirelessly connected to the gateway via the MQTT protocol. This connection is established through a router linked to the main network via a wired LAN connection. The Raspberry Pi Pico WH, equipped with sensors, broadcasts environmental data such as temperature and humidity readings to the gateway every minute using the MQTT protocol.
1. Gateway to Cloud Connectivity: The gateway and its corresponding software are linked to an external cloud HTTP API via a router that facilitates internet connectivity. This connection is organized by HTTP requests, sent from the gateway to the remote server in the cloud.
![](https://hackmd.io/_uploads/rJxihObYh.png)

The design of this network architecture ensures that the local server networks are isolated from the internet, providing an extra layer of security. The connection to the internet is established exclusively from the gateway to the cloud servers, further safeguarding the integrity and security of the local server room network.

## Presenting the data

For data storage, I have chosen to use PostgreSQL, a robust and advanced open-source Relational Database Management System (RDBMS). PostgreSQL offers several benefits that make it an excellent choice for this project. It supports both SQL (relational) and JSON (non-relational) querying, which adds to its versatility. Furthermore, it has a reputation for reliability, data integrity, and correctness, critical for preserving and analyzing server and environmental data.

For data visualization, I employ custom software developed in Vue.js, an open-source JavaScript framework, combined with the ApexCharts library. ApexCharts is a modern charting library that aids developers in creating stunning and interactive visualizations for 
b pages. Being an open-source project licensed under MIT, ApexCharts is free for use in commercial applications, making it a cost-effective choice.

The software setup ensures that temperature and humidity data is added every minute, and I have the capability to display this data over different time frames, such as the last hour or the entire day.

![](https://hackmd.io/_uploads/HJnpnc-Yn.png)


A unique feature of my implementation is the ability to signal alarms when recent values on the chart exceed or drop below certain predefined thresholds. This helps in immediate detection of any environmental anomalies that could potentially harm the servers.

The data stored in the PostgreSQL database is preserved indefinitely, allowing for long-term trend analysis and the ability to retrospectively investigate any issues that may arise. The longevity of the data enhances the value of the monitoring system and contributes to improved server room management.


## Finalizing the design
The project, as it stands, has been an informative and exciting journey. It has been an interesting blend of hardware and software work, which has allowed for in-depth exploration into topics such as IoT protocols, data processing and visualization, and server-side scripting.

The final result is an IoT ecosystem capable of broadcasting server status, temperature, and humidity readings in near real-time. 

Here's how the final assembly looks:

![](https://hackmd.io/_uploads/SkA4kjbKn.jpg)

{%youtube ZRgbUHafk1I%}

It's pleasing to see that the system has been robust over several days of continuous operation, suggesting a high degree of stability in its current form. The debugging process further helped in making the system more resilient.

However, as with any project, there's always room for improvement. Notably, the system's security aspects could be enhanced. Currently, the MQTT broker accepts unauthorized connections and doesn't verify the origin of messages, which is a significant security risk. Improvements can be made on both the hardware (the Raspberry Pi Pico WH) and the server-side software.

Additionally, more features could be incorporated into this project with more time. For instance, adding more sensor types, or implementing machine learning algorithms to predict future temperature and humidity patterns based on historical data.

Overall, it was a rewarding experience working on this project. 

