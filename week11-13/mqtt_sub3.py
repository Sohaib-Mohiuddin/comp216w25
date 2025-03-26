import paho.mqtt.client as paho
import json
import logging
import os
from dotenv import load_dotenv

load_dotenv()

# MQTT Broker Details
BROKER = "localhost"
PORT = 1883
TOPIC = "iot/sensor/temperature"
USERNAME = os.getenv("MQTT_USERNAME")
PASSWORD = os.getenv("MQTT_PASSWORD")

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
logger = logging.getLogger()

def on_connect(client, userdata, flags, rc, properties):
    """Callback for successful connection."""
    if rc == 0:
        logger.info("Connected to MQTT Broker")
        client.subscribe(TOPIC)
    else:
        logger.error("Failed to connect, return code %d", rc)

def on_message(client, userdata, msg):
    """Callback when a message is received."""
    try:
        payload = json.loads(msg.payload.decode())
        logger.info(f"Received Data: {json.dumps(payload, indent=4)}")
    except json.JSONDecodeError as e:
        logger.error(f"Error decoding JSON: {e}")

def start_subscriber():
    """Starts MQTT subscriber."""
    client = paho.Client(callback_api_version=paho.CallbackAPIVersion.VERSION2)

    # Enable authentication (if needed)
    if USERNAME and PASSWORD:
        client.username_pw_set(USERNAME, PASSWORD)

    # Set up callbacks
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(BROKER, PORT, 60)
    
    try:
        logger.info("Waiting for messages...")
        client.loop_forever()
    except KeyboardInterrupt:
        logger.info("Subscriber stopped by user.")
    finally:
        client.disconnect()
        logger.info("Disconnected from MQTT Broker")

if __name__ == "__main__":
    start_subscriber()
