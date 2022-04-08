#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <DHT.h>
#include "config.h"

#define DHTPIN 4
#define DHTTYPE DHT11
#define BROKER_URL "192.168.0.68"
#define MSG_SIZE 24

char msg[MSG_SIZE];

DHT dht(DHTPIN, DHTTYPE);
WiFiClient wifi_client;
PubSubClient mqtt_client(wifi_client);

void setup(void)
{
  Serial.begin(115200);

  dht.begin();
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

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
 snprintf(msg, MSG_SIZE, "%f", t);
 mqtt_client.publish("home/room/temp", msg);
 delay(2000);
}
