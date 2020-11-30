"""Environement variables."""

import os

# SECURITY WARNING: keep the secret key used in production secret!
MAPBOX_API_KEY = os.getenv(
    "MAPBOX_API_KEY ",
    "pk.eyJ1Ijoicm9sLTEiLCJhIjoiY2tncnhvOHZtMGpleTJ4cXdrenN0aGMzYSJ9.DikocYiTLvwfLSvHwD42Hw"
    # "ADD_YOUR_MAPBOX_API_KEY_HERE"
    # "".join([random.choice(string.printable) for _ in range(24)])
)

# SECURITY WARNING: don't run with debug turned on in production!
if os.environ.get("ENV") == "PRODUCTION":
    DEBUG = False
else:
    DEBUG = True
