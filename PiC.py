from pydoc_data.topics import topics
import time
from paho.mqtt import client as mqtt_client

broker = '192.168.0.179'
port = 1883
client_id = "RaspberryPiC"
subtopics = ["lightSensor", "threshold", "LightStatus"]
pubtopics = ["LightStatus", "Status/RaspberryPiC"]

#status will be TurnOn or TurnOff
status = "TurnOn"
Threshold = 0
LightSensor = 0

def on_connect(client, userdata, flags, rc):
    # Use retained message and LWT to observe the status of RaspberryPiC
    if rc == 0:
        print("Connected to MQTT Broker!")
        publish(client, pubtopics[1], "online", 2, True)
    else:
        print("Failed to connect, return code %d\n", rc)

def on_message(client, userdata, msg):
    global Threshold, LightSensor, status
    print("Message received-> " + msg.topic + " " + str(msg.payload.decode("ascii")))
    if msg.topic == subtopics[0]:
        LightSensor = float(msg.payload.decode("ascii"))
    elif msg.topic == subtopics[1]:
        Threshold =float(msg.payload.decode("ascii"))
    elif msg.topic == subtopics[2]:
        status = msg.payload.decode("ascii") 
        return
    
    # Ditermine the current status  
    sta = "TurnOn"
    if LightSensor < Threshold:
        sta = "TurnOff"
    
    # If the status need to change, we will publish to the topic LightStatus
    if sta != status:
        print(LightSensor, Threshold)
        status = sta
        publish(client, pubtopics[0], status, 2, True)

def publish(client, topic, payload, qos = 2, retain = True):
    result = client.publish(topic, payload, qos, retain)
    status = result[0]
    if status == 0:
        print(f"Send to topic `{topic}` : {payload}")
    else:
        print(f"Failed to send message to topic {topic}")

def run():
    client = mqtt_client.Client(client_id)
    client.will_set(pubtopics[1], "offline", 2, True)
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(broker, port)
    for subs in subtopics:
        client.subscribe(subs)
    client.loop_forever()

if __name__ == '__main__':
    run()