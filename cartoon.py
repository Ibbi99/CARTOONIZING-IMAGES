
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



# Make main window

top=tk.Tk()
top.geometry('400x400')
top.title('Cartoonify your Image !')
top.configure(background='#E6D7F0')
label=Label(top,background='#CDCDCD', font=('helvetica',20,'bold'))


""" fileopenbox opens the box to choose file and help us store file path as string """
def upload():
    ImagePath=easygui.fileopenbox()
    cartoonify(ImagePath)



# Read the image
def cartoonify(ImagePath):
    # read the image
    originalimage = cv2.imread(ImagePath)
    originalimage = cv2.cvtColor(originalimage, cv2.COLOR_BGR2RGB)
    #print(image)  # image is stored in form of numbers
    
    # confirm that image is chosen
    if originalimage is None:
        print("Can not find any image. Choose appropriate file")
        sys.exit()

    ReSized1 = cv2.resize(originalimage, (940,610))
    
    grayScaleImage= cv2.cvtColor(originalimage, cv2.COLOR_BGR2GRAY)

    smoothGrayScale = cv2.medianBlur(grayScaleImage, 5)

    colorImage = cv2.bilateralFilter(originalimage, 9, 300, 300)

    getEdge = cv2.adaptiveThreshold(smoothGrayScale, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                    cv2.THRESH_BINARY, 9, 9)
  
    #masking edged image with our "BEAUTIFY" image
    cartoonImage = cv2.bitwise_and(colorImage, colorImage, mask=getEdge)

    ReSized2 = cv2.resize(cartoonImage, (940,610))
   
    # Plotting the whole transition
    images=[ReSized1, ReSized2]

    fig, axes = plt.subplots(2,1,facecolor='#FEFEDF', figsize=(8,8), subplot_kw={'xticks':[], 'yticks':[]})#, gridspec_kw=dict(hspace=0.1, wspace=0.1))
    for i, ax in enumerate(axes.flat):
        ax.imshow(images[i], cmap='pink')

        
    # Make save button in main window
    save1=Button(top,text="Save cartoon image",command=lambda: save(ReSized2, ImagePath),padx=30,pady=5)
    save1.configure(background='#845EC2', foreground='#FEFEDF',font=('helvetica',10,'bold'))
    save1.pack(side=TOP,pady=50)
    
    plt.show()




# Function for saving button
    
def save(ReSized2, ImagePath):
    
    #saving an image using imwrite()
    newName="cartoon_Image"
    path1 = os.path.dirname(ImagePath)
    extension=os.path.splitext(ImagePath)[1]
    path = os.path.join(path1, newName+extension)
    cv2.imwrite(path, cv2.cvtColor(ReSized2, cv2.COLOR_RGB2BGR))
    I= "Image saved by name " + newName +" at "+ path
    tk.messagebox.showinfo(title=None, message=I)




# Make cartoonify button in the main window

upload=Button(top,text="Cartoonify an Image",command=upload,padx=10,pady=5)
upload.configure(background='#845EC2', foreground='#FEFEDF',font=('helvetica',10,'bold'))
upload.pack(side=TOP,pady=50)

# Main function to build the tkinter window

top.mainloop()
