from fastapi import FastAPI,Path
import json

app = FastAPI() # creating the object

# Helper to load data
def load_data():
    with open('pateints.json','r') as f:
        data = json.load(f)
        return data

# first create an end point
@app.get('/')
def hello():
    return {"Message": "Pateient Management System"}

@app.get('/about')
def about():
    return{"Message": "We are working to make all the patient management digital."}

@app.get('/view')
def view():
    data = load_data()
    return data

@app.get('/view/{patient_id}')
def view_patient(patient_id: int = Path(..., description="The ID of the patient to retrieve",example = 1)):
    data = load_data()
    for patient in data:
        if patient['id'] == patient_id:
            return patient # jis ki id url mein ho gy wo wale patient ka data return ho ga
    return {"Message": "Patient not found."}