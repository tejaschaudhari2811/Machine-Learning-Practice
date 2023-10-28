import pandas as pd
import numpy as np
import sklearn
import joblib
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict", methods=["GET","POST"])
def predict():
    if request.method == "POST":
        request.form.get("YearsExperience")
        try:
            exp_year = float(request.form["YearsExperience"])
            pred_arr = np.array(exp_year)
            preds = pred_arr.reshape(-1,1)
            model = open("DeploymentWeb\linear_regression_model.pkl","rb")
            lr_model = joblib.load(model)
            model_prediction = lr_model.predict(preds)
            model_prediction = round(model_prediction[0][0],2)
        except ValueError:
            return "Please enter valid values"
        
    return render_template("predict.html", prediction=model_prediction)

if __name__=="__main__":
    app.run(debug=True)
