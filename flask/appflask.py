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
    return render_template('visualisasi.html')

@app.route('/dataset')
def dataset():
    return render_template('dataset.html')

@app.route('/model')
def model():
    return render_template('predict.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    countmatrix = joblib.load('ModelJoblib') 
    df = pd.read_csv('advertising.csv')
    app.run(debug=True)