
from horoscope import generate_prophecies as gp
from datetime import datetime as dt

head=[]

def generate_head(title):
    head=f"<head><title>{title}</title><meta charset='utf-8'></head>"
    return head

def genearte_zag():
    date=dt.now().date()
    zag=f"Гороскоп на {str(date)}!"
    return zag


def generate_body():
    zag=genearte_zag()
    body=""
    har=f"<h1>{zag}</h1>"
    body=body+har
    pred=gp()
    for i in pred:
        pred_i=f"<p>{i}</p>"
        body+=pred_i
    return body

def generate_page():
    head=generate_head("Гороскоп")
    body=generate_body()
    page = f"<html>{head}{body}</html>"
    return page

def save_page():
    fl= open("index.html","w",encoding='utf-8')
    page=generate_page()
    print(page, file=fl)
    fl.close()

save_page()
