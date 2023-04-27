import pandas as pd
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
