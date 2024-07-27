# from utils import db_connect
# engine = db_connect()

# your code here
############################# Streamlit ##############################

# from pickle import load
# import streamlit as st

# model = load(open(r"C:\Users\wipip\OneDrive\Documentos\GitHub\Despliegue_con_Streamlit-main\models\decision_tree_classifier_default_42.sav", "rb"))
# class_dict = {
#     "0": "No Survived",
#     "1": "Survived"
# }

# st.title("Titanic Survivors prediction")


# # Entrada de características categóricas y numéricas
# pclass = st.selectbox("Passenger Class", options=[1, 2, 3])
# sex = st.selectbox("Sex of the Passenger", options=["Male", "Female"])
# FamMembers = st.slider("Number of Siblings/Spouses Aboard", min_value=0, max_value=10, step=1)
# fare = st.slider("Fare Paid", min_value=0.0, max_value=500.0, step=0.1)
# embarked = st.selectbox("Place of Embarkment", options=["C", "Q", "S"])

# # Convertir variables categóricas a valores numéricos
# sex_n = 1 if sex == "Male" else 0
# embarked_n = {"C": 0, "Q": 1, "S": 2}[embarked]

# # Botón de predicción
# if st.button("Predict"):
#     prediction = str(model.predict([[pclass, sex_n, FamMembers, fare, embarked_n]])[0])
#     pred_class = class_dict[prediction]
#     st.write("Prediction:", pred_class)

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"
    
