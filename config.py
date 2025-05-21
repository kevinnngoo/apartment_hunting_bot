import os
from dotenv import load_dotenv

load_dotenv()

MAX_RENT = int(os.getenv("MAX_RENT", 1500))
MIN_BEDROOMS = int(os.getenv("MIN_BEDROOMS", 2))
EMAIL_TO = os.getenv("EMAIL_TO")
EMAIL_FROM = os.getenv("EMAIL_FROM")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", 465))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")