app.py
#app.py
from flask import Flask, request, session, redirect, jsonify

app = Flask(__name__)
app.secret_key = 'mysecretkey'

patients=[{"id":1, "name":"Ali Hassan", "condition":"Flu"},{"id":2, "name":"Sara Khan", "condition":"Diabetes"}]


@app.route('/api/health')
def GET(status):
    return {"status":"ok"} 


@app.route('/api/patients')
def GET(all):
    return {list} 

@app.route('/api/patients/<id>')
def GET(id):
    if(id==1):
        return {"name":"Ali Hassan","condition": "Flu"}
    elif(id==2):
        return {"name":"Sara Khan","condition": "Diabetes"}
    else:
        return{404}

@app.route('/api/patients')
def Post(name,condition):
    print("Enter the name of the patient")
    input(name)
    print("Enter condition of the patient")
    input(condition)
    return {name,condition}
 

@app.route('/api/patients')
def PUT(status):
    return {"status":"ok"} 

@app.route('/api/patients')
def DELETE(status):
    return {"status":"ok"} 
