from unicodedata import category

from numpy import outer


def construct(prediction, original):
    class_names=['OBJECTIVE', 'METHODS', 'RESULTS', 'CONCLUSIONS', 'BACKGROUND']
    dict={'OBJECTIVE':"", 'METHODS':"", 'RESULTS':"", 'CONCLUSIONS':"", 'BACKGROUND':""}
    for pred,line in zip(prediction,original):
        category=class_names[pred]
        dict[category]+=line+". "
    output=""
    for heading in ['BACKGROUND','OBJECTIVE', 'METHODS', 'RESULTS', 'CONCLUSIONS']:
        output+=heading+'\n\n'+dict[heading]+'\n\n\n'
    return output