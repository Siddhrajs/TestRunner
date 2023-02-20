import urllib2

contest=str(raw_input())
question=str(raw_input())
linkurl="http://codeforces.com/contest/"+contest+"/problem/"+question
print(linkurl)

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
        pathi = "/home/siddhraj/Competitive/Main.0"+str(j/2+1)+".inp"
        fpi = open(pathi,"w")
        #fpi.write(str(j/2+1))
        #fpi.write("\n")
        for k in range(len(inputtmp)):
            fpi.write(inputtmp[k])
            fpi.write("\n")
            #print(inputtmp[k])
        fpi.close()
    else:
        patho = "/home/siddhraj/Competitive/Main.0"+str(j/2+1)+".oac"
        fpo = open(patho,"w")
        #fpo.write(str(j/2+1))
        #fpo.write("\n")
        for k in range(len(inputtmp)):
            fpo.write(inputtmp[k])
            fpo.write("\n")
            #print(inputtmp[k])
        fpo.close()
print("successfull")