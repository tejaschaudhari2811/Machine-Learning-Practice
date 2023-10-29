import pandas as pd
import numpy as np
import joblib
import streamlit

model = open("DeploymentWeb\linear_regression_model.pkl", "rb")
lr_model = joblib.load(model)

def lr_prediction(years_of_experience):
    if not isinstance(years_of_experience, float):
        years_of_experience = float(years_of_experience)
    pred_arr = np.array(years_of_experience)
    preds = pred_arr.reshape(-1,1)
    preds = preds.astype(float)
    model_prediction = lr_model.predict(preds)
    model_prediction = model_prediction[0][0]
    return round(float(model_prediction),2)

def run():
    streamlit.title("Linear Regression Model")
    html_temp="""
""" 
    streamlit.markdown(html_temp)
    yofex = streamlit.text_input("Years of Experience")
    prediction = ""

    if streamlit.button("Predict"):
        prediction = lr_prediction(years_of_experience=yofex)

    streamlit.success(f"The prediction by the model is {prediction}")

if __name__=="__main__":
    run()