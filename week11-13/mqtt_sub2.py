import paho.mqtt.client as paho
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
logger = logging.getLogger()

# MQTT Settings
BROKER = "localhost"
PORT = 1883
TOPIC = "iot/sensor/random"
USERNAME = os.getenv("MQTT_USERNAME")
PASSWORD = os.getenv("MQTT_PASSWORD")

def on_connect(client, userdata, flags, rc, properties):
    """Callback function when client connects to broker."""
    if rc == 0:
        logger.info("Connected to MQTT Broker")
        client.subscribe(TOPIC)  # Subscribe to the temperature topic
    else:
        logger.error("Failed to connect, return code %d", rc)

def on_message(client, userdata, msg):
    """Callback function when a message is received."""
    temperature_data = msg.payload.decode()
    logger.info(f"Received: {temperature_data}")

def start_subscriber():
    """Starts the MQTT subscriber."""
    client = paho.Client(callback_api_version=paho.CallbackAPIVersion.VERSION2)
    
    # Setup username and password
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
