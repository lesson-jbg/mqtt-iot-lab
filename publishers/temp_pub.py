import paho.mqtt.client as mqtt
import time, random

client = mqtt.Client()
client.connect("localhost", 1883, 60)

while True:
    temp = random.randint(20, 35)
    msg = f"ID:12218588 Temperature:{temp}"
    client.publish("iot/12218588/temp", msg)
    print("Published:", msg)
    time.sleep(2)
