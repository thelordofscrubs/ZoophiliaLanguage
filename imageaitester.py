import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
from imageai.Classification import ImageClassification as imclass

executionPath = os.getcwd()
imagePath = os.path.join(executionPath, "imagestoCompile")

predictor = imclass()
predictor.setModelTypeAsInceptionV3()
predictor.setModelPath(os.path.join(executionPath, "model.h5"))
predictor.loadModel()
animals = []

images = map(lambda i : os.path.join(imagePath, i),os.listdir(imagePath))

for i in images:
    predictions, percentage = predictor.classifyImage(i,result_count = 3)
    animals.append(predictions[0])
    print("\n\n\nFile name: " + i)
    #animals.append(predictor.classifyImage(image))
    print("\nIdentified as: \n\n\t"+predictions[0]+" at certainty "+str(percentage[0])+"\n")
    print("\t"+predictions[1]+" at certainty "+str(percentage[1])+"\n")
    print("\t"+predictions[2]+" at certainty "+str(percentage[2]))