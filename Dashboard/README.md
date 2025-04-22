**Setup the AdversarialAI Dashboard
   a. create a folder called "Lab-1.0_Dashboard in the project directory to hold all the files
   ![image](https://github.com/user-attachments/assets/31329325-9bde-4605-b7f7-1ee7c0b89a88)
      -  app.py: This is the main Flask application file. Save it in the project root 
      -  requirements.txt: This will contain all the Python dependencies for the Flask Dashboard. Save it in the project root       
      -  index.html: This will be your HTML template that the user sees. Save it inside the templates/ folder.
      -  styles.css: This file contains the custom CSS for styling the dashboard. Save it inside static/folder.
      -  script.js: save it inside static/folder
   b. activate virtual environment. before  running any script, ensure venv is    activated source venv/bin/activate 
   c. install dependencies pip install -r requirements.txt
   d. run the flas application python app.py
   e. visit the URL and access the dashboard
   f. escap with CTRL+C to end

**Script to locate the venv for Dashboard**
   - save this activate_venv.sh script in the Dashboard/ folder
   - if needed, dos2unix activate_venv.sh
   - make it executable chmod +x activate_venv.sh
   - run it from inside the dashboard/ folder ./activate_venv.sh

**Run the Dashboard**
  - python app.py from the venv
  - visit http://127.0.0.1:5000 in any browser
  - navigate attack simulations from here
