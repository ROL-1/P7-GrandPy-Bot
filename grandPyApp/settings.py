"""Environement variables."""

import os

# SECURITY WARNING: keep the secret key used in production secret!
MAPBOX_API_KEY = os.getenv(
    "MAPBOX_API_KEY ", #"ADD_YOUR_MAPBOX_API_KEY_HERE"
)

# SECURITY WARNING: don't run with debug turned on in production!
if os.environ.get("ENV") == "PRODUCTION":
    DEBUG = False
else:
    DEBUG = True
