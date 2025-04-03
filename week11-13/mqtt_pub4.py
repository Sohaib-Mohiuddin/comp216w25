import paho.mqtt.client as paho
import json
import time
import logging
import os
from datetime import datetime, timedelta
import requests
from dotenv import load_dotenv

load_dotenv()

# MQTT Broker Details
BROKER = "localhost"
PORT = 1883
TOPIC = "iot/weather/temperature"
USERNAME = os.getenv("MQTT_USERNAME")
PASSWORD = os.getenv("MQTT_PASSWORD")

# Open-Meteo API URL
OPEN_METEO_API_URL = "https://api.open-meteo.com/v1/forecast"

# Hardcoded city and country
CITY = "Toronto"
COUNTRY = "Canada"

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
logger = logging.getLogger()

def fetch_coordinates(city, country):
    """Fetch latitude and longitude for a city using OpenWeatherMap."""
    API_KEY = os.getenv("OWM_API_KEY")
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{country}&limit=1&appid={API_KEY}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data:
            lat, lon = data[0]["lat"], data[0]["lon"]
            return lat, lon
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching coordinates: {e}")
    
    return None, None

def fetch_historical_temperature(lat, lon):
    """Fetch the last 24 hours of temperature data from Open-Meteo."""
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(days=1)

    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m",
        "timezone": "auto",
        "start": start_time.strftime("%Y-%m-%dT%H:00"),
        "end": end_time.strftime("%Y-%m-%dT%H:00")
    }

    try:
        response = requests.get(OPEN_METEO_API_URL, params=params)
        response.raise_for_status()
        data = response.json()
        return data["hourly"]["time"], data["hourly"]["temperature_2m"]
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching historical temperature: {e}")
    
    return None, None

def publish_weather_data():
    """Publishes historical weather data to MQTT."""
    client = paho.Client(callback_api_version=paho.CallbackAPIVersion.VERSION2)

    if USERNAME and PASSWORD:
        client.username_pw_set(USERNAME, PASSWORD)

    client.connect(BROKER, PORT, 60)

    lat, lon = fetch_coordinates(CITY, COUNTRY)
    if lat is None or lon is None:
        logger.error("Could not retrieve coordinates. Exiting...")
        return

    times, temperatures = fetch_historical_temperature(lat, lon)
    if not times or not temperatures:
        logger.error("No temperature data retrieved. Exiting...")
        return

    try:
        for t, temp in zip(times, temperatures):
            payload = json.dumps({"timestamp": t, "temperature": temp})
            client.publish(TOPIC, payload, qos=0)
            logger.info(f"Published: {payload}")
            time.sleep(1)  # Simulate real-time publishing
    except KeyboardInterrupt:
        logger.info("Publisher stopped")
    finally:
        client.disconnect()
        logger.info("Disconnected from MQTT Broker")

if __name__ == "__main__":
    publish_weather_data()
