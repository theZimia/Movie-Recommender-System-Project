import pickle
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/')
def home():
    return "movie recommendation system"

@app.route('/predict', methods=['POST'])
def predict():

