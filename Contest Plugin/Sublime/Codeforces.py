import subprocess
import os

path = "D:/Workspace/Coding/Codeforces/url.txt"
pathi = "D:/Workspace/Coding/Codeforces/tempinput.txt"
patho = "D:/Workspace/Coding/Codeforces/tempoutput.txt"
pathte = "D:/Workspace/Coding/Codeforces/temp.txt"
pathm = "D:/Workspace/Coding/JavaOutput.txt"
path2 = "D:/Workspace/Coding/CustomInput.txt"
fp = open(path)
values = fp.read()
values = values.splitlines()
fp.close()
flag = True

patht = "D:/Workspace/Coding/Codeforces/"+values[1]+".txt"
fpt = open(patht)

valuest = fpt.read()
valuest = valuest.splitlines()
fpt.close()

i = 1
j = 0
passed =0
fpm = open(pathm,"w")

while i<len(valuest):
    fpi = open(pathi,"w")
    while i<len(valuest) and valuest[i]!="Output":
        if valuest[i]!="" and valuest[i]!="Input":
            fpi.write(valuest[i])
            fpi.write("\n")
        i = i+1
    fpi.close()

    i = i+1
    fpo = open(patho,"w")
    while i<len(valuest) and valuest[i]!="Input":
        if valuest[i]!="" and valuest[i]!="Output":
            fpo.write(valuest[i])
            fpo.write("\n")
        i = i+1
    fpo.close()

    os.chdir("D:/Workspace/Coding/")
    subprocess.call('java Main<Codeforces/tempinput.txt>Codeforces/temp.txt', shell=True)

    fpo = open(patho)
    fpte = open(pathte)

    fpm.write("TestCase "+str(j+1)+"\n\n")
    #print("TestCase "+str(j+1)+"\n\n")

    fpm.write("Input\n")
    fpm.write(open(pathi).read()+"\n")

    fpm.write("Expected Output\n")
    #print("Expected Output\n")
    stringo = fpo.read()
    fpm.write(stringo+"\n")
    #print(stringo+"\n")

    fpm.write("Your Output\n")
    #print("Your Output\n")
    stringte = fpte.read()
    fpm.write(stringte+"\n")
    #print(stringte+"\n")

    if stringo==stringte:
        passed = passed +1
        fpm.write("Pass\n\n")
        #print("This test case passed\n\n")
    else:
        fpm.write("FAIL\n\n")
        if flag:
            f = open(path2,"w")
            f.write(open(pathi).read())
            f.close()
            flag = False
        #print("This failed\n\n")
    
    j = j+1
    fpo.close()
    fpte.close()
    fpm.write("=======================\n\n")

if passed == j:
    fpm.write("ALL TESTCASES PASSED!!\n")
    if len(values)==2:
        directory = "D:/Workspace/Coding/Codeforces/"+values[0]
        if not os.path.isdir(directory):
            os.makedirs(directory,0777)
        of=open("D:/Workspace/Coding/Main.java")
        cf=open(directory+"/"+values[1]+".java","w+")
        cf.write(of.read())
        of.close()
        cf.close()
            
    #print("All testcases passed\n")
else:
    fpm.write("Out of "+str(j)+", "+str(passed)+" testcases passed\n\n")
    fpm.write("Due to spaces error may occur so please check manually\n")
    #print("Out of "+str(j)+", "+str(passed)+" testcases passed\n")

fpm.close()


