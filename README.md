# dht22-docker-arm
Docker to publish dht22 sensor data to an mqtt broker

# build it 
docker build --rm -t jumajumo/dht22 .

# run it
docker run -d --network="host" --privileged -e brokeraddr=192.168.0.150 -e thingid=tslivingroom -e refresh=10 --name "jumajumo_dht22" jumajumo/dht22 

- --privileged: privileged is necessary in order to allow access to gpio
- -e brokeraddr: ip address of the mqtt broker (default port 1883 is used) (default "openhabian")
- -e thingid: thing id of the sensor (used for mqtt-topic) (default "default")
- -e pin: the gpio pin used for the sensor (default 4)
- -e refresh: publishing interval in seconds (default 5)
- --name: give it a name
