#!/usr/bin/python


#========================================================
# demo.py
#
# ABOUT:  This script grabs image files in the input directory ('input_dir'), and pastes them into the output directory ('output_dir').  Then, it renames all of the images in the 'output_dir' with the prefix, 'output_<existing file name>'.  Next, it runs each of the 'output_' files through a classification Digital Neural Network (DNN)'.  Changing the 'network' variable to another existing DNN from the 'Hello' directory can be done by the user (example, 'googlenet', 'alexnet', 'vgg-16'.  Each of the 'output_' files is then stamped with the name of the identified object along with the percentage of certainty
#
#
# USE:  Use this script to process a large batch of images files in a directory, without having to use a command line for each image to classify it
#
# 
# CAVEATS:  -  Should log-in as 'learner' account to run this python script
#	    -  Terminal window should be set to the following directory before running this python script: ~/Documents/Hello/Images_Input 
#           -  Once navigated to the above directory, enter in the following command to run:  python3 demo.py		
#           -  Assumes that the user running this Python script has Python version 3.0 or greater
# 
#
# CREATED BY:  Stephen Long
# CREATED ON:  8/11/2019
#========================================================



 # Import NVIDIA Jetson modules and SYSTEM modules used for this script
import jetson.inference
import jetson.utils

import argparse
import os
import shutil
import subprocess


# Set local variables to Define workspace Directories
input_dir = "/home/learner/Documents/Hello/Images_Input"
output_dir = "/home/learner/Documents/Hello/Images_Output"

input_file = os.fsencode(input_dir)
output_file = os.fsencode(output_dir)


class cd:
# Context manager for changing the current working directory

    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)    

# Grab image files in Images_Input directory and copy to Images_Output directory
# NOTE:  At this time, only '.jpg' image files work when processed the entire way through the classification process
for file in os.listdir(input_file):
    select_img = os.fsdecode(file)
    if select_img.endswith( ('.jpeg', '.jpg', '.gif', '.png') ):
        print("Copied!")
        shutil.copy2(select_img, output_dir)
        print(os.getcwd())
        continue

# Change working directory to Images_Output, and rename each image in the directory with 'output_' prefix in the file name
# If existing images in the directory already have a 'output_' prefix, another 'output_' prefix will be added in the file name
with cd(output_dir):
    for file in os.listdir(output_file):
        rename_img = os.fsdecode(file)
        if rename_img.endswith( ('.jpeg', '.jpg', '.gif', '.png') ):
            print("Renamed!")
            os.rename(rename_img, 'output_' + rename_img)
            print(os.getcwd())

#print(os.getcwd())

import sys

# This section defines the parameters used for classifying the image file (network, model, and labels)
# NOTE:  At this time, only the user switching the 'network' to other predefined DNNs work, like 'googlenet' or 'alexnet'.  The retrained '.onnx' file for the resnet-18 DNN does not work
number_runs = 1
network = "resnet-18"

model = "--model=$"
myModelPath = "/home/learner/Documents/Hello/jetson-inference/python/training/imagenet/nonrecycle_recycle"
mpath = myModelPath
myModel = "/resnet18.onnx"

label = "--labels=$"
myLabelPath = "/home/learner/Documents/datasets_objects/nonrecycle_recycle"
lpath = myLabelPath
myLabels = "/labels.txt"


profile = False
file_in = "in"
file_out = "out"

# Change directory to 'Images_Output' and grab image files in the directory
# NOTE:  At this time, only '.jpg' image files work
with cd(output_dir):
    for file in os.listdir(output_file):
        processed_img = os.fsdecode(file)
        if processed_img.endswith( ('.jpeg', '.jpg', '.gif', '.png') ):
            print(os.getcwd())
            #print("Grabing the file to process!")


    # load an image (into shared CPU/GPU memory)
        img, width, height = jetson.utils.loadImageRGBA(processed_img)


    # load the recognition network
        net = jetson.inference.imageNet(network)


    # enable model profiling
        if profile is True:
                        net.EnableLayerProfiler()

        else:
		        number_runs = 1

    # run model inference
        for i in range(number_runs):
                        if number_runs > 1:

                            print("\n////////////// RUN {:d} \n////////////" .format(i))
                
                    # Classify the image
                        class_idx, confidence = net.Classify(img, width, height)

		    # find the object description
                        class_desc = net.GetClassDesc(class_idx)

		    # print out the result into the current Terminal window
                        print("image is recognized as '{:s}' (class #{:d}) with {:f}% confidence".format(class_desc, class_idx, confidence * 100))
	
                    # print out timing info into the current Terminal window
                        net.PrintProfilerTimes()


        print(os.getcwd())
        #print("Home stretch!")

    # overlay the classification result with certainty percentage on the image
        if processed_img is not None:
                font = jetson.utils.cudaFont(size=jetson.utils.adaptFontSize(width))
                font.OverlayText(img, width, height, "{:f}% {:s}".format(confidence * 100, class_desc), 10, 10, font.White, font.Gray40)
                jetson.utils.cudaDeviceSynchronize()
                jetson.utils.saveImageRGBA(processed_img, img, width, height)


