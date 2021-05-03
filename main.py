import uvicorn
from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def index():
    return "Welcome to city"
    
    
    
@app.get('/name')
def get_name(name: str):
    return {"My name is" : f"{name}"}
    
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=5000)
         