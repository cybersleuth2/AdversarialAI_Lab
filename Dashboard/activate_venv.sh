#!/bin/bash

# Automatically finds and activates the nearest venv folder in parent directories

echo "[+] Looking for virtual environment..."

MAX_DEPTH=3
current_path=$(pwd)

for i in $(seq 1 $MAX_DEPTH); do
    if [ -d "$current_path/venv/bin" ]; then
        echo "[✔] Found venv at: $current_path/venv"
        source "$current_path/venv/bin/activate"
        echo "[✔] Virtual environment activated."
        exit 0
    fi
    current_path=$(dirname "$current_path")
done

echo "[!] Could not find a virtual environment within $MAX_DEPTH levels."
exit 1
