# -*- coding: utf-8 -*-
import uvicorn
import tensorflow as tf
from fastapi import FastAPI
from pydantic import BaseModel
from predict import predict
app = FastAPI()

@tf.keras.utils.register_keras_serializable()
def create_model():
    return tf.keras.models.load_model('./models/pubmed_model')

new_model=create_model()
class Item(BaseModel):
    data: str
@app.get('/')
def index(item:Item):
    val=predict(item.data,new_model)
    assert type(val) == str
    return {'value': val}