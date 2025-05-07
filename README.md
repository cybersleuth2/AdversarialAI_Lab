**A WORK IN PROGRESS**

# Adversarial AI Lab (CPU ONLY)

## Overview

This repository contains the resources for setting up and running an out-of-the-box Adversarial AI Lab for **CPU ONLY**. The lab facilitates experimentation with adversarial attacks using popular libraries and frameworks in machine learning.


## Adversarial AI Dashboard v Notebook
This lab has an integrated testing notebook as well as a testing dashboard

 **Use the Notebooks** for step-by-step, interactive tutorials for learning, testing, and iterating:
   - learning or experimenting.
   - following each step manually.
   - reviewing or debugging results.
   - fine control over attack parameters and code.
     
**Use the Dashboard** for visual front-end for quick access, running attacks, uploading models/data:
   - simple UI for testing without coding.
   - upload models or data and run attacks.
   - keep everything light and unified in a browser.


## Lab Diretory Structure

![image](https://github.com/user-attachments/assets/457ca8de-6cb2-4fc3-a90c-14761d9300fe)



## Getting Started

1. Create a Virtual Environment within your lab directory: python3.10 -m venv venv.
2. Activate the venv:  source venv/bin/activate
3. install required packages: pip install --upgrade pip  
4. Setup the lab infra: python3.10 setup_lab.py Use Python 3.10 explicitly to make sure you're using the correct version. The script will:
   - Create /projects/AdversarialAI with subfolders like methods, notebooks, dashboard, data, etc.
   - Write out a requirements.txt file tailored for your CPU-only, PyTorch setup.
   - Create a starter dashboard.py file in the dashboard/ folder.
   - Write a structured README.md.
   - Offer printed confirmation messages in the terminal for each step it completes.
6. Run pip install -r requirements.txt
7. Verify the Structure Was Created running the tree command. If tree is not installed, install it with: sudo apt install tree and thentree ~<your path>
8. To setup the AdversarialAI Dashboard, navigate to the dashboard folder from within venv THEN pip install flask THEN python3 dashboard/dashboard.py and THEN  visit http://127.0.0.1:5000  **Dashboard GUI In Proress**


## Disclaimer

This lab is for educational purposes only.  Also, please use at your own risk! We are not responsible for supply chain risks associated with open-source requirements for this lab. Always follow best security practices.


## License

TBD

## Author

This project is created by Sonu Kumar using ChatGPT.


# **LABS** 
## FGSM

