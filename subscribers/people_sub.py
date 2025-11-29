import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print("PeopleCounter Sub:", msg.payload.decode())

client = mqtt.Client()
client.connect("localhost", 1883, 60)

client.subscribe("iot/12218588/people")  

client.on_message = on_message
client.loop_forever()
