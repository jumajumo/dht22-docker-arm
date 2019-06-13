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

client = mqtt.Client(thingid)

client.will_set(thingTopic + "sys/state", "OFFLINE", qos=1, retain=True)

client.connect(brokeraddr)

client.publish(thingTopic, str(datetime.datetime.now()), qos=1, retain=True)
client.publish(thingTopic + "sys/type", "sensor", qos=1, retain=True)
client.publish(thingTopic + "sys/device", "dht22", qos=1, retain=True)
client.publish(thingTopic + "sys/state", "ONLINE", qos=1, retain=True)

client.publish(thingTopic + "env/thingid", thingid, qos=1, retain=True)
client.publish(thingTopic + "env/brokeraddr", brokeraddr, qos=1, retain=True)
client.publish(thingTopic + "env/refresh", refresh, qos=1, retain=True)
client.publish(thingTopic + "env/pin", pin, qos=1, retain=True)

try:
    while True:

        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, pin)

        client.publish(thingTopic + "humidity",humidity, qos=0, retain=True)
        client.publish(thingTopic + "temperature", temperature, qos=0, retain=True)

        time.sleep(refresh)

except:
    client.disconnect()
