import paho.mqtt.client as paho
import random
import time
import logging
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
logger = logging.getLogger()

# MQTT Settings
BROKER = "localhost"
PORT = 1883
TOPIC = "iot/sensor/random"
USERNAME = os.getenv("MQTT_USERNAME")
PASSWORD = os.getenv("MQTT_PASSWORD")

def generate_random_temperature():
    """Generates a random temperature between 15 and 30 degrees Celsius."""
    return round(random.uniform(15.0, 30.0), 2)

def on_connect(client, userdata, flags, rc, properties):
    """Callback function when client connects to broker."""
    if rc == 0:
        logger.info("Connected to MQTT Broker")
    else:
        logger.error("Failed to connect, return code %d", rc)

def on_publish(client, userdata, mid, qos, properties):
    """Callback function when a message is published."""
    logger.info(f"Message published with ID {mid}")

def publish_temperature():
    """Publishes a random temperature value at regular intervals."""
    client = paho.Client(callback_api_version=paho.CallbackAPIVersion.VERSION2)
    
    # Setup username and password
    if USERNAME and PASSWORD:
        client.username_pw_set(USERNAME, PASSWORD)

    # Set up callbacks
    client.on_connect = on_connect
    client.on_publish = on_publish

    client.connect(BROKER, PORT, 60)

    # Keep publishing random temperature data every 5 seconds
    try:
        while True:
            temperature = generate_random_temperature()
            message = f"Temperature: {temperature} °C"
            result = client.publish(TOPIC, message, qos=0)
            logger.info(f"Published: {message}")
            time.sleep(5)  # Delay before sending next message
    except KeyboardInterrupt:
        logger.info("Publisher stopped by user.")
    finally:
        client.disconnect()
        logger.info("Disconnected from MQTT Broker")

if __name__ == "__main__":
    publish_temperature()
