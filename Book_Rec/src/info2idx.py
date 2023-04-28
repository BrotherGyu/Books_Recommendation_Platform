"""
This module provides a function for loading the necessary data used by the recommender system.

Functions:
    info_data_load() -> Tuple[Dict[str, int], Dict[str, int], Dict[str, str], Dict[str, int], Dict[int, Tuple[str, str, int, str]]]:
        Loads the necessary data used by the recommender system.

Returns:
    - country (Dict[str, int]): A dictionary mapping country names to their corresponding IDs in the database.
    - language (Dict[str, int]): A dictionary mapping language names to their corresponding IDs in the database.
    - language_fullname (Dict[str, str]): A dictionary mapping language to their corresponding full names in the database.
    - category (Dict[str, int]): A dictionary mapping book category names to their corresponding IDs in the database.
    - idx2info (Dict[int, Tuple[str, str, int, str]]): A dictionary mapping book IDs to their corresponding information (title, author, year of publication, and URL).
    
Dependencies:
    - pickle
    - os
"""

import pickle
import os

def info_data_load():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, '..', 'data', 'info2idx_convert_data.pkl')
    with open(file_path, 'rb') as f:
        data = pickle.load(f)
    file_path = os.path.join(current_dir, '..', 'data', 'idx2info.pkl')
    with open(file_path, 'rb') as f:
        idx2info = pickle.load(f)

    country = data['country']
    language = data['language']
    language_fullname = data['language_fullname']
    category = data['category']
    return country, language, language_fullname, category, idx2info
