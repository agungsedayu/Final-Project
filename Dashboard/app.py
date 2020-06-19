# DARI MAS KIM UNTUK HOME
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
#     <!--Import Google Icon Font-->
#     <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
#     <!--Import materialize.css-->
#     <link type="text/css" rel="stylesheet" href="css/materialize.min.css"  media="screen,projection"/>

#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <script type="text/javascript" src="scripts.js">
# 	</script>
# 	<link rel="stylesheet" href="styles.css">
#     <title>Your Dashboard</title>

# </head>
# <body style="background-image: url({{url_for('static',filename='aa.jpg') }});background-size:cover;">
#     <div class="container-fluid">
#         <center><br>
#             <h2 class="display-4">
#                 <font color="white">
#                     <st

from flask import Flask, render_template, jsonify, request
import joblib
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import json

app = Flask(__name__)

# home route
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/data_visualization')
def data_visualization():
    return render_template('Cluster_datavisualization.html')

@app.route('/dataset')
def dataset():
    return render_template('Cluster_tables.html')

@app.route('/model')
def model():
    return render_template('Cluster_model.html')

if __name__ == '__main__':
    countmatrix = joblib.load('ModelJoblib') 
    df = pd.read_csv('advertisingREADY.csv')
    app.run(debug=True)