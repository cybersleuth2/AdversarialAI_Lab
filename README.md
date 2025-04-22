# Lab_AI 1.0

# Adversarial AI Lab (CPU ONLY)

###TO DO: fill the folders while building out the lab modules, experiments, and dashboard. 

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

6. **Setup the Lab1.0_Dashboard
   a. create a folder called "Lab-1.0_Dashboard in the project directory to hold all the files
   ![image](https://github.com/user-attachments/assets/31329325-9bde-4605-b7f7-1ee7c0b89a88)
      -  app.py: This is your main Flask application file. Save it in your project root 
      -  requirements.txt: This will contain all the Python dependencies for your Flask Dashboard. Save it in the project root       
      -  index.html: This will be your HTML template that the user sees. Save it inside the templates/ folder.
      -  styles.css: This file contains the custom CSS for styling your dashboard. Save it inside static/folder.
      -  script.js: save it inside static/folder
   b. activate virtual environment. before  running any script, ensure venv is activated
      source venv/bin/activate 
   c. install dependencies pip install -r requirements.txt
   d. run the flas application python app.py
   e. visit the URL and access the dashboard
   f. escap with CTRL+C to end

8. **Run the Lab:**




## PIP List for CPU-ONLY Lab
└─$ pip list                 
Package                            Version
---------------------------------- --------------
absl-py                            2.2.2
accelerate                         1.6.0
adversarial-robustness-toolbox     1.19.1
aiohappyeyeballs                   2.6.1
aiohttp                            3.11.18
aiosignal                          1.3.2
anyio                              4.9.0
anytree                            2.13.0
argon2-cffi                        23.1.0
argon2-cffi-bindings               21.2.0
arrow                              1.3.0
asttokens                          3.0.0
astunparse                         1.6.3
async-lru                          2.0.5
async-timeout                      5.0.1
attrs                              25.3.0
babel                              2.17.0
beautifulsoup4                     4.13.4
bert-score                         0.3.13
bioc                               2.1
bleach                             6.2.0
blinker                            1.9.0
boto3                              1.37.38
botocore                           1.37.38
cachetools                         5.5.2
certifi                            2025.1.31
cffi                               1.17.1
charset-normalizer                 3.4.1
cleverhans                         4.0.0
click                              8.1.8
cloudpickle                        3.1.1
comm                               0.2.2
conllu                             4.5.3
contourpy                          1.3.2
cycler                             0.12.1
datasets                           3.5.0
debugpy                            1.8.14
decorator                          5.2.1
defusedxml                         0.7.1
Deprecated                         1.2.18
dill                               0.3.8
dm-tree                            0.1.9
docopt                             0.6.2
eagerpy                            0.30.0
easydict                           1.13
editdistance                       0.8.1
exceptiongroup                     1.2.2
executing                          2.2.0
fastjsonschema                     2.21.1
filelock                           3.18.0
flair                              0.15.1
Flask                              3.1.0
flatbuffers                        25.2.10
fonttools                          4.57.0
foolbox                            3.3.4
fqdn                               1.5.1
frozenlist                         1.6.0
fsspec                             2024.12.0
ftfy                               6.3.1
gast                               0.4.0
gdown                              5.2.0
gitdb                              4.0.12
GitPython                          3.1.44
google-auth                        2.39.0
google-auth-oauthlib               0.4.6
google-pasta                       0.2.0
grpcio                             1.71.0
h11                                0.14.0
h5py                               3.13.0
httpcore                           1.0.8
httpx                              0.28.1
huggingface-hub                    0.30.2
idna                               3.10
intervaltree                       3.1.0
ipykernel                          6.29.5
ipython                            8.35.0
isoduration                        20.11.0
itsdangerous                       2.2.0
jedi                               0.19.2
jieba                              0.42.1
Jinja2                             3.1.6
jmespath                           1.0.1
joblib                             1.4.2
json5                              0.12.0
jsonlines                          4.0.0
jsonpointer                        3.0.0
jsonschema                         4.23.0
jsonschema-specifications          2024.10.1
jupyter_client                     8.6.3
jupyter_core                       5.7.2
jupyter-events                     0.12.0
jupyter-lsp                        2.2.5
jupyter_server                     2.15.0
jupyter_server_terminals           0.5.3
jupyterlab                         4.4.0
jupyterlab_pygments                0.3.0
jupyterlab_server                  2.27.3
keras                              2.10.0
Keras-Preprocessing                1.1.2
kiwisolver                         1.4.8
langdetect                         1.0.9
language_tool_python               2.9.3
lemminflect                        0.2.3
libclang                           18.1.1
lru-dict                           1.3.0
lxml                               5.3.2
Markdown                           3.8
MarkupSafe                         3.0.2
matplotlib                         3.10.1
matplotlib-inline                  0.1.7
mistune                            3.1.3
mnist                              0.2.2
more-itertools                     10.6.0
mpld3                              0.5.10
mpmath                             1.3.0
multidict                          6.4.3
multiprocess                       0.70.16
nbclient                           0.10.2
nbconvert                          7.16.6
nbformat                           5.10.4
nest-asyncio                       1.6.0
networkx                           3.4.2
nltk                               3.9.1
nose                               1.3.7
notebook_shim                      0.2.4
num2words                          0.5.14
numpy                              2.2.5
oauthlib                           3.2.2
OpenHowNet                         2.0
opt_einsum                         3.4.0
overrides                          7.7.0
packaging                          25.0
pandas                             2.2.3
pandocfilters                      1.5.1
parso                              0.8.4
pexpect                            4.9.0
pillow                             11.2.1
pinyin                             0.4.0
pip                                25.0.1
platformdirs                       4.3.7
pptree                             3.1
prometheus_client                  0.21.1
prompt_toolkit                     3.0.51
propcache                          0.3.1
protobuf                           3.19.6
psutil                             7.0.0
ptyprocess                         0.7.0
pure_eval                          0.2.3
pyarrow                            19.0.1
pyasn1                             0.6.1
pyasn1_modules                     0.4.2
pycodestyle                        2.13.0
pycparser                          2.22
Pygments                           2.19.1
pyparsing                          3.2.3
PySocks                            1.7.1
python-dateutil                    2.9.0.post0
python-json-logger                 3.3.0
pytorch_revgrad                    0.2.0
pytz                               2025.2
PyYAML                             6.0.2
pyzmq                              26.4.0
referencing                        0.36.2
regex                              2024.11.6
requests                           2.32.3
requests-oauthlib                  2.0.0
rfc3339-validator                  0.1.4
rfc3986-validator                  0.1.1
rpds-py                            0.24.0
rsa                                4.9.1
s3transfer                         0.11.5
safetensors                        0.5.3
scikit-learn                       1.6.1
scipy                              1.15.2
seaborn                            0.13.2
segtok                             1.5.11
Send2Trash                         1.8.3
sentencepiece                      0.2.0
setuptools                         65.5.0
six                                1.17.0
smmap                              5.0.2
sniffio                            1.3.1
sortedcontainers                   2.4.0
soupsieve                          2.7
sqlitedict                         2.1.0
stack-data                         0.6.3
sympy                              1.13.3
tabulate                           0.9.0
tensorboard                        2.10.1
tensorboard-data-server            0.6.1
tensorboard-plugin-wit             1.8.1
tensorflow                         2.10.0
tensorflow-estimator               2.10.0
tensorflow-io-gcs-filesystem       0.37.1
tensorflow-probability             0.25.0
termcolor                          3.0.1
terminado                          0.18.1
terminaltables                     3.1.10
textattack                         0.3.10
threadpoolctl                      3.6.0
tinycss2                           1.4.0
tokenizers                         0.21.1
toml                               0.10.2
tomli                              2.2.1
torch                              2.0.0+cpu
torchaudio                         2.0.0+cpu
torchvision                        0.15.0+cpu
tornado                            6.4.2
tqdm                               4.67.1
traitlets                          5.14.3
transformer-smaller-training-vocab 0.4.1
transformers                       4.51.3
types-python-dateutil              2.9.0.20241206
typing_extensions                  4.13.2
tzdata                             2025.2
uri-template                       1.3.0
urllib3                            2.4.0
wcwidth                            0.2.13
webcolors                          24.11.1
webencodings                       0.5.1
websocket-client                   1.8.0
Werkzeug                           3.1.3
wheel                              0.45.1
Wikipedia-API                      0.8.1
word2number                        1.1
wrapt                              1.17.2
xxhash                             3.5.0
yarl                               1.20.0
                                        
