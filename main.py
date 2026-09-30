from fastapi import FastAPI
import json

app = FastAPI() # creating the object

# Helper to load data
def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)

# first create an end point
@app.get('/')
def hello():
    return {"Message": "Pateient Management System"}

@app.get('/about')
def about():
    return{"Message": "We are working to make all the patient management digital."}


