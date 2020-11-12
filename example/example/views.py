"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from example import app 
from flask import Flask
from example.info import Data
new=[]

new.append(Data(1,"xeber1","Content1"))
  
new.append (Data(2,"xeber2","Content2"))
new.append (Data(3,"xeber3","Content3"))
new.append (Data(4,"xeber4","Content4"))

@app.route('/newsdetail/<id>')
def news(id):
    """Renders the contact page."""
    for i in new:
        if(int(id)==i.id):
           
           obj=i
           
    return render_template(
        "newsdetail.html",
       data=obj)

@app.route('/')
def index():
    """Renders the contact page."""        
                     
    return render_template(
        "index.html",
       data=new)









