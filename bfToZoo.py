import os
from shutil import copyfile
import string

imc = os.getcwd()+"/exampleImages"
imp = os.getcwd()+"/imagesToCompile"
for file in os.listdir(imp):
    os.remove(imp+"/"+file)
bfin = """++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."""
for index, char in enumerate(bfin):
    newFileName = list("aaaaaaaaaa")
    ti = index
    for i , digit in enumerate(newFileName):
        #print(str(ti))
        newFileName[i] = list(string.ascii_lowercase)[ti%26]
        ti -= ti%26
        ti = ti // 26
    #for i, letter in enumerate(list(string.ascii_lowercase[1:])):
    #    num = index%(10**i)
    #    newString = letter*num
    #    newFileName = newString+newFileName[num:]
    newFileName.reverse()
    newFileName = "".join(newFileName)
    if char == "<":
        copyfile(imc+"/dog.jpg",imp+"/"+newFileName+".jpg")
    elif char == ">":
        copyfile(imc+"/cat.jpg",imp+"/"+newFileName+".jpg")
    elif char == ".":
        copyfile(imc+"/chicken.jpg",imp+"/"+newFileName+".jpg")
    elif char == ",":
        copyfile(imc+"/turtle.jpg",imp+"/"+newFileName+".jpg")
    elif char == "[":
        copyfile(imc+"/elephant.jpg",imp+"/"+newFileName+".jpg")
    elif char == "]":
        copyfile(imc+"/rabbit.jpg",imp+"/"+newFileName+".jpg")
    elif char == "+":
        copyfile(imc+"/toucan.jpg",imp+"/"+newFileName+".jpg")
    elif char == "-":
        copyfile(imc+"/lion.jpg",imp+"/"+newFileName+".jpg")
    else:
        pass
