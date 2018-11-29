#!/usr/bin/python
import paho.mqtt.client as mqtt
import time
import os
import datetime
import Adafruit_DHT

thingid = os.getenv('thingid','default')
brokeraddr = os.getenv('brokeraddr','openhabian')
refresh = int(os.getenv('refresh', '5'))
pin = int(os.getenv('pin', '4'))

thingTopic = "jumajumo/" + thingid + "/"
refreshTopic = thingTopic + "env/refresh"

client = mqtt.Client(thingid)
client.connect(brokeraddr)

client.publish(thingTopic, str(datetime.datetime.now()))
client.publish(thingTopic + "sys/type", "sensor")
client.publish(thingTopic + "sys/device", "dht22")

client.publish(refreshTopic, refresh)

try:
    while True:

        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, pin)

        client.publish(thingTopic + "humidity",humidity)
        client.publish(thingTopic + "temperature", temperature)

        time.sleep(refresh)

except:
    client.disconnect()
