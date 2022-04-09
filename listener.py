import os

from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
from paho.mqtt import client


bucket = os.getenv("DOCKER_LISTENER_BUCKET")
org = os.getenv("DOCKER_LISTENER_ORG")
token = os.getenv("DOCKER_LISTENER_TOKEN")
url = "http://db:8086"

influxdb_client = InfluxDBClient(
    url=url,
    token=token,
    org=org
)

write_api = influxdb_client.write_api(write_options=SYNCHRONOUS)


def on_connect(client, userdata, flags, rc):
    client.subscribe("home/room/temp")


def on_message(client, userdata, msg):
    temperature = float(msg.payload.decode())

    print("Writing to database...")
    sequence = [
        f"temperature,host=room value={temperature}",
        # "mem,host=host1 available_percent=15.856523",
    ]
    write_api.write(bucket, org, sequence)

    print(f"Room temperature: {temperature:.2f}")


mqtt_client = client.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

mqtt_client.connect("192.168.0.68")
mqtt_client.loop_forever()
