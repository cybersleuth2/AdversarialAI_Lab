#!/bin/bash
echo "[*] Setting up Adversarial AI Lab on Kali (CPU-only)..."

# System requirements
sudo apt update && sudo apt full-upgrade -y
sudo apt install -y python3.10 python3.10-venv python3-pip git curl unzip build-essential

# Python virtual environment
python3.10 -m venv venv
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install requirements (with CPU-only PyTorch)
pip install -r requirements.txt -f https://download.pytorch.org/whl/cpu/torch_stable.html

echo "[✔] Setup complete. Activate your environment using: source venv/bin/activate"
