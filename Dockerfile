FROM resin/rpi-raspbian

RUN apt-get update && \
    apt-get -y install \
      python \
      python-dev \
      python-pip \
      python-virtualenv \
      gcc mono-mcs && \
      rm -rf /var/lib/apt/lists/*
RUN pip install Adafruit_Python_DHT -i https://pypi.python.org/simple
RUN pip install paho-mqtt -i https://pypi.python.org/simple

ADD publish.py /var/jumajumo/publish.py
RUN chmod +x /var/jumajumo/publish.py

CMD python /var/jumajumo/publish.py

