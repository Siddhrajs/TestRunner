path = "C:/Users/siddh/IdeaProjects/CHelperTest/output/Main.java"
path2 = "C:/Users/siddh/IdeaProjects/CHelperTest/DACodeforces/DAMain.java"

fp = open(path)
fp2 = open(path2,"w")

values = fp.read()
values = values.splitlines()

spaces = [0]*len(values)

titleComment = "/**\n * @author Siddhraj Sisodiya\n */\n\n"

fp2.write(titleComment)

for i in range(len(values)):
        spaces[i] = 0
        for j in range(len(values[i])):
                if values[i][j] != ' ':
                        break
                spaces[i]+=1

i = 0

while i < len(values):
        if values[i] == "/**":
                i = i+6
        for j in range(len(values[i])):
                if j == len(values[i])-1 and values[i][j] == '{':
                        fp2.write("\n")
                        for k in range(spaces[i]):
                                fp2.write(" ")
                fp2.write(values[i][j])
        fp2.write("\n")
        i = i + 1
                
fp.close()
fp2.close()
