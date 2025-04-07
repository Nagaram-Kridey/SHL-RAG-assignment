import subprocess
import time
import webbrowser

# Step 1: Start FastAPI server in the background
fastapi_process = subprocess.Popen(["uvicorn", "app.main:app", "--reload"])

# Step 2: Wait for server to start
print("⏳ Starting FastAPI server...")
time.sleep(3)  # You can increase this if needed

# Step 3: Launch Streamlit app
print("🚀 Launching Streamlit UI...")

subprocess.run(["streamlit", "run", "frontend/app.py"])

