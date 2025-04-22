from flask import Flask
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os
import sys

# Load environment variables from .env file
load_dotenv(override=True)

EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER', EMAIL_USER)
MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
MAIL_PORT = int(os.environ.get('MAIL_PORT', 587))
MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'True').lower() == 'true'

if not EMAIL_USER or not EMAIL_PASSWORD:
    print("ERROR: EMAIL_USER and EMAIL_PASSWORD must be set in your environment or .env file.", file=sys.stderr)
    sys.exit(1)

# Get recipient for test email (use EMAIL_USER if not set)
RECIPIENT = os.environ.get('TEST_RECIPIENT', EMAIL_USER)

app = Flask(__name__)
app.config.update(
    MAIL_SERVER=MAIL_SERVER,
    MAIL_PORT=MAIL_PORT,
    MAIL_USE_TLS=MAIL_USE_TLS,
    MAIL_USERNAME=EMAIL_USER,
    MAIL_PASSWORD=EMAIL_PASSWORD,
    MAIL_DEFAULT_SENDER=MAIL_DEFAULT_SENDER,
)

print("Raw Environment Variables:")
print(f"EMAIL_USER: {EMAIL_USER}")
print(f"MAIL_DEFAULT_SENDER: {MAIL_DEFAULT_SENDER}\n")

print("Email Configuration:")
print(f"MAIL_SERVER: {MAIL_SERVER}")
print(f"MAIL_PORT: {MAIL_PORT}")
print(f"MAIL_USE_TLS: {MAIL_USE_TLS}")
print(f"MAIL_USERNAME: {EMAIL_USER}")
print(f"MAIL_DEFAULT_SENDER: {MAIL_DEFAULT_SENDER}")
print(f"TEST EMAIL RECIPIENT: {RECIPIENT}\n")

mail = Mail(app)

with app.app_context():
    try:
        msg = Message(
            subject='Diffusion Calculator - Test Email',
            sender=('Diffusion Calculator', MAIL_DEFAULT_SENDER),
            recipients=[RECIPIENT],
            body='This is a test email sent to verify that your Diffusion Calculator email configuration is working.',
        )
        mail.send(msg)
        print("Test email sent successfully!")
        sys.exit(0)
    except Exception as e:
        print(f"ERROR: Failed to send email: {e}", file=sys.stderr)
        sys.exit(2)