import os



lab_structure = [

    "dashboard/static/js",

    "dashboard/static/css",

    "dashboard/templates",

    "methods",

    "notebooks",

    "setup"

]



requirements = '''

torch==2.0.1+cpu

torchvision==0.15.2+cpu

torchaudio==2.0.2+cpu

-f https://download.pytorch.org/whl/torch_stable.html



flask

numpy

pandas

matplotlib

scikit-learn

tqdm

seaborn

jupyterlab

adversarial-robustness-toolbox

foolbox

textattack

git+https://github.com/cleverhans-lab/cleverhans.git

'''



readme_content = '''# AdversarialAI Lab



A lightweight, CPU-only adversarial machine learning lab with PyTorch, Flask, and Jupyter integration. Built for experimentation, interpretability, and education.

'''



dashboard_html = '''<!DOCTYPE html>

<html>

<head>

    <title>AdversarialAI Dashboard</title>

    <link rel="stylesheet" href="/static/css/style.css">

</head>

<body>

    <h1>Welcome to the AdversarialAI Dashboard</h1>

    <p>Use the navigation tabs to explore attack methods and tools.</p>

    <script src="/static/js/script.js"></script>

</body>

</html>

'''



style_css = '''body {

    font-family: Arial, sans-serif;

    background-color: #0f0f0f;

    color: #f0f0f0;

    text-align: center;

    padding: 2rem;

}'''



script_js = '''console.log("Dashboard JS loaded");'''



dashboard_py = '''from flask import Flask, render_template



app = Flask(__name__)



@app.route('/')

def home():

    return "AdversarialAI Dashboard is running! Visit http://127.0.0.1:5000"



if __name__ == '__main__':

    app.run(debug=True)

'''



def create_file(path, content):

    with open(path, 'w') as f:

        f.write(content)

    print(f"  Created file: {path}")



def main():

    base_path = os.getcwd()

    print(f"Creating lab structure under {base_path}...")



    for folder in lab_structure:

        full_path = os.path.join(base_path, folder)

        os.makedirs(full_path, exist_ok=True)

        print(f"  Created: {full_path}")



    create_file(os.path.join(base_path, "requirements.txt"), requirements)

    create_file(os.path.join(base_path, "README.md"), readme_content)

    create_file(os.path.join(base_path, "dashboard", "dashboard.py"), dashboard_py)

    create_file(os.path.join(base_path, "dashboard", "templates", "index.html"), dashboard_html)

    create_file(os.path.join(base_path, "dashboard", "static", "css", "style.css"), style_css)

    create_file(os.path.join(base_path, "dashboard", "static", "js", "script.js"), script_js)



    print("\n✅ Lab setup complete. You can now add attack methods and notebooks.")



if __name__ == '__main__':

    main()
    
