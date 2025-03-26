import paho.mqtt.client as paho
import json
import logging
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque
from datetime import datetime
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

# Store last 20 temperature readings
temperature_data = deque(maxlen=20)
time_data = deque(maxlen=20)

# Set up Matplotlib figure
fig, ax = plt.subplots()
line, = ax.plot([], [], marker="o", linestyle="-", color="b", label="Temperature")

ax.set_xlabel("Time")
ax.set_ylabel("Temperature (°C)")
ax.set_title("Live Temperature Updates")
ax.legend()
ax.grid(True)
plt.xticks(rotation=45)

# Store animation globally
anim = None  

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
        temperature = float(payload["temperature"])  # Convert to float
        timestamp = datetime.fromisoformat(payload["timestamp"])  # Convert timestamp

        # Append new data
        temperature_data.append(temperature)
        time_data.append(timestamp.strftime("%H:%M:%S"))  # HH:MM:SS format

        logger.info(f"Received Temperature: {temperature} °C at {timestamp}")

    except (json.JSONDecodeError, ValueError) as e:
        logger.error(f"Error processing message: {e}")

def update_plot(frame):
    """Updates the Matplotlib plot dynamically."""
    if time_data:
        line.set_data(range(len(time_data)), list(temperature_data))  # Ensure numeric data
        ax.set_xticks(range(len(time_data)))  
        ax.set_xticklabels(time_data, rotation=45)  # Display timestamps correctly
        ax.relim()  
        ax.autoscale_view()
        fig.canvas.draw()

def start_subscriber():
    """Starts MQTT subscriber and initializes real-time plotting."""
    global anim  # Store animation globally

    client = paho.Client(callback_api_version=paho.CallbackAPIVersion.VERSION2)

    if USERNAME and PASSWORD:
        client.username_pw_set(USERNAME, PASSWORD)

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(BROKER, PORT, 60)

    # Start MQTT loop in a separate thread
    client.loop_start()

    # Ensure anim is stored globally to prevent garbage collection
    anim = animation.FuncAnimation(fig, update_plot, interval=1000, cache_frame_data=False)  

    plt.show()  # Keep the plot open

    # Stop MQTT loop when the window is closed
    client.loop_stop()
    client.disconnect()
    logger.info("Disconnected from MQTT Broker")

if __name__ == "__main__":
    start_subscriber()
