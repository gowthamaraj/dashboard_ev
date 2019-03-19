
from influxdb import InfluxDBClient
import random
client = InfluxDBClient(host='localhost', port=8086)

client.create_database('network')
client.switch_database('network')


while True:
    total= random.randint(1,101)
    print(total)
    json_body = [ { "measurement": "astra", "tags": { "user": "impact", }, "fields": { "tot": total, } } ] 
    client.write_points(json_body)