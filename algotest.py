import os
import string
import os


for ti in range(150):
    newFileName = list("aaaaaaaaaa")
    for i , digit in enumerate(newFileName):
        #print(str(ti))
        newFileName[i] = list(string.ascii_lowercase)[ti%26]
        ti -= ti%26
        ti = ti // 26
    newFileName.reverse()
    newFileName = "".join(newFileName)
    print(newFileName)