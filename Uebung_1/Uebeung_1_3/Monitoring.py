import paho.mqtt.client as mqtt  # import the client

temperatur_received = False
feuchtigkeit_received = False


def on_connect(client, userdata, flags, rc, properties):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)

def publish_status(client):
    client.on_connect = on_connect
    client.connect(broker_address, 1883)

    topic = "eHealth/Status"
    payload = "Ok"

    result = client.publish(topic, payload)
    status = result[0]
    if status == 0:
        print("Just published " + payload + " to topic " + topic)
    else:
        print(f"Failed to send message to topic")

def on_message(client, userdata, message):
    global temperatur_received, feuchtigkeit_received

    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)

    if message.topic == "eHealthNils/Temperatur":
        temperatur_received = True
        print("Temperatur message received.")
    elif message.topic == "eHealth/Feuchtigkeit":
        feuchtigkeit_received = True
        print("Feuchtigkeit message received.")

    if temperatur_received and feuchtigkeit_received:
        publish_status(client)

if __name__ == '__main__':

    broker_address = "test.mosquitto.org"
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="Monitoring",)  # create new instance

    print("connecting to broker")
    client.connect(broker_address, 1883)  # connect to broker

    print("Subscribing to topic", "eHealthNils/Temperatur")
    client.subscribe("eHealthNils/Temperatur")

    print("Subscribing to topic", "eHealth/Feuchtigkeit")
    client.subscribe("eHealth/Feuchtigkeit")

    client.on_message = on_message  # attach function to callback

    client.loop_forever()