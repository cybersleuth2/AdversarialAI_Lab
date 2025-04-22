# create_lab_structure.py

import os

# Define folder structure and corresponding README content
folders = {
    "datasets": "This folder stores all datasets used for adversarial attacks and training.",
    "models": "This folder contains trained models and model definitions.",
    "notebooks": "This folder includes Jupyter notebooks for interactive experimentation.",
    "scripts": "This folder holds scripts for training, testing, and attacking models.",
    "results": "This folder stores logs, metrics, and attack results.",
    "tools": "This folder is for custom utilities and tools (e.g., data preprocessors, visualizers).",
    "docs": "This folder contains markdown tutorials, diagrams, usage guides, and documentation files.",
    "configs": "This folder stores JSON/YAML config files for experiments or training/attack pipelines."
}

def create_structure(base_path="."):
    for folder, description in folders.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)

        readme_path = os.path.join(folder_path, "README.md")
        if not os.path.exists(readme_path):
            with open(readme_path, "w") as f:
                f.write(f"# {folder}\n\n{description}\n")

    print("[✔] Lab folder structure created with README files.")

if __name__ == "__main__":
    create_structure()
