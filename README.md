# Lab_AI 1.0

# Adversarial AI Lab (CPU ONLY)

## Overview

This repository contains the resources for setting up and running an Adversarial AI Lab. The lab allows you to experiment with adversarial attacks and defenses using popular libraries and frameworks in machine learning. 

## Goals

- Learn how adversarial attacks work
- Simulate real-world AI red teaming scenarios
- Practice defense and mitigation strategies
- Build a portfolio-ready lab project

## Pre-Installed Frameworks

- Pre-installed Frameworks:
- TensorFlow 2.10 (CPU)
- PyTorch (CPU-only)
- CleverHans, ART, Foolbox, TextAttack
- Flask (for local dashboards)
- JupyterLab (for notebooks)

## Quick Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/AdversarialAI-Lab.git
   cd AdversarialAI-Lab
   ```

2. **Run the Setup Script:**

   The `setup_lab.py` script will handle the environment setup, installation of dependencies, and everything needed to get started.

   ```bash
   python3 setup_lab.py
   ```

   This will:
   - Create a Python 3.10 virtual environment.
   - Install necessary packages including PyTorch (CPU-only), TensorFlow, and additional libraries for adversarial robustness.
   - Install CleverHans directly from GitHub.

3. **Activate the Virtual Environment:**

   Once the setup is complete, activate the virtual environment:

   ```bash
   source venv/bin/activate
   ```

4. **Run the Lab:**

   After activation, you can begin working with the lab! Refer to the `docs/` folder for detailed tutorials, guides, and diagrams on using the lab effectively.

## Folder Structure

- `AdversarialAI-Lab/`
  - `setup_lab.py`: The script that automates the setup process.
  - `requirements.txt`: The list of dependencies for the lab.
  - `docs/`: A folder containing markdown tutorials, lab usage guides, and other resources to help you get the most out of the lab.
  - `attacks/`: Scripts and experiments related to adversarial attacks.
  - `defenses/`: Scripts and experiments related to adversarial defenses.
  - `models/`: Pre-trained models used in the lab experiments.
 
    AdversarialAI_Lab/
│
├── setup_lab.py               # Full environment setup script
├── install.sh                 # Optional manual install shell script
├── requirements.txt           # All dependencies, including CPU-only
├── /docs                      # Tutorials, guides, and visuals
│   ├── usage_guide.md
│   ├── attack_tutorials.md
│   ├── dashboard_plan.md
│   └── diagrams/
│       └── architecture.png
└── /notebooks                 # Sample adversarial attack notebooks


## Usage

- Use the `attacks/` folder to explore adversarial attack methods.
- Use the `defenses/` folder to explore and test defenses against adversarial examples.
- Customize or add new attack/defense methods as you build on the lab.
