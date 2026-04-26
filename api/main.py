# FastAPI bridge between DolphinCoder 3B and E2B Desktop

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import requests
import subprocess
import os

app = FastAPI()

# CORS for Railway/Replit
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load DolphinCoder 3B model (GGUF)
DOLPHIN_API_URL = os.getenv("DOLPHIN_API_URL", "http://localhost:8080/completion")

@app.post("/execute")
async def execute(request: Request):
    data = await request.json()
    task = data.get("task", "")
    
    # Step 1: Ask DolphinCoder for the command
    ai_command = ask_dolphin(f"Blackhat task: {task}. Write the exact Linux command or script. Return only the command.")
    
    # Step 2: Execute in E2B sandbox
    output = run_in_sandbox(ai_command)
    
    return {"command": ai_command, "output": output}

def ask_dolphin(prompt: str) -> str:
    response = requests.post(
        DOLPHIN_API_URL,
        json={
            "prompt": prompt,
            "n_predict": 1024,
            "temperature": 0.3
        }
    ).json()
    return response.get("content", "").strip()

def run_in_sandbox(command: str) -> str:
    # For self-hosted E2B:
    try:
        result = subprocess.run(
            ["docker", "exec", "e2b-desktop", "bash", "-c", command],
            capture_output=True,
            text=True,
            timeout=60
        )
        return result.stdout
    except Exception as e:
        return f"Error: {str(e)}"

@app.get("/")
async def root():
    return {"status": "ready", "message": "DolphinCoder-E2B-Blackhat API"}
