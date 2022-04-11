#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <DHT.h>
#include "config.h"  // put your network data here

#define DHTTYPE DHT11
#define MSG_SIZE 24

char msg_temperature[MSG_SIZE];
char msg_humidity[MSG_SIZE];

DHT dht(DHTPIN, DHTTYPE);
WiFiClient wifi_client;
PubSubClient mqtt_client(wifi_client);

void setup(void)
{
  Serial.begin(115200);

  dht.begin();
  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

  while(WiFi.status() != WL_CONNECTED){
    Serial.print(".");
    delay(500);
  }
  Serial.println("");
  Serial.print("Connected to WiFi");

  mqtt_client.setServer(BROKER_URL, 1883);
  delay(2000);
  mqtt_client.connect("ESP8266_1");
}


void loop()
{
 mqtt_client.loop();

 float t = dht.readTemperature();
 float h = dht.readHumidity();

 snprintf(msg_temperature, MSG_SIZE, "%f", t);
 mqtt_client.publish("home/room/temperature", msg_temperature);

 snprintf(msg_humidity, MSG_SIZE, "%f", h);
 mqtt_client.publish("home/room/humidity", msg_humidity);

 delay(5000);
}
