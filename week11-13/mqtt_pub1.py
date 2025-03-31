import sys
import os
from dotenv import load_dotenv
import paho.mqtt.client as paho

load_dotenv()

USERNAME = os.getenv("MQTT_USERNAME")
PASSWORD = os.getenv("MQTT_PASSWORD")

client = paho.Client(callback_api_version=paho.CallbackAPIVersion.VERSION2)

if USERNAME and PASSWORD:
    client.username_pw_set(USERNAME, PASSWORD)

if client.connect("localhost", 1883, 60) != 0:
    print("Couldn't connect to the mqtt broker")
    sys.exit(1)

client.publish("test_topic", "Hi!", 0)
client.disconnect()