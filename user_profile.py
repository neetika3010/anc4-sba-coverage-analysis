import os
import pandas as pd

def get_project_paths():
    """
    Returns a dictionary of absolute paths used across the project.
    """
    base_path = os.path.dirname(os.path.abspath(__file__))

    return {
        'base': base_path,
        'data_raw': os.path.join(base_path, 'data', 'raw'),
        'data_processed': os.path.join(base_path, 'data', 'processed'),
        'data_outputs': os.path.join(base_path, 'data', 'outputs'),
        'report_path': os.path.join(base_path, 'report'),
        'template_path':  os.path.join(base_path, 'templates')
    }

def load_file(filepath, sheet_name=None, header_row=None):
    ext = os.path.splitext(filepath)[-1].lower()

    if ext in ['.xlsx', '.xls']:
        return pd.read_excel(filepath, sheet_name=sheet_name, header=header_row)
    elif ext == '.csv':
        return pd.read_csv(filepath)
    else:
        raise ValueError("Unsupported file format")
