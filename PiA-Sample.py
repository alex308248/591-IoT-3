import time
from paho.mqtt import client as mqtt_client

broker = '192.168.0.179'
port = 1883
client_id = "PiA"
MQTT_TOPICS = ["lightSensor", "threshold"]

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
        publish(client, "Status/RaspberryPiA", "online", 2, True)
    else:
        print("Failed to connect, return code %d\n", rc)

def on_message(client, userdata, msg):
    print("Message received-> " + msg.topic + " : " + str(msg.payload))

def publish(client, topic, payload, qos = 2, retain = False):
    result = client.publish(topic, payload, qos, retain)
    status = result[0]
    if status == 0:
        print(f"Send to topic `{topic}`:    {payload}")
    else:
        print(f"Failed to send message to topic {topic}")

def run():
    client = mqtt_client.Client(client_id)
    client.will_set("Status/RaspberryPiA", "offline", 2, True)
    client.connect(broker, port)
    client.on_connect = on_connect
    client.on_message = on_message
    client.loop_start()
    for i in range(10000):
        n = i % 2
        payload = i%5 + 1
        
        publish(client, MQTT_TOPICS[n], payload, 2)
        time.sleep(3)
    client.loop_stop()

if __name__ == '__main__':
    run()