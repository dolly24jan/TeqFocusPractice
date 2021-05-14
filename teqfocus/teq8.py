try:
    f=open("file1.txt","r")
    d = []
    for x in f:
        keys, value =x.split(" ",1)
        newKey = keys.replace(":" , "")
        a={"ID:"+newKey,"data: "+value.strip()}
        a=d.append(a)
    print(d)
except:
    print("Unable to read file")



