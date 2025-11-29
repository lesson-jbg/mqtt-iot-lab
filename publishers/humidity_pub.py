import paho.mqtt.client as mqtt
import time, random

client = mqtt.Client()
client.connect("localhost", 1883, 60)

while True:
    hum = random.randint(40, 90)
    msg = f"ID:12218588 Humidity:{hum}"
    client.publish("iot/12218588/humidity", msg)
    print("Published:", msg)
    time.sleep(2)
