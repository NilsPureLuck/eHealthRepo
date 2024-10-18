import paho.mqtt.client as mqtt

broker_address="test.mosquitto.org"
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="FeutchtigkeitPublisher")

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)

client.on_connect = on_connect
client.connect(broker_address, 1883)

topic = "eHealth/Feuchtigkeit"
payload = "77%"

result = client.publish(topic, payload)
status = result[0]

if status == 0:
    print("Just published "+ payload + " to topic " + topic)
else:
    print(f"Failed to send message to topic")