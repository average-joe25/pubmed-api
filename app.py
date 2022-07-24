# -*- coding: utf-8 -*-
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import tensorflow as tf
from predict import predict
app = FastAPI()

def create_model():
    return tf.keras.models.load_model('./models/pubmed_model')
model=create_model()
class Item(BaseModel):
    data: str
@app.get('/')
def index(item:Item):
    val=predict(item.data,model)
    assert type(val) == str
    return {'value': val}