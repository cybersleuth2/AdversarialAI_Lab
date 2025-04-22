Move the notebook, if it's not already in the correct labs/fgsm/folder:
mv ~/Downloads/FGSM.ipynb ~/kali/projects/AdversarialAI-Lab/labs/fgsm/

Open your terminal and activate the venv:
source ../../venv/bin/activate

Open JupyterLab in the virtual environment:
jupyter lab

This will open a new browser tab or window (by default: http://localhost:8888/lab).
If it doesn’t open automatically, copy the link from the terminal and paste it into your browser.

Navigate in JupyterLab, in the left sidebar of JupyterLab (which looks like a file explorer):
labs/fgsm/FGSM.ipynb (click on this file)

And open it to start testing FGSM.
- Read through the cells—they’re all commented with instructions and explanation.
- Run each cell one by one by:
- Clicking the cell
- Pressing Shift + Enter (or the ▶️ play button in the toolbar)
  
This will:
- Load data
- Load a small model (CPU only)
- Run FGSM attack
- Show results with interpretations


