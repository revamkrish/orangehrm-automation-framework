import os
from dotenv import load_dotenv
# dotenv is a Python library that helps your application read configuration values from a .env file.
# A .env file is a simple text file containing environment variables (configuration values).

load_dotenv() # Performs the loading

ENV = os.getenv("TEST_ENV", "dev").lower() # Reads a specific environment variable

ENVIRONMENTS = {
    "dev": {
        "base_url": "https://katalon-demo-cura.herokuapp.com/"
    },
    "sit": {
        "base_url": "https://katalon-demo-cura.herokuapp.com/"
    },
    "uat": {
        "base_url": "https://katalon-demo-cura.herokuapp.com/"
    }
}

if ENV not in ENVIRONMENTS:
    raise ValueError(f"Invalid environment: {ENV}")

BASE_URL = ENVIRONMENTS[ENV]["base_url"]

USERNAME = os.getenv("CURA_USERNAME")
PASSWORD = os.getenv("CURA_PASSWORD")

if not USERNAME or not PASSWORD:
    raise ValueError("CURA credentials are missing. Check your .env file.")