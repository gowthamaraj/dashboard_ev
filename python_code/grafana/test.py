import serial
from influxdb import InfluxDBClient
client = InfluxDBClient(host='localhost', port=8086)
client.switch_database('network')
ser = serial.Serial('COM3',9600,timeout=1)
while(1):
    try:
        t1=int(ser.readline().decode('ascii'))
        print(t1)
        json_body = [ { "measurement": "monitoring", "tags": { "user": "rev_mech", }, "fields": { "dat": t1,} } ]
        client.write_points(json_body)
    except ValueError:
        pass 