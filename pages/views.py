from django.shortcuts import render
import numpy as np
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Create your views here.
def homeView(request):
    return render(request,'pages/welcome_page.html',{})

def analyseResult(request):
    
    if request.method == 'POST':
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        cpt = request.POST.get('cpt')
        trest_bps = request.POST.get('trestbps')
        chol = request.POST.get('chol')
        fbs = request.POST.get('fbs')
        rest_ecg = request.POST.get('rest-ecg')
        thalach = request.POST.get('thalach')
        exang = request.POST.get('exang')
        old_peak = request.POST.get('old_peak')
        slope = request.POST.get('slope')
        ca = request.POST.get('ca')
        th_def_type = request.POST.get('thal')

        
        heart_data = pd.read_csv('heart_disease_data.csv')
        X = heart_data.drop(columns='target',axis=1)
        y = heart_data['target']
        X_train , X_test , y_train , y_test = train_test_split(X,y,test_size=0.2 , stratify=y , random_state=2)
        dataset_details = [age , sex , cpt , trest_bps , chol , fbs, rest_ecg , thalach , exang , old_peak , slope , ca , th_def_type ]

        model = LogisticRegression()
        model.fit(X_train , y_train)

        input_data = dataset_details

        # change the input data to a numpy array

        input_data_as_numpy_array = np.asarray(input_data)

        # reshape the np array as we are predicting for only one instance
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

        prediction = model.predict(input_data_reshaped)
        predict_disease(prediction[0])

        def predict_disease(pred):
            if(pred == 0):
                st = 'The person doesn\'t have heart disease'
                return render(request,'pages/results.html',{'has_disease':st})
            else:
                st = 'The person has a heart disease'
                return render(request,'pages/results.html',{'has_disease':st})

    
    return render(request,'pages/analyse.html',{})

def resultsPage(request):
    return render(request,'pages/results.html',{})