import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

from user_profile import get_project_paths
paths = get_project_paths()

os.makedirs(paths['data_processed'], exist_ok=True)
os.makedirs(paths['data_outputs'], exist_ok=True)
os.makedirs(paths['report_path'], exist_ok=True)

# Define notebooks in the order they should be executed
notebooks = [
    "notebooks/data_preparation.ipynb",
    "notebooks/data_cleaning_exploration.ipynb",
    "notebooks/merge_and_analysis.ipynb",
    "notebooks/generate_report.ipynb"
]

def run_notebook(path):
    print(f"🔁 Running notebook: {path}")
    with open(path) as f:
        nb = nbformat.read(f, as_version=4)
        ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
        ep.preprocess(nb, {'metadata': {'path': os.path.dirname(path)}})

for nb_path in notebooks:
    run_notebook(nb_path)

print("All notebooks executed successfully!")