import os

import subprocess

import sys

import venv



def create_virtualenv():

    """Create and activate a Python 3.10 virtual environment."""

    print("[+] Creating Python 3.10 virtual environment...")

    venv_dir = "venv"

    if not os.path.exists(venv_dir):

        venv.create(venv_dir, with_pip=True)

        print(f"[+] Virtual environment created in {venv_dir}")

    else:

        print(f"[+] Virtual environment already exists in {venv_dir}")



def activate_virtualenv():

    """Activate the virtual environment."""

    print("[+] Activating virtual environment...")

    activate_script = os.path.join("venv", "bin", "activate_this.py")

    if os.path.exists(activate_script):

        exec(open(activate_script).read(), {'__file__': activate_script})

        print("[+] Virtual environment activated")

    else:

        print("[!] Activation script not found.")



def upgrade_pip():

    """Upgrade pip to the latest version."""

    print("[+] Upgrading pip...")

    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])



def install_requirements():

    """Install dependencies from requirements list."""

    print("[+] Installing dependencies...")



    # CPU-only PyTorch installation

    subprocess.check_call([sys.executable, "-m", "pip", "install", "torch==2.0.0+cpu", "torchvision==0.15.0+cpu", "torchaudio==0.13.0", 

                           "-f", "https://download.pytorch.org/whl/cpu/torch_stable.html"])



    # Additional libraries

    dependencies = [

        "tensorflow==2.10", "keras", "numpy", "pandas", "matplotlib", "scikit-learn", "tqdm", "seaborn", "jupyterlab",

        "adversarial-robustness-toolbox", "foolbox", "textattack", "flask"

    ]

    subprocess.check_call([sys.executable, "-m", "pip", "install"] + dependencies)



    # Install CleverHans from GitHub

    subprocess.check_call([sys.executable, "-m", "pip", "install", "git+https://github.com/cleverhans-lab/cleverhans.git"])



def main():

    create_virtualenv()

    activate_virtualenv()

    upgrade_pip()

    install_requirements()

    print("[✔] Setup complete. Activate your environment using: source venv/bin/activate")



if __name__ == "__main__":

    main()

