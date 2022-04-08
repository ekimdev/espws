from paho.mqtt import client


def on_connect(client, userdata, flags, rc):
    client.subscribe("home/room/temp")


def on_message(client, userdata, msg):
    temperature = float(msg.payload.decode())
    print(f"Room temperature: {temperature:.2f}")


mqtt_client = client.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

mqtt_client.connect("192.168.0.68")
mqtt_client.loop_forever()
