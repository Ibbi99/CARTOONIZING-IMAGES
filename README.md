# CARTOONIZING-IMAGES

Programming Language: Python
Integrated Development Environment (IDE): Visual Studio Code

Libraries imported:
#for image processing
import cv2
#to open the filebox
import easygui
#to store image
import numpy as np
#to read image stored at particular path
import imageio
import sys
import matplotlib.pyplot as plt
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

1. Theoretical part
     1.1 CODE DEVELOPMENT OVERVIEW
The core functionality of the project revolves around image processing techniques 
provided by the OpenCV library. Below are the key aspects of the code development:
  a. Image Processing Libraries - the project relies on several libraries for image 
processing, including OpenCV, NumPy, and imageio. These libraries offer a 
wide range of functionalities for reading, processing, and saving images. 
OpenCV is a powerful library for computer vision tasks, making it an ideal 
choice for image manipulation projects.
  b. Graphical User Interface (GUI) - the GUI for the project is built using Tkinter, a 
standard GUI toolkit for Python. Tkinter provides a simple and easy-to-use 
interface for creating desktop applications. It allows developers to design 
interactive graphical interfaces with various widgets such as buttons, labels, 
and entry fields. In the context of this project, Tkinter is used to create a userfriendly interface for uploading images and displaying the cartoonized results.

  1.2 IMAGE CARTOONIZATION ALGORITHM
The cartoonization algorithm implemented in this project follows a series of steps to 
transform a real-life image into a cartoon-like representation. Below are the key steps 
involved in the algorithm:
  a. Grayscale Conversion - The first step in the cartoonization process is to convert 
the original image from color to grayscale. Grayscale images simplify the 
processing task by representing each pixel's intensity with a single value, ranging 
from 0 (black) to 255 (white).
  b. Smoothing - After converting the image to grayscale, a smoothing filter is applied 
to reduce noise and unwanted details. In this project, a median filter is used for 
smoothing, which replaces each pixel's value with the median value of its 
neighboring pixels.
  c. Edge Detection - Edge detection is a critical step in creating the cartoon-like 
effect. It involves identifying the edges and contours within the image. In this 
project, an adaptive thresholding technique is used to detect edges, where the 
threshold value is dynamically adjusted based on local pixel intensities.
  d. Cartoonization - Once the edges are detected, the cartoonization process 
combines the edge-detected image with the original color image to create the final cartoon-like effect. This is achieved by applying a bitwise AND operation 
between the color image and the edge-detected image.

  1.3 USER INTERACTION
  Users interact with the application through the graphical user interface (GUI). They 
can upload an image file from their system using the "Cartoonify an Image" button. Once 
the image is uploaded, the application processes it uses the cartoonization algorithm and 
displays the original and cartoonized versions side by side. Users can then choose to save 
the cartoonized image to their system using the "Save cartoon image" button.

   2. PRACTICAL PART
  2.1 FUNCTIONALITY OVERVIEW
  a. Uploading Images - Upon launching the application, users are presented with 
a GUI interface that allows them to upload an image file. This is achieved 
using the "Cartoonify an Image" button, which triggers a file dialog box where 
users can navigate their system and select an image file.
  b. Cartoonization Process - Once the user selects an image, the application 
processes it uses the implemented cartoonization algorithm. This algorithm 
transforms the original image into a cartoon-like representation, preserving 
key features while simplifying details.
  c. Displaying Results - After the cartoonization process is complete, the 
application displays the original and cartoonized versions of the image side 
by side. This allows users to compare the two versions and see the 
transformation in real-time.

  2.2 GRAPHICAL USER INTERFACE
  a. User-Friendly Interface - the GUI is designed to be intuitive and user-friendly, 
with clear instructions and prominent buttons for uploading images and saving 
results. Users can easily navigate the interface and perform the desired actions 
without any technical knowledge. 
  b. Responsive Design - the GUI is responsive and adjusts to different screen sizes 
and resolutions. This ensures a consistent user experience across different 
devices and platforms.
