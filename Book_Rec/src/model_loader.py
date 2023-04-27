import pickle
import os

def predict_model_load(use_category: bool = False):
    
    path = os.getcwd()
    if use_category:
        print('predict_model_load : use_category - True')
        with open(path+'/model/catboost_model_IALLC.pkl', 'rb') as f:
            model = pickle.load(f)
    
    else:
        print('predict_model_load : use_category - false')
        with open(path+'/model/catboost_model_IALL_.pkl', 'rb') as f:
            model = pickle.load(f)
    return model