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