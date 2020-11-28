"""Environement variables."""

import os

# SECURITY WARNING: keep the secret key used in production secret!
MAPBOX_API_KEY = os.getenv(
    "MAPBOX_API_KEY ",
    "pk.eyJ1Ijoicm9sLTEiLCJhIjoiY2tncnhvOHZtMGpleTJ4cXdrenN0aGMzYSJ9.DikocYiTLvwfLSvHwD42Hw",
)
# TC REMOVE KEY

# SECURITY WARNING: don't run with debug turned on in production!
if os.environ.get("ENV") == "PRODUCTION":
    DEBUG = False
else:
    DEBUG = True

# https://openclassrooms.com/fr/courses/4425076-decouvrez-le-framework-django/4632636-deployez-une-application-sur-heroku
