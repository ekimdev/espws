import os

from influxdb_client import InfluxDBClient
from fastapi import FastAPI

org = os.getenv("DOCKER_API_ORG")
token = os.getenv("DOCKER_API_TOKEN")
url = "http://db:8086"

influx_client = InfluxDBClient(url=url, token=token, org=org)
app = FastAPI()


def get_table_from_query(query: str):
    return influx_client.query_api().query(query)


@app.get("/temperature")
def temperature_resource():
    temperature_query = ' from(bucket:"db0")\
    |> range(start: -10s)\
    |> filter(fn:(r) => r._measurement == "temperature")\
    |> filter(fn: (r) => r.location == "room")\
    |> filter(fn:(r) => r._field == "temperature_value" ) '

    tables = get_table_from_query(temperature_query)
    if not tables:
        return dict(temperature="No measurement available")

    record = tables[0].records[-1]
    response = dict(
        temperature=record.get_value(),
    )
    return response


@app.get("/humidity")
def humidity_resource():
    humidity_query = ' from(bucket:"db0")\
    |> range(start: -10m)\
    |> filter(fn:(r) => r._measurement == "humidity")\
    |> filter(fn: (r) => r.location == "room")\
    |> filter(fn:(r) => r._field == "humidity_value" ) '

    tables = get_table_from_query(humidity_query)
    if not tables:
        return dict(humidity="No measurement available")

    record = tables[0].records[-1]
    response = dict(
        humidity=record.get_value(),
    )
    return response


@app.get("/")
def root_resource():
    temperature_json = temperature_resource()
    humidity_json = humidity_resource()

    return {
        "temperature": temperature_json["temperature"],
        "humidity": humidity_json["humidity"],
    }
