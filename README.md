# Adversarial AI Lab (CPU ONLY)

## Overview

This repository contains the resources for setting up and running an out-of-the-box Adversarial AI Lab. The lab facilitates experimentation with adversarial attacks using popular libraries and frameworks in machine learning.

## disclaimer

This lab is for educational purposes only.  Also, please use at your own risk! We are not responsible for supply chain risks associated with open-source requirements for this lab. Always follow best security practices.

## Adversarial AI Dashboard v Notebook
This lab has an integrated testing notebook as well as a testing dashboard

 **Notebooks**: Step-by-step, interactive tutorials for learning, testing, and iterating. Use the Notebook when:
   - You're learning or experimenting.
   - You want to follow each step manually.
   - You’re reviewing or debugging results.
   - You want fine control over attack parameters and code.
     
**Dashboard**: Visual front-end for quick access, running attacks, uploading models/data. Use the Dashboard when:
   - You want a simple UI for testing without coding.
   - You want to upload models or data and run attacks.
   - You’re demonstrating your lab or showing others.
   - You want to keep everything light and unified in a browser.


## Lab Diretory Structure

![image](https://github.com/user-attachments/assets/4f1c37b8-937c-4cd7-880f-40cfedd0eb3c)



## Pre-Installed Frameworks


- TensorFlow 2.10 (CPU)
- PyTorch (CPU-only)
- CleverHans, ART, Foolbox, TextAttack
- Flask (for local dashboards)
- JupyterLab (for notebooks)


## Getting Started

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/AdversarialAI-Lab.git
   cd AdversarialAI-Lab
   ```

2. **Run the Setup Script:**

   The `setup_lab.py` script will handle the environment setup, installation of dependencies, and everything needed to get started.
   This may take 2-5 minutes depending on your system.
   
   ```bash
   python3 setup_lab.py
   ```

   This will:
   - Create a Python 3.10 virtual environment.
   - Install necessary packages including PyTorch (CPU-only), TensorFlow, and additional libraries for adversarial robustness.
   - Install CleverHans directly from GitHub.
   ![image](https://github.com/user-attachments/assets/39c2d671-9114-49ce-8ace-8e88f056d7ba)

4. **Activate the Virtual Environment:**

   Once the setup is complete, activate the virtual environment:

   ```bash
   source venv/bin/activate
   ```
   ![image](https://github.com/user-attachments/assets/587c9115-63fa-479c-b409-94a44cae3bd4)

   NOTE: the setup_lab.py already ran the requirements.txt file, however, the file is included in this repo as refernce and for         future updates:  pip install -r requirements.txt and if that doesn't work then: pip install torch==2.0.0+cpu 
   torchvision==0.15.0+cpu    torchaudio==2.0.0+cpu \ -f https://download.pytorch.org/whl/cpu/torch_stable.html   --> This is 
   needed because CPU-only versions aren’t on the default PyPI index.

5. **Auto-Create the Lab Structure**
   Save it as create_lab_structure.py in your project root.  Run it from your terminal. This will neatly generate your folders, each    with a simple README to keep things organized:    python3 create_lab_structure.py
   ![image](https://github.com/user-attachments/assets/1390c5b1-4441-4901-a8dd-c7bc89d887a4)

6. See the folder for how to create the Adversarial AI Dashboard
7. **Run the Attack Simulations:**


## License

TBD

## Author

This project is created by Sonu Kumar using ChatGPT
