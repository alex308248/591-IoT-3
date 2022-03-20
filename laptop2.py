import time
from paho.mqtt import client as mqtt_client

broker = '192.168.0.179'
port = 1883
path = "record.txt"
client_id = "laptop2"
subtopics = ["lightSensor", "threshold", "LightStatus", "Status/RaspberryPiA", "Status/RaspberryPiC"]

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)

def on_message(client, userdata, msg):
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + ", Topic: " + msg.topic + ", Contents: " + str(msg.payload))
    f = open(path, "a+")
    f.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + ", Topic: " + msg.topic + ", Contents: " + str(msg.payload) + "\n")
    f.close()

def run():
    client = mqtt_client.Client(client_id)
    client.connect(broker, port)
    client.on_connect = on_connect
    for subs in subtopics:
        client.subscribe(subs)
    client.on_message = on_message
    client.loop_forever()

if __name__ == '__main__':
    run()