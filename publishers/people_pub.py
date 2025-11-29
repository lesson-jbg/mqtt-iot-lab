import paho.mqtt.client as mqtt
import time, random

client = mqtt.Client()
client.connect("localhost", 1883, 60)

while True:
    people = random.randint(0, 10)
    msg = f"ID:12218588 People:{people}"
    client.publish("iot/12218588/people", msg)
    print("Published:", msg)
    time.sleep(3)
