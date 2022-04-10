import os

from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from paho.mqtt import client


broker_url = os.getenv("DOCKER_LISTENER_BROKER_URL")
bucket = os.getenv("DOCKER_LISTENER_BUCKET")
org = os.getenv("DOCKER_LISTENER_ORG")
token = os.getenv("DOCKER_LISTENER_TOKEN")
url = "http://db:8086"

influxdb_client = InfluxDBClient(url=url, token=token, org=org)

write_api = influxdb_client.write_api(write_options=SYNCHRONOUS)


def on_connect(client, userdata, flags, rc):
    client.subscribe("home/room/temperature")
    client.subscribe("home/room/humidity")


def on_message(client, userdata, msg):
    if msg.topic == "home/room/temperature":
        data = float(msg.payload.decode())
        write_api.write(
            bucket,
            org,
            Point("temperature")
            .tag("location", "room")
            .field("temperature_value", data),
        )
        print(f"Room temperature: {data:.2f}")
    elif msg.topic == "home/room/humidity":
        data = float(msg.payload.decode())
        write_api.write(
            bucket,
            org,
            Point("humidity").tag("location", "room").field("humidity_value", data),
        )
        print(f"Room humidity: {data:.2f}")


mqtt_client = client.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

mqtt_client.connect(broker_url)
mqtt_client.loop_forever()
