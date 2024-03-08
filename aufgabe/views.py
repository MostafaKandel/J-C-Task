from django.shortcuts import render
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import requests,json
from django.http import JsonResponse





def index(request):
    '''
    usage: used for main html page for card and display the graph(x,y) and render the graph to Html file  
    '''
    link = 'http://localhost:8000/data' 
   # get the data from the link
    response=requests.get(link)
    # convert the response to json
    responsetwo=response.json()
    json_data=responsetwo
    # Load JSON data
    data = json.loads(json_data)

    # Extract x and y values
    x_values = [entry["a"] for entry in data]
    y_values = [entry["b"] for entry in data]

    # Create plot
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_values, y=y_values, mode='markers', name='Data'))

    # Update layout if needed
    fig.update_layout(title='Plot of a vs b', xaxis_title='a', yaxis_title='b')

    # Convert plot to HTML
    plot_html = fig.to_html(full_html=False, include_plotlyjs='cdn')

    return render(request, 'aufgabe/index.html', {'plot_html': plot_html})
    


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


