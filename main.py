from fastapi import FastAPI, Form, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates 

app = FastAPI()

templates = Jinja2Templates(directory = '.')

@app.get('/')
def home(request: Request):
  return templates.TemplateResponse(
    'index.html',
    {'request' : request}
  )
    
   
@app.post('/predict')
def predict(
  request: Request,
  number_1: float = Form(...)
):
  prediction = number_1 * 10

  return templates.TemplateResponse(
    'results.html',
    {
      'request' : request,
      'prediction' : prediction
    }
  )
