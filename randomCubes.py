#randomCubes.py

import maya.cmds as cmds
import random

#Here, we're creating a script to create a bunch of instances of one square
#Then we take those instances, apply a random rotation, transform, and scaling to them
#This creates a scattered cube

random.seed(1234)

#ls command brings up the names
#we are searching for ls with name 'myCube'
#if they exist, we delete it
#this creates a blank scene

cubeList = cmds.ls('myCube*')
if len (cubeList) > 0: 
    cmds.delete(cubeList)
    

result = cmds.polyCube( w = 1, h = 1, d = 1, name = "myCube#")

print ('result ' + str(result))

#result = ['mycube1', 'polyCube1'] so we just want [0] of result to get the name
transformName = result[0]

#we want to create 50 cubes
for i in range (0,50): 
    
    #going to create an instance of the cube
    instanceResult = cmds.instance( transformName, name = transformName + '_instance#')
    
    #print('instanceResult: '+ str(instanceResult))
    #use i to stack the cubes
    x = random.uniform(-10,10)
    y = random.uniform(0,20)
    z = random.uniform(-10,10)
    cmds.move(x,y,z,instanceResult)
    
    xRot = random.uniform(0,360)
    yRot = random.uniform(0,360)
    zRot = random.uniform(0,360)
    
    cmds.rotate(xRot,yRot,zRot, instanceResult)

    scalingFactor = random.uniform(0.3,1.5)
    cmds.scale(scalingFactor, scalingFactor, scalingFactor, instanceResult)
