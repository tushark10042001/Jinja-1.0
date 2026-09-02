from fastapi import FastAPI, Form
from fastapi.responses import FileResponse, HTMLResponse

app = FastAPI()

@app.get('/')
def home():
  return FileResponse("index.html")
   
@app.post('/predict')
def predict(
  number_1: float = Form(...)
):
  prediction = number_1 * 10

  return """
  <!DOCTYPE html>
  
  <html>
  
  <head>
     <title>Prediction</title>
  </head>

  <body>

  <p>Your prediction is: {prediction}</p>
  
  </body>
  </html>
  """
  
