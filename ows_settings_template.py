from pathlib import Path
import os

# AWS
AWS_BUCKET = "bucketname"
AWS_DYNAMO_REGION = "us-east-1" # Or any other region
AWS_DYNAMO_TABLE = "tablename"

# Spotify
SPOTIFY_CLIENT_ID = os.environ.get("spotify_client_id")
SPOTIFY_CLIENT_SECRET = os.environ.get("spotify_client_secret")

# Templating
WEBSITE_DIRECTORY = Path("/path/to/ourweddingssongs/website")
WEBSITE_INDEX_HTML_OUT = WEBSITE_DIRECTORY / "index.html"
WEBSITE_TEMPLATE_DIRECTORY = WEBSITE_DIRECTORY / "templates"

# Twilio
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_FROM_NUMBER = "+17085555555"
