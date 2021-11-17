# ZoophiliaLanguage
A Brainfuck equivalent language compiler and decompiler

Wikipage at 

You will need to run these pip commands to install dependencies, and have python 2 or 3 installed:
pip install tensorflow==2.4.0
pip install keras==2.4.3 numpy==1.19.3 pillow==7.0.0 scipy==1.4.1 h5py==2.10.0 matplotlib==3.3.2 opencv-python keras-resnet==0.2.0
pip install imageai --upgrade

Place your images of cats, dogs, turtles, toucans, elephants, lions, rabbits, and chickens in the "imagesToCompile" folder, or alternatively place one of each in the exampleImages folder and use the bfToZoo decompiler to decompile Brainfuck into Zoophile

If you put in your own images, they must be in lexigraphical order (I used big endian base 26 notation using a-z)

compiler.py is a bit of a misnomer, as it will both compile to BF and then interpret the BF using a built in BF interpreter
