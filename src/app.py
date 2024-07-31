# from utils import db_connect
# engine = db_connect()

# your code here

from flask import Flask, request, render_template
from pickle import load

app = Flask(__name__)

# Obtengo el modelo
model = load(open("../models/workspace/Tutorial-de-aplicacion-web-de-ml-usando-flask/src/decision_tree_classifier_default_42.sav", "rb"))

# Diccionario con la prediccion 
class_dict = {
    "0": "No Survived",
    "1": "Survived"
}


@app.route("/", methods= ["GET", "POST"])


def index():
    if request.method == "POST":
        
        # Obtain values from form
        pclass = float(request.form["pclass"])
        sex = request.form["sex"]
        FamMembers = float(request.form["FamMembers"])
        fare = float(request.form["fare"])
        embarked = request.form["embarked"]

# # Convertir variables categóricas a valores numéricos
        sex_n = 1 if sex == "Male" else 0
        embarked_n = {"C": 0, "Q": 1, "S": 2}[embarked]
        
        data = [[pclass, sex_n, FamMembers, fare, embarked_n]]
        prediction = str(model.predict(data)[0])
        pred_class = class_dict[prediction]
        
    else:
        pred_class = None
    
    return render_template("index.html", prediction = pred_class)
