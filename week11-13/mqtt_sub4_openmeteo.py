import paho.mqtt.client as paho
import json
import logging
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# MQTT Broker Details
BROKER = "localhost"
PORT = 1883
TOPIC = "iot/weather/temperature"
USERNAME = os.getenv("MQTT_USERNAME")
PASSWORD = os.getenv("MQTT_PASSWORD")

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
logger = logging.getLogger()

# Store last 24 hours of temperature readings
temperature_data = deque(maxlen=24)
time_data = deque(maxlen=24)

# Set up Matplotlib figure
fig, ax = plt.subplots()
line, = ax.plot([], [], marker="o", linestyle="-", color="r", label="Temperature")

ax.set_xlabel("Time")
ax.set_ylabel("Temperature (°C)")
ax.set_title("Temperature in the Last 24 Hours")
ax.legend()
ax.grid(True)
plt.xticks(rotation=45)

anim = None  # Store animation globally

def on_connect(client, userdata, flags, rc, properties=None):
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
        temperature = float(payload["temperature"])
        timestamp = datetime.fromisoformat(payload["timestamp"])

        temperature_data.append(temperature)
        time_data.append(timestamp.strftime("%H:%M"))

        logger.info(f"Received Temperature: {temperature} °C at {timestamp}")

    except (json.JSONDecodeError, ValueError) as e:
        logger.error(f"Error processing message: {e}")

def update_plot(frame):
    """Updates the Matplotlib plot dynamically."""
    if time_data:
        line.set_data(range(len(time_data)), list(temperature_data))
        ax.set_xticks(range(len(time_data)))  
        ax.set_xticklabels(time_data, rotation=45)
        ax.relim()
        ax.autoscale_view()
        fig.canvas.draw()

def start_subscriber():
    """Starts MQTT subscriber and initializes real-time plotting."""
    global anim

    client = paho.Client(callback_api_version=paho.CallbackAPIVersion.VERSION2)

    if USERNAME and PASSWORD:
        client.username_pw_set(USERNAME, PASSWORD)

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(BROKER, PORT, 60)
    client.loop_start()

    anim = animation.FuncAnimation(fig, update_plot, interval=1000, cache_frame_data=False)  

    plt.show()

    client.loop_stop()
    client.disconnect()
    logger.info("Disconnected from MQTT Broker")

if __name__ == "__main__":
    start_subscriber()
