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

![image](https://github.com/user-attachments/assets/51f5073a-9187-4c07-9eae-0cbc3eac4103)



## Pre-Installed Frameworks


- TensorFlow 2.10 (CPU)
- PyTorch (CPU-only)
- CleverHans, ART, Foolbox, TextAttack
- Flask (for local dashboards)
- JupyterLab (for notebooks)


## Getting Started

1. Create a Virtual Environment within your lab directory: python3.10 venv -m venv venv.
2. Activate the venv:  source venv/bin/activate
3. install required packages: pip install --upgrade pip  AND  pip install -r requirements.txt
4. Setup the lab infra: python3.10 setup_lab.py Use Python 3.10 explicitly to make sure you're using the correct version.
5. The script will:
   - Create /projects/AdversarialAI with subfolders like methods, notebooks, dashboard, data, etc.
   - Write out a requirements.txt file tailored for your CPU-only, PyTorch setup.
   - Create a starter dashboard.py file in the dashboard/ folder.
   - Write a structured README.md.
   - Offer printed confirmation messages in the terminal for each step it completes.
6. Verify the Structure Was Created running the tree command. If tree is not installed, install it with: sudo apt install tree and thentree ~<your path>




## License

TBD

## Author

This project is created by Sonu Kumar using ChatGPT
