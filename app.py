# -*- coding: utf-8 -*-
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from predict import predict
app = FastAPI()
class Item(BaseModel):
    data: str
@app.get('/')
def index(item:Item):
    print(item.data)
    val=predict(item.data)
    return {'value': val}

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)
    
#uvicorn app:app --reload