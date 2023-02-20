import urllib2
import subprocess

path = "D:/Workspace/Coding/Codeforces/url.txt"
fp = open(path)
values = fp.read()
values = values.splitlines()
flag = False
if len(values[0])<5:
    values[0]="http://codeforces.com/contest/"+values[0]+"/problem/"
    flag = True
if len(values)==2:
    testcases = ['A','B','C','D','E','F','G','H','I','J','K','L','M']
else:
    testcases = ['A']

for i in range(len(testcases)):
    pathw = "D:/Workspace/Coding/Codeforces/"+testcases[i]+".txt"
    fpw = open(pathw,"w")
    if flag:
        linkurl = values[0]+testcases[i]
    else:
        linkurl=values[0]
    print(linkurl)

#print(linkurl)

    response = urllib2.urlopen(linkurl)
    page_source = response.read()
    #print(page_source)

    inputs = page_source.split("<pre>")
    #print(len(inputs))

    for j in range(len(inputs)-1):
        #print(inputs[j+1])
        inputs[j+1] = inputs[j+1].split("</pre>")[0]
        inputtmp = inputs[j+1].split("<br />")
        if j%2==0:
            fpw.write("Input\n")
        else:
            fpw.write("Output\n")
        for k in range(len(inputtmp)):
            fpw.write(inputtmp[k])
            fpw.write("\n")
            print(inputtmp[k])
    #print("\n")
    
    fpw.close()
    
fp.close()
