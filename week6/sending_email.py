import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Email configuration
SMTP_SERVER = "smtp.gmail.com"  # For Gmail
SMTP_PORT = 587

SENDER_EMAIL = os.getenv("EMAIL_ADDRESS")
SENDER_PASSWORD = os.getenv("EMAIL_PASSWORD")

print(SENDER_EMAIL)

def send_email(recipient, subject, message):
    try:
        # Prepare the email
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = recipient
        msg["Subject"] = subject
        msg.attach(MIMEText(message, "plain"))

        # Send the email using SMTP
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.ehlo()
            server.starttls()  # Start a secure connection
            server.ehlo()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
        
        print("Email sent successfully!")

    except smtplib.SMTPAuthenticationError:
        print("Error: Authentication failed. Check your email and password.")
    except smtplib.SMTPException as e:
        print(f"Error: Failed to send email. {str(e)}")

# Get input from the user
recipient = input("Enter the recipient's email address: ")
subject = input("Enter the subject of the email: ")
message = input("Enter the message: ")

# Call the function to send the email
send_email(recipient, subject, message)
