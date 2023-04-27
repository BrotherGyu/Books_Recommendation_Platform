import pandas as pd
import pickle
import os

def info_data_load():
    path = os.getcwd()
    with open(path+'/data/info2idx_convert_data.pkl', 'rb') as f:
        data = pickle.load(f)
    with open(path+'/data/idx2info.pkl', 'rb') as f:
        idx2info = pickle.load(f)

    country = data['country']
    language = data['language']
    language_fullname = data['language_fullname']
    category = data['category']
    return country, language, language_fullname, category, idx2info
