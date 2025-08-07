#!/usr/bin/env python3
"""
Notebook Conversion Script: Google Drive to Borealis Data Access
Converts Jupyter notebooks from using Google Drive mounting to Borealis data repository access.
"""

import json
import os
import shutil
from pathlib import Path

# Borealis boilerplate code
BOREALIS_CODE = '''# Borealis API configuration
import requests
import zipfile

BOREALIS_SERVER = "https://borealisdata.ca"

def get_public_dataset_info(persistent_id):
    """
    Get information about a public dataset
    """
    url = f"{BOREALIS_SERVER}/api/datasets/:persistentId/"
    params = {"persistentId": persistent_id}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        dataset_info = response.json()
    else:
        print(f"Cannot access dataset: {response.status_code}")
        return None
    """
    Get a list of files in a public dataset
    """
    # Access the list of files from the dataset_info dictionary
    files_list = dataset_info['data']['latestVersion']['files']

    # Create an empty list to store file information
    file_info_list = []

    # Iterate through the files list and append file ID and filename to the list
    for file_info in files_list:
        file_id = file_info['dataFile']['id']
        filename = file_info['dataFile']['filename']
        file_info_list.append({"file_id": file_id, "filename": filename})

    return file_info_list

def download_public_file(file_id, save_path="./"):
    """
    Download a specific public file from a dataset by its file ID
    No authentication required
    """
    url = f"{BOREALIS_SERVER}/api/access/datafile/{file_id}"

    response = requests.get(url, stream=True)

    if response.status_code == 200:
        # Determine filename from headers or URL
        filename = None
        if "Content-Disposition" in response.headers:
            cd = response.headers["Content-Disposition"]
            # Try to extract filename from content disposition
            if "filename=" in cd:
                filename = cd.split("filename=")[1].strip('"')

        # Fallback to extracting from URL if header not available or malformed
        if not filename:
             filename = url.split("/")[-1]

        file_path = f"{save_path}/{filename}"

        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        print(f"SUCCESS: File downloaded to {file_path}")
        return file_path
    else:
        print(f"ERROR: {response.status_code}: File may be restricted or not found")
        return None

def is_zip_file(filepath):
    """
    Checks if a file is a valid zip file.
    """
    return zipfile.is_zipfile(filepath)

def unzip_file(filepath, extract_path="./"):
    """
    Unzips a zip file to a specified path and returns the name of the top-level extracted folder.
    Returns None if not a zip file or extraction fails.
    """
    if is_zip_file(filepath):
        try:
            with zipfile.ZipFile(filepath, 'r') as zip_ref:
                # Get the name of the top-level directory within the zip
                # Assumes there is a single top-level directory
                top_level_folder = None
                for file_info in zip_ref.infolist():
                    parts = file_info.filename.split('/')
                    if parts[0] and len(parts) > 1:
                        top_level_folder = parts[0]
                        break # Assuming the first entry gives the top-level folder

                zip_ref.extractall(extract_path)
                print(f"SUCCESS: Successfully unzipped {filepath} to {extract_path}")
                return top_level_folder

        except Exception as e:
            print(f"ERROR: Error unzipping {filepath}: {e}")
            return None
    else:
        print(f"INFO: {filepath} is not a valid zip file.")
        return None

# Initialize Borealis dataset access
public_doi = "doi:10.5683/SP3/H3HGWF"
print("Borealis dataset initialized for animal notebook data.")'''

# File mapping for Borealis dataset
BOREALIS_FILES = {
    '100grid-sample-images.zip': 965307,
    '4370-entire-subset.zip': 965304,
    'cat-100.zip': 965303,
    'close-encounters.zip': 965308,
    'combined_animals.xlsx': 965305,
    'dataset-sizes.zip': 965306,
    'deer_100.zip': 965302
}

def convert_notebook_paths(notebook_path):
    """
    Convert Google Drive paths to local Borealis paths in a notebook.
    """
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    path_mappings = {
        '/content/drive/MyDrive/shared-data/Notebook datafiles/': './',
        '/content/drive/My Drive/shared-data/Notebook datafiles/': './',
        '/content/drive/MyDrive/shared-data/': './',
        '/content/drive/My Drive/shared-data/': './',
        '/content/drive/': './',
    }
    
    # Process each cell
    for cell in notebook['cells']:
        if cell['cell_type'] == 'code':
            # Check if cell contains Google Drive mounting
            source_lines = cell['source']
            if isinstance(source_lines, str):
                source_lines = [source_lines]
            
            # Replace Google Drive mounting with Borealis code
            new_source = []
            skip_mount = False
            
            for line in source_lines:
                # Skip Google Drive mounting lines
                if 'from google.colab import drive' in line or 'drive.mount(' in line:
                    if not skip_mount:
                        # Replace with Borealis code on first occurrence
                        new_source.append(BOREALIS_CODE)
                        skip_mount = True
                    continue
                
                # Replace file paths
                for old_path, new_path in path_mappings.items():
                    if old_path in line:
                        line = line.replace(old_path, new_path)
                
                new_source.append(line)
            
            cell['source'] = new_source
    
    # Save converted notebook
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=2)
    
    return True

def convert_all_notebooks(test_dir):
    """
    Convert all notebooks in the test directory.
    """
    converted_notebooks = []
    errors = []
    
    for root, dirs, files in os.walk(test_dir):
        for file in files:
            if file.endswith('.ipynb'):
                notebook_path = os.path.join(root, file)
                try:
                    convert_notebook_paths(notebook_path)
                    converted_notebooks.append(notebook_path)
                    print(f"SUCCESS: Converted: {notebook_path}")
                except Exception as e:
                    errors.append(f"ERROR: Failed to convert {notebook_path}: {str(e)}")
                    print(f"ERROR: Failed to convert {notebook_path}: {str(e)}")
    
    return converted_notebooks, errors

if __name__ == "__main__":
    test_directory = r"C:\Users\aless\OneDrive\Documents\uraprojects\public-experiments\jupyter-notebooks-test"
    converted, errors = convert_all_notebooks(test_directory)
    
    print(f"\nCONVERSION SUMMARY:")
    print(f"SUCCESS: Successfully converted: {len(converted)} notebooks")
    print(f"ERRORS: {len(errors)} notebooks")
    
    if converted:
        print("\nCONVERTED NOTEBOOKS:")
        for notebook in converted:
            print(f"  - {notebook}")
    
    if errors:
        print("\nERRORS:")
        for error in errors:
            print(f"  - {error}")