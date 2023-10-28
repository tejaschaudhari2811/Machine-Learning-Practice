import pandas as pd
import numpy as np
import sklearn
import joblib
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    pass

