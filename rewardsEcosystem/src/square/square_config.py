from square.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

def get_square_client():
    access_token = os.getenv("SANDBOX_ACCESS_TOKEN")
    client = Client(access_token=access_token, environment='sandbox')
    return client
