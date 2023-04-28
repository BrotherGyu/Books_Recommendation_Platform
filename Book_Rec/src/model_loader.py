"""
This module provides a function for loading a pre-trained machine learning model used for generating personalized book recommendations.

Functions:
    predict_model_load(use_category: bool = False) -> Any:
        Loads a pre-trained machine learning model used for generating personalized book recommendations.
        If `use_category` is True, the function loads a model that considers book categories. Otherwise, the function loads a model that does not consider book categories.
        Returns the loaded machine learning model.
        
Parameters:
    - use_category (bool, optional): Whether or not to consider the book category in generating recommendations. Defaults to False.
    
Returns:
    - model (Any): The loaded machine learning model.
    
Dependencies:
    - pickle
    - os
"""

import pickle
import os

def predict_model_load(use_category: bool = False):
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    if use_category:
        print('predict_model_load : use_category - True')
        file_path = os.path.join(current_dir, '..', 'model', 'catboost_model_IALLC.pkl')
        with open(file_path, 'rb') as f:
            model = pickle.load(f)
    
    else:
        print('predict_model_load : use_category - false')
        file_path = os.path.join(current_dir, '..', 'model', 'catboost_model_IALL_.pkl')
        with open(file_path, 'rb') as f:
            model = pickle.load(f)
    return model