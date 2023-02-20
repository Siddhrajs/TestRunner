import os

pathurl = "D:/Workspace/Coding/Codeforces/url.txt"
halfpath = "D:/Workspace/Coding/"
path = "D:/Workspace/Coding/Main.java"

fpurl = open(pathurl)

values = fpurl.read()
values = values.splitlines()

pathnew = halfpath+values[2]+"/"+values[3]+"/"+values[4]+".java"

fpurl.close()

if not os.path.isdir(halfpath+values[2]+"/"+values[3]):
    print(halfpath+values[2]+"/"+values[3])
    os.makedirs(halfpath+values[2]+"/"+values[3],0777)

fpo=open(path)

fpc=open(pathnew,"w+")

fpc.write(fpo.read())

fpo.close()
fpc.close()
