from imp import new_module
import string
import tensorflow as tf
import pandas as pd
import numpy as np
def clean(abstract:str):
    cleaned=""
    for ch in abstract:
        if(ch.isdigit()):
            cleaned+='@'
        else:
            cleaned+=ch
    return cleaned
def shorten(text):
  lists=text.split(" ")
  size=np.minimum(50,len(lists))
  t = " ".join(lists[:size])
  return t   
def CharTransform(x):
    return " ".join(list(x))
def convert_to_df(abstract:str):
    list_lines=abstract.split('.')
    org_text=[]
    dict_list=[]
    count=1
    for line in list_lines:
        line=line.strip()
        line=line[:max(50,len(line))]
        org_text.append(line)
        line=clean(line)
        if(len(line)==0):
            continue
        line=shorten(line)
        dict_list.append({'text':line, 'location':float(count/len(list_lines))})
        count+=1
    new_df=pd.DataFrame(dict_list)
    
    new_df['char_text']=new_df['text'].apply(CharTransform)
    
    return (new_df,org_text)

def predict(input:str,model):
    (df,org)=convert_to_df(input)
    tf_data_df=tf.data.Dataset.from_tensor_slices((df['text'].to_numpy(),df['char_text'].to_numpy(),df['location'].to_numpy()))
    output=model.predict(tf_data_df)
    return output