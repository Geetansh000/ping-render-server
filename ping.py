import requests
import time
from datetime import datetime

URL = "https://restaurant-app-be-wh3h.onrender.com"  # replace with your actual Render API endpoint

def ping_server():
    try:
        response = requests.get(URL)
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Ping success: {response.status_code}")
    except Exception as e:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Ping failed: {str(e)}")

# Run indefinitely
while True:
    ping_server()
    time.sleep(10 * 60)  # Sleep for 10 minutes
