import catboost as cb
import pickle
import pandas as pd

from .data_loader import predict_dataframe_load
from .model_loader import predict_model_load

def book_recommend_info(age: int, location_country: int, language: int,
                        use_category:bool = False, category: int = None):
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


## test code
if __name__=='__main__':
    age = 3
    location_country = 1
    language = 0
    use_category = True
    category= 2
    predict_li = book_recommend_info(age, location_country,language,use_category, category)
    print(max(predict_li), min(predict_li))

