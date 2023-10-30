from flask import Flask, request
import pickle
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

pickle_in = open("docker_app/logreg.pkl","rb")
model=pickle.load(pickle_in)

@app.route("/predict", methods=["Get"])
def predict_class():
    """Predict the species of the flower.
    ---
    parameters:
    - name : sepal_length
        in : query
        type : number
        required : true
    - name : sepal_width
        in : query
        type : number
        required : true
    - name : petal_length
        in : query
        type : number
        required : true
    - name : petal_width
        in : query
        type : number
        required : true
    """
    sepal_length = float(request.args.get("sepal_length"))
    sepal_width = float(request.args.get("sepal_width"))
    petal_length = float(request.args.get("petal_length"))
    petal_width = float(request.args.get("petal_width"))
    prediction = model.predict([sepal_length,sepal_width,petal_length,petal_width])
    print(prediction)
    return "Model prediction is"+str(prediction)


if __name__=="__main__":
    app.run(debug=True)
    