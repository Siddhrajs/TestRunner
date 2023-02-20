import os
import subprocess

pathurl = "D:/Workspace/Coding/Codeforces/url.txt"
directory = "D:/Workspace/Coding/"
path = "D:/Workspace/Coding/JavaOutput.txt"

fpurl = open(pathurl)

values = fpurl.read()
values = values.splitlines()


if len(values) == 2:
    command = 'dir | findstr DIR>temp.sid'
    #print('2')

elif len(values) == 3:
    directory = directory + values[2] + '/'
    command = 'dir | findstr DIR>temp.sid'
    #print('3')

elif len(values) == 4:
    directory = directory + values[2] + '/' + values[3] + '/'
    command = 'dir | findstr .java>temp.sid'
    #print('4')

os.chdir(directory)
subprocess.call(command,shell=True)
fpc=open(directory+'temp.sid')
fpv=open(path,"w")
copies = fpc.read()
copies = copies.splitlines()
for i in range(len(copies)):
    copies[i]=copies[i].split(" ")[len(copies[i].split(" "))-1]
    fpv.write(copies[i]+"\n")
    #print(copies[i+2])
fpv.close()

fpurl.close()
