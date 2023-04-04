# micropython-ESP8266-AM2302/DHT22
Advertising Temperature Data from AM2302/DHT22 with micropython on ESP8266 (NodeMCU) Board

## Requirement

* NodeMCU board with ESP8266
* an AM2302/DHT22 Temperature Sensor (If you want to connect more than one, you can edit the code.)
* Available WiFi Signal with known user credentials

## Installation

* First you have to flash micropython firmware to your ESP8266 board with esptool.py if you did not before. (to download the firmware go to https://micropython.org/download/?port=esp8266)
* Clone the project (git clone https://github.com/omur-dalan/micropython-ESP8266-DHT22.git)
* Use any ide or cli to upload project files to the board (https://code.visualstudio.com, https://marketplace.visualstudio.com/items?itemName=pycom.Pymakr)

## Features

* Board will adverstise a JSON data from its ip address

## Extra (Monitoring)

* You can use any monitoring application (https://www.zabbix.com etc.) to monitor trends or trigger alarms.
* Use HTPP Agent method and JSON preproccessing like "$.sensors[0].temperature" and "$.sensor[0].temperature" or "$.sensor[0].humidity" to get seperate sensor values.
