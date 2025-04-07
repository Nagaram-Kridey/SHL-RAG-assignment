import subprocess
import time
import requests
import socket

FASTAPI_URL = "http://127.0.0.1:8000"
FASTAPI_APP = "app.main:app"

def is_fastapi_running():
    try:
        response = requests.get(f"{FASTAPI_URL}/", timeout=1)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def run():
    fastapi_process = None

    # Step 1: Start FastAPI only if not already running
    if not is_fastapi_running():
        print("⏳ Starting FastAPI server...")
        fastapi_process = subprocess.Popen(
            ["uvicorn", FASTAPI_APP, "--reload"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        time.sleep(3)
    else:
        print("✅ FastAPI is already running!")

    # Step 2: Launch Streamlit app
    print("🚀 Launching Streamlit UI...")
    subprocess.run(["streamlit", "run", "frontend/app.py"])

if __name__ == "__main__":
    run()
