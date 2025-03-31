import paho.mqtt.client as paho
import json
import random
import time
import logging
import os
from datetime import datetime
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

def generate_sensor_data():
    """Generate random temperature and humidity data."""
    return {
        "timestamp": datetime.now().isoformat(),
        "temperature": round(random.uniform(18.0, 30.0), 2),
        "humidity": round(random.uniform(30.0, 80.0), 2)
    }

def on_connect(client, userdata, flags, rc, properties):
    """Callback for successful connection."""
    if rc == 0:
        logger.info("Connected to MQTT Broker")
    else:
        logger.error("Failed to connect, return code %d", rc)

def on_publish(client, userdata, mid, qos, properties):
    """Callback for successful message publish."""
    logger.info(f"Message {mid} published successfully")

def publish_sensor_data():
    """Publishes random sensor data to MQTT topic."""
    client = paho.Client(callback_api_version=paho.CallbackAPIVersion.VERSION2)

    # Enable authentication (if needed)
    if USERNAME and PASSWORD:
        client.username_pw_set(USERNAME, PASSWORD)

    # Set up callbacks
    client.on_connect = on_connect
    client.on_publish = on_publish

    client.connect(BROKER, PORT, 60)

    try:
        while True:
            sensor_data = generate_sensor_data()
            payload = json.dumps(sensor_data)
            client.publish(TOPIC, payload, qos=0)
            logger.info(f"Published: {payload}")
            time.sleep(1)
    except KeyboardInterrupt:
        logger.info("Publisher stopped")
    finally:
        client.disconnect()
        logger.info("Disconnected from MQTT Broker")

if __name__ == "__main__":
    publish_sensor_data()
