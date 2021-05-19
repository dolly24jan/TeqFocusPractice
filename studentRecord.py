from flask import Flask, Response
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask import jsonify,request


app = Flask(__name__)
app.secret_key="secretkey"
app.config['MONGO_URI'] = "mongodb://localhost:27017/StudentDatabase"
mongo=PyMongo(app)

@app.route('/add',methods=["GET"])
def getDataAll():
    gt=list(myData.find())
    for x in data:
        x["_id"]=str(x["_id"])
    return Response(response=json.dumps({"Records" :gt}),mimetype="application/json")
                    

@app.route('/getData/<name>', methods=["GET"])
def getdata(name,Class,marks):
    data = list(myData.find({'firstName': name,"Class":Class,"Marks":marks}))
    for x in data:
        x["_id"] = str(x["_id"])
    return  Response(response=json.dumps({"student data" : data}),mimetype="application/json")

if __name__ == "__main__":
    app.run(debug=True)
