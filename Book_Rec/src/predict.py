"""
This module provides a function for generating personalized book recommendations based on user information.

Functions:
    book_recommend_info(age: int, location_country: int, language: int, use_category: bool = False, category: int = None) -> List[float]:
        Generates personalized book recommendations based on the user's age, country of residence, language preference, and book category (optional).
        If `use_category` is True, the function generates recommendations based on both user input and the book category. Otherwise, the function generates recommendations based only on user input.
        Returns a list of predicted ratings for books in the database.
        
Parameters:
    - age (int): The user's age. Must be an integer between 5 and 100 (inclusive).
    - location_country (int): The user's country of residence. Must be an integer corresponding to a country ID in the database.
    - language (int): The user's preferred language. Must be an integer corresponding to a language ID in the database.
    - use_category (bool, optional): Whether or not to consider the book category in generating recommendations. Defaults to False.
    - category (int, optional): The book category to consider in generating recommendations. Required if `use_category` is True.
    
Returns:
    - rating_pred (List[float]): A list of predicted ratings for books in the database. Each element of the list corresponds to a book in the database, and the indices of the elements represent the book IDs.
    
Dependencies:
    - data_loader
    - model_loader
"""

from .data_loader import predict_dataframe_load
from .model_loader import predict_model_load
from typing import List

def book_recommend_info(age: int, location_country: int, language: int,
                        use_category:bool = False, category: int = None) -> List[float]:
    if use_category:
        print('book_recommend_info : use_category - true')
        model = predict_model_load(use_category)
        data = predict_dataframe_load(age, location_country,language,use_category, category)
        rating_pred = model.predict(data)
        return rating_pred
    
    else:
        print('book_recommend_info : use_category - false')
        model = predict_model_load(use_category)
        data = predict_dataframe_load(age, location_country,language, use_category)
        rating_pred = model.predict(data)
        return rating_pred