from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import pandas as pd
import pickle

def classifier(mat, model):
    '''
    Predict using the trained model

    Input:
    -----
        mat : NxM matrix 
        model : the model choice 
    Output:
    ------
        pred : list of predicted labels
    '''
    if model=='SVM':
        model = pickle.load(open("classification_model_SVM.pkl", "rb"))
        pred = model.predict(mat)
        
    elif model=='RF':
        model = pickle.load(open("classification_model_RF.pkl", "rb"))
        pred = model.predict(mat)
        
    elif model=='GBC':
        model = pickle.load(open("classification_model_GBC.pkl", "rb"))
        pred = model.predict(mat)
        
    else:
        raise Exception("Please select one of the three methods : SVM, RF, GBC")
    
    return pred

data = pd.read_csv('data/validation_diabetes_health_indicators.csv')
data['Diabetes_012'] = data['Diabetes_012'].astype(int)

y = data['Diabetes_012']
t = data['NoDocbcCost']

models = ['RF','SVM','GBC']
for model in models:
    if model == 'RF':
        X = data.drop(columns=['Diabetes_012','Unnamed: 0','NoDocbcCost'])
    else:
        X = data.drop(columns=['Diabetes_012','Unnamed: 0'])

    pred = classifier(X, model)

    accuracy = accuracy_score(pred, y)
    f1 = f1_score(pred, y, average='macro', zero_division=True)

    print(f'Model: {model}\n-----\nAccuracy: {accuracy:.2f} \nF1_score: {f1:.2f} \n')
