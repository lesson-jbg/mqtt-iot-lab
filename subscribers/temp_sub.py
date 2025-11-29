import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print("Temperature Sub:", msg.payload.decode())

client = mqtt.Client()
client.connect("localhost", 1883, 60)
client.subscribe("iot/12218588/temp")
client.on_message = on_message
client.loop_forever()
