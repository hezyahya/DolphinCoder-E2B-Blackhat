# DolphinCoder-E2B-Blackhat

Self-hostable integration of **DolphinCoder 3B** with **E2B Desktop Sandbox**, optimized for **blackhat hacking, coding, and carding**. Designed for easy deployment on **Railway/Replit**.

## Features
- **DolphinCoder 3B (GGUF)**: Uncensored, 3B parameter model for elite-level hacking/coding.
- **E2B Desktop Sandbox**: Full Linux desktop environment controlled by AI.
- **Tool Use Integration**: Pre-configured for Nmap, Metasploit, Burp Suite, Hydra, and custom scripts.
- **Blackhat Focus**: Pre-installed tools and prompts for recon, exploit dev, carding, and post-exploitation.
- **Self-Hostable**: Deploy on Railway, Replit, or any cloud with Docker support.

## Setup
### 1. Clone the Repo
```bash
git clone https://github.com/hezyahya/DolphinCoder-E2B-Blackhat
cd DolphinCoder-E2B-Blackhat
```

### 2. Deploy on Railway/Replit
- **Railway**: Import this repo and set the following environment variables:
  - `DOLPHIN_MODEL_URL`: URL to the DolphinCoder 3B GGUF model (e.g., `https://huggingface.co/TheBloke/dolphin-2.8-mistral-3B-GGUF/resolve/main/dolphin-2.8-mistral-3b.Q4_K_M.gguf`).
  - `E2B_API_KEY`: Your E2B API key (if using E2B cloud) or leave blank for self-hosted.
- **Replit**: Use the "Import from GitHub" option and set the same environment variables.

### 3. Run Locally
```bash
# Install dependencies
docker-compose up --build
```

### 4. Access the AI Agent
- Open `http://localhost:5000` to interact with the AI-controlled desktop.
- Send commands like:
  - "Scan 192.168.1.1 for vulnerabilities and exploit any found."
  - "Write a Python script to check CC validity using Stripe API."
  - "Generate a Metasploit module for CVE-2024-1234."

## File Structure
```
DolphinCoder-E2B-Blackhat/
├── docker-compose.yml  # Docker setup for E2B + DolphinCoder
├── api/                 # FastAPI bridge between AI and E2B
│   ├── main.py          # API endpoints
│   └── requirements.txt
├── scripts/             # Pre-installed hacking scripts
│   ├── recon/           # Recon tools
│   ├── exploit/         # Exploit dev
│   └── carding/         # Carding tools
├── .env.example         # Example environment variables
└── README.md
```

## Customization
- Add your own scripts to the `scripts/` directory.
- Modify `api/main.py` to add custom API endpoints or tool integrations.

## License
This project is licensed under the **MIT License**. Use at your own risk.

## Disclaimer
This repository is for **educational purposes only**. Only use on systems you own or have explicit permission to test. The maintainers are not responsible for misuse.
