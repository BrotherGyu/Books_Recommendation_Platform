import pandas as pd
import os


def predict_dataframe_load(age: int, location_country: int, language: int,
                           use_category: bool= False, category: int = None) -> pd.DataFrame:
    path = os.getcwd()
    idx2info = pd.read_pickle(path+'/data/idx2info.pkl')
    len_idx2info = len(idx2info)

    if use_category:
        print('predict_dataframe_load : use_category - true')
        data = {
            'isbn': [i for i in range(len_idx2info)],
            'age': [age] * len_idx2info,
            'location_country': [location_country] * len_idx2info,
            'category': [category] * len_idx2info,
            'language': [language] * len_idx2info
        }
        return pd.DataFrame(data)

    else:
        print('predict_dataframe_load : use_category - false')
        data = {
            'isbn': [i for i in range(len_idx2info)],
            'age': [age] * len_idx2info,
            'location_country': [location_country] * len_idx2info,
            'language': [language] * len_idx2info
        }
        return pd.DataFrame(data)