import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
from imageai.Classification import ImageClassification as imclass
import bfInterpreter


executionPath = os.getcwd()
imagePath = os.path.join(executionPath, "imagestoCompile")

predictor = imclass()
predictor.setModelTypeAsInceptionV3()
predictor.setModelPath(os.path.join(executionPath, "model.h5"))
predictor.loadModel()
animals = []
bfout = ""

images = map(lambda i : os.path.join(imagePath, i),os.listdir(imagePath))

for i in images:
    predictions, percentage = predictor.classifyImage(i,result_count = 1)
    animals.append(predictions[0])
    print("\n\n\nFile name: " + i)
    #animals.append(predictor.classifyImage(image))
    print("\nIdentified as: \n\n\t"+predictions[0]+" at certainty "+str(percentage[0])+"\n")
    #print("\t"+predictions[1]+" at certainty "+str(percentage[1])+"\n")
    #print("\t"+predictions[2]+" at certainty "+str(percentage[2]))

for a in animals:
    a = a.lower()
    if a == "dog" or a == "vizsla" or a == "appenzeller":
        bfout += "<"
    elif a == "cat" or a == "tabby" or a == "egyptian_cat":
        bfout += ">"
    elif a == "chicken" or a == "hen" or a == "rooster":
        bfout += "."
    elif a == "leatherback_turtle" or a == "loggerhead":
        bfout += ","
    elif a == "toucan":
        bfout += "+"
    elif a == "lion":
        bfout += "-"
    elif a == "elephant" or a == "african_elephant" or a == "tusker":
        bfout += "["
    elif a == "rabbit" or a == "cowboy_hat" or a == "hare":
        bfout += "]"
    else:
        bfout += a
print("\nbrainfuck output is "+bfout+"\n")
bfInterpreter.evaluate(bfout)

#hello world example
#bfInterpreter.evaluate("++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.")
