#!/usr/bin/env python3



import os

import subprocess

import sys



def run(command):

    print(f"[+] Running: {command}")

    subprocess.check_call(command, shell=True, executable='/bin/bash')



def main():

    venv_path = "./venv"

    python_bin = f"{venv_path}/bin/python"

    pip_bin = f"{venv_path}/bin/pip"



    # Step 1: Create virtual environment if not exists

    if not os.path.exists(venv_path):

        print("[+] Creating Python 3.10 virtual environment...")

        run("python3.10 -m venv venv")

    else:

        print("[+] Virtual environment already exists in venv")



    # Step 2: Upgrade pip

    print("[+] Upgrading pip...")

    run(f"{pip_bin} install --upgrade pip")



    # Step 3: Install CPU-only PyTorch, torchvision, torchaudio

    print("[+] Installing CPU-only PyTorch, torchvision, torchaudio...")

    run(

        f"{pip_bin} install torch==2.0.0+cpu torchvision==0.15.0+cpu torchaudio==2.0.0+cpu "

        "-f https://download.pytorch.org/whl/cpu/torch_stable.html"

    )



    # Step 4: Install other Python packages

    print("[+] Installing other required packages...")

    run(

        f"{pip_bin} install tensorflow==2.10 keras numpy pandas matplotlib "

        "scikit-learn tqdm seaborn jupyterlab adversarial-robustness-toolbox "

        "foolbox textattack flask"

    )



    # Step 5: Install CleverHans from GitHub

    print("[+] Installing CleverHans from GitHub...")

    run(f"{pip_bin} install git+https://github.com/cleverhans-lab/cleverhans.git")



    print("[✔] Setup complete. Activate your environment using: source venv/bin/activate")



if __name__ == "__main__":

    main()

