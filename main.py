from fastapi import FastAPI

app = FastAPI() # creating the object

# first create an end point
@app.get('/')
def hello():
    return {"Message": "Hello World!!!"}

@app.get('/about')
def about():
    return{"Message": "I am learning FastApi"}