import subprocess
import time
import webbrowser

# Step 1: Start FastAPI server in the background
fastapi_process = subprocess.Popen(["uvicorn", "app.main:app", "--reload"])

# Step 3: Launch Streamlit app
print("🚀 Launching Streamlit UI...")

subprocess.run(["streamlit", "run", "frontend/app.py"])

