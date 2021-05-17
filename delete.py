import pymongo

myClient = pymongo.MongoClient("localhost",27017) #Establish connection 
myDB = myClient["StudentDatabase"]                          #database creation
myCol = myDB["Student"]                                             #collection

mylist = [
  {'first_name': "Dolly","last_name":"Singh","dob":"24/01/95","class":"10th","Roll":"01"},
  {'first_name': "Shruti","last_name":"Sinha","dob":"13/11/95","class":"12th","Roll":"02"},
  {'first_name': "Pranav","last_name":"Shekhar","dob":"05/05/92","class":"10th","Roll":"03"},
  {'first_name': "Neha","last_name":"Khandelwal","dob":"14/03/89","class":"10th","Roll":"04"},
  {'first_name': "Ankit","last_name":"Singh","dob":"26/12/97","class":"12th","Roll":"05"}
]

query = {"Roll_no" : "3"}
myCol.delete_one(query)

for x in myCol.find():
    print(x)
