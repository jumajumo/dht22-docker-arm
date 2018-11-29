# dht22-docker-arm
Docker to publish dht22 sensor data to an mqtt broker

# build it 
docker build --rm -t jumajumo/dht22 .

# run it
docker run -d --network="host" 
  --privileged                    # privileged is necessary in order to allow access to gpio
  -e brokeraddr=192.168.1.174     # ip address of the mqtt broker (default port 1883 is used)
  -e thingid=tslivingroom         # thing id of the sensor (used for mqtt-topic)
  -e refresh=10                   # publishing interval in seconds
  --name "jumajumo_dht22"         # give it a name
  jumajumo/dht22 
