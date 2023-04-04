try:
    import usocket as socket
except:
    import socket

#Turn off debug messages
import esp
esp.osdebug(None)

#do some garbage collection
import gc
gc.collect()

#libraries neccessary for DHT sensors and using Pins
import dht
from machine import Pin

#define sensors here
sensors = []

#add some sensors here
sensors.append(dht.DHT22(Pin(14)))
#sensors.append(dht.DHT22(Pin(14)))
#sensors.append(dht.DHT22(Pin(14)))
#sensors.append(dht.DHT22(Pin(14)))

from time import sleep

from machine import Pin
import network

ssid = '<SSID_NAME>'
password = '<PASSWORD>'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

#Turn on the led if a valid connection to network has established
top_led = Pin(2, Pin.OUT)
top_led.on()

while station.isconnected() == False:
    pass

top_led.off()
print('Connection successful')
print(station.ifconfig())

