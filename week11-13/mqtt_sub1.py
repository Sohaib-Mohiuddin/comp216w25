import sys
import os
from dotenv import load_dotenv
import paho.mqtt.client as paho

load_dotenv()

def message_handling(client, userdata, msg):
    print(f"{msg.topic}: {msg.payload.decode()}")

USERNAME = os.getenv("MQTT_USERNAME")
PASSWORD = os.getenv("MQTT_PASSWORD")

client = paho.Client(callback_api_version=paho.CallbackAPIVersion.VERSION2)

if USERNAME and PASSWORD:
    client.username_pw_set(USERNAME, PASSWORD)

client.on_message = message_handling

if client.connect("localhost", 1883, 60) != 0:
    print("Couldn't connect to the mqtt broker")
    sys.exit(1)

client.subscribe("test_topic")

try:
    print("Press CTRL+C to exit...")
    client.loop_forever()
except Exception:
    print("Caught an Exception, something went wrong...")
finally:
    print("Disconnecting from the MQTT broker")
    client.disconnect()