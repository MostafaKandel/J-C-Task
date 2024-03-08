from django.shortcuts import render
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import requests,json
from django.http import JsonResponse



def index(request):
    return render(request, 'aufgabe/index.html')
    

def get_df(request):
    '''
    usage: this function is used to return json data from data frame which is two columns and 1000 rows
    returns: json data
    '''
    # create the random numbers for column a
    random_numbers = np.random.randint(0, 101, size=1000)
    #create column b
    column_b = random_numbers % 10
    # Create DataFrame
    df = pd.DataFrame({'a': random_numbers, 'b': column_b})
    # Convert DataFrame to JSON
    data_json = df.to_json(orient='records')
    # Return the JSON response
    return JsonResponse(data_json, safe=False)


    '''
    usage: this function is used to return json data from data frame which is two columns and 1000 rows
    returns: json data
    '''
    # create the random numbers for column a
    random_numbers = np.random.randint(0, 101, size=1000)
    #create column b
    column_b = random_numbers % 10
    # Create DataFrame
    df = pd.DataFrame({'a': random_numbers, 'b': column_b})
    # Convert DataFrame to JSON
    data_json = df.to_json(orient='records')
    # Return the JSON response
    return JsonResponse(data_json, safe=False)


