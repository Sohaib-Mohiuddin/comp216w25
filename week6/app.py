from flask import Flask, jsonify, request, render_template, redirect, url_for, flash
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)
app.secret_key = "supersecretkey"  # For flash messages (used in the email form route)

# Route 1: Output Hello World in JSON
@app.route("/")
def hello_world():
    response = {
        "message": "Hello, World!", 
        "status": "success"
    }
    return jsonify(response)

# Route 2: Custom JSON output with input from the address
@app.route("/greet")
@app.route("/greet/<name>")
@app.route("/greeting")
def greet_user(name = 'Killua'):
    response = {
        "greeting": f"Hello, {name.title()}!", 
        "status": "success"
    }
    return jsonify(response)

# Route 3: Render an HTML page and pass information from the backend
@app.route("/country_info")
def country_info():
    country_data = {
        "name": "Canada",
        "capital": "Ottawaaaaa",
        "population": "38 million",
        "region": "North America",
        "subregion": "Americas"
    }
    return render_template("country_info.html", country=country_data)

# Route 4: Connect to RestCountries API and display country data
@app.route("/country/<country_name>")
def get_country_info(country_name):
    api_url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        country_data = response.json()[0]
        processed_data = {
            "name": country_data.get("name", {}).get("common", "N/A"), # country_data['name']['common']
            "capital": country_data.get("capital", ["N/A"])[0],
            "population": country_data.get("population", 0000),
            "region": country_data.get("region", "N/A"),
            "subregion": country_data.get("subregion", "N/A"),
            "flag": country_data.get("flags", {}).get("png", "N/A"),
            "flagAlt": country_data.get("flags", {}).get("alt", "N/A")
        }
        return render_template("country_info.html", country=processed_data)
    else:
        return jsonify({"error": "Country not found"}), 404

# Route 5: Form for sending email
@app.route("/send_email", methods=["GET", "POST"])
def send_email():
    if request.method == "POST":
        recipient = request.form["recipient"]
        subject = request.form["subject"]
        message = request.form["message"]

        # Simple email service (SMTP)
        sender_email = os.getenv("EMAIL_ADDRESS")
        sender_password = os.getenv("EMAIL_PASSWORD")
        
        if not sender_email or not sender_password:
            flash("Email service is not configured properly.", "danger")
            print("Email service is not configured properly.")
            return redirect(url_for("send_email"))
                
        try:
            # Prepare the email
            msg = MIMEMultipart()
            msg["From"] = sender_email
            msg["To"] = recipient
            msg["Subject"] = subject
            msg.attach(MIMEText(message, "plain"))

            # Send the email using SMTP
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()  # Secure the connection
                server.login(sender_email, sender_password)
                server.send_message(msg)

            flash("Email sent successfully!", "success")
            print('Email sent successfully!')

        except smtplib.SMTPAuthenticationError:
            flash("Authentication failed. Check your email and password.", "danger")
            print('Authentication failed. Check your email and password.')
        except smtplib.SMTPException as e:
            flash(f"Failed to send email: {str(e)}", "danger")
            print(f'Failed to send email: {str(e)}')

        return redirect(url_for("send_email"))

    return '''
    <form method="POST">
        <label for="recipient">Recipient:</label><br>
        <input type="email" name="recipient" required><br><br>
        <label for="subject">Subject:</label><br>
        <input type="text" name="subject" required><br><br>
        <label for="message">Message:</label><br>
        <textarea name="message" rows="5" required></textarea><br><br>
        <button type="submit">Send Email</button>
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5444)
