from fastapi import FastAPI,Path,HTTPException,Query
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
    raise HTTPException(status_code=404, detail="Patient not found")

@app.get('/sort')
def sort_patients(sorted_by:str = Query(..., description="The field to sort patients by"), order :str = Query('asc', description="The order of sorting, 'asc' for ascending and 'desc' for descending")):
    valid_fields = ['height', 'weight', 'bmi']
    if sorted_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid field '{sorted_by}'. Valid fields are: {', '.join(valid_fields)}")
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail=f"Invalid order '{order}'. Valid orders are: 'asc', 'desc'")
    data = load_data()
    
    sort_order = True if order == 'desc' else False
    sorted_data = sorted(data, key=lambda x: x.get(sorted_by, 0), reverse=sort_order)
    return sorted_data
    