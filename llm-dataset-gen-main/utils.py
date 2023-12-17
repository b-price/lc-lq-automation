from typing import List
import os
import pandas as pd

def create_and_save_empty_dataset(columns: List[str], filepath: str) -> None:
    """
    Creates an empty Pandas DataFrame with specified columns and saves it in a file format based on the file extension in the given filepath.
    """
    
    # Extracting the file extension from the filepath
    _, file_extension = os.path.splitext(filepath)
    file_extension = file_extension[1:]

    # Deictionary to map file extensions to corresponding Pandas methods
    file_extensions = {
        'csv': {'method': 'to_csv', 'kwargs': {'index': False}},
    }

    if file_extension not in file_extensions:
        supported_filetypes = ", ".join(file_extensions.keys())
        raise ValueError(f"Unsupported file extension: {file_extension}. Supported file extensions: {supported_filetypes}")

    method_info = file_extensions[file_extension]
    empty_dataset = pd.DataFrame(columns=columns)
    method = getattr(empty_dataset, method_info['method'])
    method(filepath, **method_info['kwargs'])
