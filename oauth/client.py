from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
import os
from dotenv import load_dotenv

load_dotenv()

oauth_id = os.getenv("oauth_id")
oauth_secret = os.getenv("oauth_id")