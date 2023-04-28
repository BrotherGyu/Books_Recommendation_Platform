"""
This module provides a function for generating a pandas DataFrame containing user information used by the recommender system.

Functions:
    predict_dataframe_load(age: int, location_country: int, language: int, use_category: bool = False, category: int = None) -> pd.DataFrame:
        Generates a pandas DataFrame containing user information used by the recommender system.
        If `use_category` is True, the function generates a DataFrame with an additional column for book categories.
        Otherwise, the function generates a DataFrame without the book category column.
        Returns the generated pandas DataFrame.
        
Parameters:
    - age (int): The user's age. Must be an integer between 5 and 100 (inclusive).
    - location_country (int): The user's country of residence. Must be an integer corresponding to a country ID in the database.
    - language (int): The user's preferred language. Must be an integer corresponding to a language ID in the database.
    - use_category (bool, optional): Whether or not to consider the book category in generating recommendations. Defaults to False.
    - category (int, optional): The book category to consider in generating recommendations. Required if `use_category` is True.
    
Returns:
    - data (pd.DataFrame): A pandas DataFrame containing the user information for each book in the database. The DataFrame has the following columns:
        - isbn (int): The book ID.
        - age (int): The user's age.
        - location_country (int): The user's country of residence.
        - language (int): The user's preferred language.
        - category (int, optional): The book category to consider in generating recommendations. Only present if `use_category` is True.
    
Dependencies:
    - pandas
    - os
"""

import pandas as pd
import os


def predict_dataframe_load(age: int, location_country: int, language: int,
                           use_category: bool= False, category: int = None) -> pd.DataFrame:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, '..', 'data', 'idx2info.pkl')
    idx2info = pd.read_pickle(file_path)
    
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