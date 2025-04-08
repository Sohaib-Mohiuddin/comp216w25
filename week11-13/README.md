# Paho-MQTT Installation Guide

## Introduction
This guide provides step-by-step instructions for installing the **Paho-MQTT** Python library on **Ubuntu, Windows, and macOS**.


## Prerequisites
- Ensure **Python 3** is installed on your system.
- It is recommended to create a **virtual environment** before installing Paho-MQTT.


## Installation Instructions

### Ubuntu (Linux)
#### 1. Update package lists:
```bash
sudo apt update
```
#### 2. Install Python and pip (if not installed):
```bash
sudo apt install python3 python3-pip -y
```
#### 3. Install Paho-MQTT:
```bash
pip install paho-mqtt
```
#### 4. Verify installation:
```bash
python3 -c "import paho.mqtt.client as mqtt; print('Paho-MQTT installed successfully!')"
```


### Windows
#### 1. Install Python:
- Download and install Python from [python.org](https://www.python.org/downloads/)
- Ensure **Add Python to PATH** is checked during installation.

#### 2. Install Paho-MQTT:
Open **Command Prompt (cmd)** and run:
```cmd
pip install paho-mqtt
```
#### 3. Verify installation:
```cmd
python -c "import paho.mqtt.client as mqtt; print('Paho-MQTT installed successfully!')"
```


### macOS
#### 1. Install Homebrew (if not installed):
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
#### 2. Install Python and pip:
```bash
brew install python3
```
#### 3. Install Paho-MQTT:
```bash
pip3 install paho-mqtt
```
#### 4. Verify installation:
```bash
python3 -c "import paho.mqtt.client as mqtt; print('Paho-MQTT installed successfully!')"
```


## Creating a Virtual Environment (Optional but Recommended)
Before installing Paho-MQTT, you can create a virtual environment:
```bash
python3 -m venv mqtt_env
source mqtt_env/bin/activate  # On Windows use: mqtt_env\Scripts\activate
pip install paho-mqtt
```


## .env File Setup

### 1. Create a `.env` file in your project directory:
```bash
touch .env
```

### 2. Add the following lines to the `.env` file:
```ini
USERNAME=your_username
PASSWORD=your_password
OWM_API_KEY=your_openweathermap_api_key
```

### 3. Load the environment variables in your Python script:
```python
import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
owm_api_key = os.getenv('OWM_API_KEY')
```


## Additional Resources
- [Paho-MQTT Documentation](https://www.eclipse.org/paho/)
- [Python Package Index (PyPI) - paho-mqtt](https://pypi.org/project/paho-mqtt/)

---

# Securing MQTT with Password-Based Authentication

This guide provides instructions on setting up password-based authentication for an MQTT broker using Mosquitto. The setup includes creating a password file, configuring the broker, and testing the authentication.

1. **Create a Password File**
```bash
sudo nano /etc/mosquitto/passwd
```

Change permissions (OPTIONAL):
```bash
sudo chmod 0700 /etc/mosquitto/passwd
```

2. **Add Usernames and Passwords**
```ini
username1:password1
username2:password2
```

3. **Generate Password Hashes**
```bash
sudo mosquitto_passwd -U /etc/mosquitto/passwd
```

4. **Edit Mosquitto Configuration**
```bash
sudo nano /etc/mosquitto/conf.d/default.conf
```

Add the following lines:
```ini
allow_anonymous false
password_file /etc/mosquitto/passwd
```

5. **Restart Mosquitto**
```bash
sudo systemctl restart mosquitto
```

---

# Secure MQTT Setup with SSL/TLS

This guide provides instructions on setting up SSL/TLS for an MQTT broker using OpenSSL. The setup includes generating certificates and keys and configuring the broker and clients for secure communication.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Generating SSL Certificates](#generating-ssl-certificates)
- [Configuring Mosquitto for SSL](#configuring-mosquitto-for-ssl)
- [Client Configuration](#client-configuration)
- [Setup Instructions](#setup-instructions)
  - [Ubuntu Setup](#ubuntu-setup)
  - [Windows Setup](#windows-setup)
  - [macOS Setup](#macos-setup)

## Prerequisites
Ensure you have OpenSSL and Mosquitto installed on your system:

### Install OpenSSL and Mosquitto

#### Ubuntu:
```bash
sudo apt update
sudo apt install openssl mosquitto mosquitto-clients -y
```

#### Windows:
Download and install OpenSSL from [OpenSSL for Windows](https://openssl-library.org/source/) and Mosquitto from [Eclipse Mosquitto](https://mosquitto.org/download/).

#### macOS:
```bash
brew install openssl mosquitto
```

## Generating SSL Certificates

### 1. Create a Certificate Authority (CA)
```bash
openssl genrsa -out ca.key 2048
openssl req -new -x509 -days 365 -key ca.key -out ca.crt -subj "/CN=MQTT-CA"
```

### 2. Generate Server Certificates
```bash
openssl genrsa -out server.key 2048
openssl req -new -key server.key -out server.csr -subj "/CN=MQTT-Server"
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -days 365
```

### 3. Generate Client Certificates
```bash
openssl genrsa -out client.key 2048
openssl req -new -key client.key -out client.csr -subj "/CN=MQTT-Client"
openssl x509 -req -in client.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out client.crt -days 365
```

## Configuring Mosquitto for SSL
Edit the Mosquitto configuration file (`mosquitto.conf`):
```ini
listener 1883
cafile /path/to/ca.crt
certfile /path/to/server.crt
keyfile /path/to/server.key
require_certificate true
```
Restart Mosquitto:
```bash
sudo systemctl restart mosquitto
```

## Client Configuration
To connect with SSL, use the following command:
```bash
mosquitto_pub -h localhost -p 8883 --cafile ca.crt --cert client.crt --key client.key -t "test/topic" -m "Secure message"
```

## Setup Instructions

### Ubuntu Setup
1. Install OpenSSL and Mosquitto: `sudo apt install openssl mosquitto -y`
2. Generate certificates using the commands above.
3. Edit `mosquitto.conf` to enable SSL.
4. Restart the Mosquitto service: `sudo systemctl restart mosquitto`
5. Use the client command to test secure publishing and subscribing.

### Windows Setup
1. Install OpenSSL and Mosquitto from official websites.
2. Open a PowerShell window and navigate to the OpenSSL installation directory.
3. Run the certificate generation commands in PowerShell.
4. Modify `mosquitto.conf` and restart Mosquitto.
5. Use the Mosquitto client to test secure connections.

### macOS Setup
1. Install OpenSSL and Mosquitto via Homebrew: `brew install openssl mosquitto`
2. Generate certificates using OpenSSL.
3. Edit `mosquitto.conf` to enable SSL.
4. Restart Mosquitto: `brew services restart mosquitto`
5. Test secure MQTT connections using the Mosquitto client.

## Conclusion
You have successfully set up a secure MQTT broker using SSL/TLS. Ensure all clients use valid certificates when connecting to the broker.

