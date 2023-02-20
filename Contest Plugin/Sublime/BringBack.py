import os

pathurl = "D:/Workspace/Coding/Codeforces/url.txt"
halfpath = "D:/Workspace/Coding/"
path = "D:/Workspace/Coding/Main.java"

fpurl = open(pathurl)

values = fpurl.read()
values = values.splitlines()

pathn = halfpath+values[2]+"/"+values[3]+"/"+values[4]+".java"

fpurl.close()

fpo=open(path,"w");

fpc=open(pathn)

fpo.write(fpc.read())

fpo.close() 
fpc.close()
