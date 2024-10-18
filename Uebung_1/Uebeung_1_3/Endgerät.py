import paho.mqtt.client as mqtt  # import the client

def on_message(client, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)

if __name__ == '__main__':

    broker_address="test.mosquitto.org"

    print("creating new instance")
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="subscriber")

    print("connecting to broker")
    client.connect(broker_address, 1883)

    print("Subscribing to topic","eHealthNils/Temperatur")
    client.subscribe("eHealthNils/Temperatur")

    print("Subscribing to topic", "eHealth/Feuchtigkeit")
    client.subscribe("eHealth/Feuchtigkeit")

    print("Subscribing to topic", "eHealth/Status")
    client.subscribe("eHealth/Status")

    client.on_message = on_message #attach function to callback
    client.loop_forever() #start the lo