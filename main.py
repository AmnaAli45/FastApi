from fastapi import FastAPI

app = FastAPI() # creating the object

# first create an end point
@app.get('/')
def hello():
    return {"Message": "Pateient Management System"}

@app.get('/about')
def about():
    return{"Message": "We are working to make all the patient management digital."}