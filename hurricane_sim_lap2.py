# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 14:42:34 2020

@author: glf14002
"""

import random
import numpy as np
import scipy.stats
import math
import tkinter as tk
from PIL import ImageTk,Image
from tkinter import *
import sys
import math
from tkinter import simpledialog
import matplotlib.pyplot as plt
from PIL import ImageTk,Image
import arcinfo
import arcpy
import arcgis
import arcgisscripting
import requests
from io import BytesIO

def writeCoordinates():
    y_coord = entry1.get()
    x_coord = entry2.get()    
   # file = open("Coordinates","w")
   # file.write("x_coordinate, y_coordinate \n")
    coordinates_string = "{}, {}".format(x_coord,y_coord)
   # file.write(coordinates_string)
   # file.flush()
    file = open("Coordinates_up","w")
    file.write("Point \n")
    coordinates_string = "0 {} {} 0 0".format(x_coord,y_coord)
    file.write(coordinates_string)
    file.write("\nEND")
    file.flush()
    root14.destroy()

def submitAnswers():
    global K_zt
    Lh = entry3.get()
    Lh = float(Lh)
    H = entry4.get()
    H = float(H)
    z = entry5.get()
    z = float(z)
    x = entry6.get()
    x = float(x)
    if exposure_category == 1:
        if feature_type == 1:
            K1 = 0.95*H/Lh
            u = 1.5
            lamb = 4
            K2 = 1 - (x/(u*Lh))
            K3 = math.exp((-lamb*z)/Lh)
            K_zt = (1+K1*K2*K3)**2
        elif feature_type == 2:
            K1 = 1.30*H/Lh
            u = 1.5
            lamb = 3
            K2 = 1 - (x/(u*Lh))
            K3 = math.exp((-lamb*z)/Lh)
            K_zt = (1+K1*K2*K3)**2
        elif feature_type == 3:
            K1 = 0.75*H/Lh
            u = 4
            lamb = 2.5
            K2 = 1 - (x/(u*Lh))
            K3 = math.exp((-lamb*z)/Lh)
            K_zt = (1+K1*K2*K3)**2
        else:
            K_zt = 1.0
    if exposure_category == 2:
        if feature_type == 1:
            K1 = 1.05*H/Lh
            u = 1.5
            lamb = 4
            K2 = 1 - (x/(u*Lh))
            K3 = math.exp((-lamb*z)/Lh)
            K_zt = (1+K1*K2*K3)**2
        elif feature_type == 2:
            K1 = 1.45*H/Lh
            u = 1.5
            lamb = 3
            K2 = 1 - (x/(u*Lh))
            K3 = math.exp((-lamb*z)/Lh)
            K_zt = (1+K1*K2*K3)**2
        elif feature_type == 3:
            K1 = 0.85*H/Lh
            u = 4
            lamb = 2.5
            K2 = 1 - (x/(u*Lh))
            K3 = math.exp((-lamb*z)/Lh)
            K_zt = (1+K1*K2*K3)**2
        else:
            K_zt = 1.0
    if exposure_category == 3:
        if feature_type == 1:
            K1 = 1.15*H/Lh
            u = 1.5
            lamb = 4
            K2 = 1 - (x/(u*Lh))
            K3 = math.exp((-lamb*z)/Lh)
            K_zt = (1+K1*K2*K3)**2
        elif feature_type == 2:
            K1 = 1.55*H/Lh
            u = 1.5
            lamb = 3
            K2 = 1 - (x/(u*Lh))
            K3 = math.exp((-lamb*z)/Lh)
            K_zt = (1+K1*K2*K3)**2
        elif feature_type == 3:
            K1 = 0.95*H/Lh
            u = 4
            lamb = 2.5
            K2 = 1 - (x/(u*Lh))
            K3 = math.exp((-lamb*z)/Lh)
            K_zt = (1+K1*K2*K3)**2
        else:
            K_zt = 1.0
    root15.destroy()


# collecting anonymous user number
#root4 = tk.Tk()
#root4.withdraw()
#Participant_num = simpledialog.askstring(title = "Participant Number", prompt = "What is the participant number assigned to you?")

# get user demographics
root2 = tk.Tk()
root2.title('Demographics')
root2.geometry("400x400")


clicked5 = tk.StringVar(root2)
clicked5.set("Choose Option")

clicked6 = tk.StringVar(root2)
clicked6.set("Choose Option")

clicked7 = tk.StringVar(root2)
clicked7.set("Choose Option")

clicked8 = tk.StringVar(root2)
clicked8.set("Choose Option")

clicked9 = tk.StringVar(root2)
clicked9.set("Choose Option")


question5 = tk.Label(root2, text = "What gender do you identify as?")
question5.pack()

drop5 = tk.OptionMenu(root2,clicked5,"Male", "Female", "Others", "Prefer  not to answer")
drop5.pack()

question6 = tk.Label(root2, text = "What is your age?")
question6.pack()

drop6 = tk.OptionMenu(root2,clicked6, "Under 18", "18-25", "26-35", "36-45", "46-55", "56-75", "76+", "Prefer not to answer")
drop6.pack()

question7 = tk.Label(root2, text = "What is the highest degree or level of education you have \n completed?")
question7.pack()

drop7 = tk.OptionMenu(root2,clicked7, "Some high school", "High school diploma", "Bachelor's degree", "Graduate degree (Master's and/or PhD)", "Prefer not to answer")
drop7.pack()

question8 = tk.Label(root2, text = "What is your annual household income?")
question8.pack()

drop8 = tk.OptionMenu(root2,clicked8, "Less than $20,000", "$20,000 to $34,999", "$35,000 to $49,999", "$50,000 to $74,999", "$75,000 to $99,999", "Over $100,000", "Prefer not to answer")
drop8.pack()

question9 = tk.Label(root2, text = "Including yourself, how many people currently live in your \n household?")
question9.pack()

drop9 = tk.OptionMenu(root2,clicked9, "1", "2", "3", "4", "5", "More than 5", "Prefer not to answer")
drop9.pack()


exit_button = tk.Button(root2, text = "Submit", command = root2.destroy)
exit_button.pack(side=BOTTOM)


root2.mainloop()

# get human behavior/factors influencing evacuation decision
root3 = tk.Tk()
root3.title('Human Behaviors/Factors')
root3.geometry("400x400")


clicked10 = tk.StringVar(root3)
clicked10.set("Choose Option")

clicked11 = tk.StringVar(root3)
clicked11.set("Choose Option")

clicked12 = tk.StringVar(root3)
clicked12.set("Choose Option")

clicked13 = tk.StringVar(root3)
clicked13.set("Choose Option")

clicked14 = tk.StringVar(root3)
clicked14.set("Choose Option")


question10 = tk.Label(root3, text = "Do you or anyone in your household have speical needs \n (disabilities, elderly, etc)?")
question10.pack()

drop10 = tk.OptionMenu(root3,clicked10,"Yes", "No")
drop10.pack()

question11 = tk.Label(root3, text = "How many pets does your household have?")
question11.pack()

drop11 = tk.OptionMenu(root3,clicked11, "0", "1", "2", "3", "4", "5", "5+")
drop11.pack()

question12 = tk.Label(root3, text = "What would be your primary  mode of transportation \n in case of evacuation?")
question12.pack()

drop12 = tk.OptionMenu(root3,clicked12, "Car", "Bus", "Train", "Other", "I have no form of transporation")
drop12.pack()

question13 = tk.Label(root3, text = "Where would you shelter in case of evacuation?")
question13.pack()

drop13 = tk.OptionMenu(root3,clicked13, "In a second home located elsewhere", "With friends or family", "In a rented space (hotel, motel, etc)", "In an evacuation shelter", "Other", "I have no other place to evacuate to")
drop13.pack()

question14 = tk.Label(root3, text = "Do you have any past hurricane experience?")
question14.pack()

drop14 = tk.OptionMenu(root3,clicked14, "Yes", "No")
drop14.pack()


exit_button = tk.Button(root3, text = "Submit", command = root3.destroy)
exit_button.pack(side=BOTTOM)


root3.mainloop()

# get user input for the category of hurricane
root1 = tk.Tk()
root1.title('Building and Storm Factors')
root1.geometry("500x400")

clicked4 = tk.StringVar(root1)
clicked4.set("Choose Option")


question4 = tk.Label(root1, text = "What category hurricane is predicted to strike?")
question4.pack()

drop4 = tk.OptionMenu(root1,clicked4, "Category 1", "Category 2", "Category 3", "Category 4", "Category 5")
drop4.pack()

response = requests.get('https://github.com/gfusco19/VR_V1/blob/main/windscale.png?raw=true')
img11 = Image.open(BytesIO(response.content))
img11 = img11.resize((400, 300))
tkimage11 = ImageTk.PhotoImage(img11)
tk.Label(root1, image=tkimage11).pack()

exit_button = tk.Button(root1, text = "Submit", command = root1.destroy)
exit_button.pack(side=BOTTOM)


root1.mainloop()

category = clicked4.get()
if category in ['Category 1']:
    category = 1
elif category in ['Category 2']:
    category = 2
elif category in ['Category 3']:
    category = 3
elif category in ['Category 4']:
    category = 4
elif category in ['Category 5']:
    category = 5
else:
    sys.exit("Please select valid hurricane category option")  
    
file = open("Hurricane_Category", "w")
category_string = str(category)
file.write(category_string)
file.flush()

### concrete block or wood frame 
root8 = tk.Tk()
root8.title('Building Factors')
root8.geometry("700x425")

clicked1 = tk.StringVar(root8)
clicked1.set("Choose Option")

question1 = tk.Label(root8, text = "Is your home wood frame or concrete block ?")
question1.pack()

drop1 = tk.OptionMenu(root8,clicked1,"Wood Frame", "Concrete Block")
drop1.pack()

response = requests.get('https://github.com/gfusco19/VR_V1/blob/main/concreteblockVSwoodframe.PNG?raw=true')
img4 = Image.open(BytesIO(response.content))
tkimage4 = ImageTk.PhotoImage(img4)
tk.Label(root8, image=tkimage4).pack()

exit_button = tk.Button(root8, text = "Submit", command = root8.destroy)
exit_button.pack()


root8.mainloop()


# get user input for roof material
root9 = tk.Tk()
root9.title('Building Factors')
root9.geometry("600x600")

clicked2 = tk.StringVar(root9)
clicked2.set("Choose Option")

question2 = tk.Label(root9, text = "What type of roof cover does your home have?")
question2.pack()

drop2 = tk.OptionMenu(root9,clicked2, "Asphalt Shingles", "Metal Roofing", "Concrete Tiles", "Clay Tiles")
drop2.pack()

response = requests.get('https://github.com/gfusco19/VR_V1/blob/main/RoofingOptions.PNG?raw=true')
img5 = Image.open(BytesIO(response.content))
tkimage5 = ImageTk.PhotoImage(img5)
tk.Label(root9, image=tkimage5).pack()

exit_button = tk.Button(root9, text = "Submit", command = root9.destroy)
exit_button.pack()


root9.mainloop()


# get user input for connections
root10 = tk.Tk()
root10.title('Building and Storm Factors')
root10.geometry("800x425")

clicked3 = tk.StringVar(root10)
clicked3.set("Choose Option")

question3 = tk.Label(root10, text = "Does your home have hurricane straps or toe nailing connections?")
question3.pack()

drop3 = tk.OptionMenu(root10,clicked3, "Hurricane Straps", "Toe Nailing")
drop3.pack()

response = requests.get('https://github.com/gfusco19/VR_V1/blob/main/ConnectionOptions.PNG?raw=true')
img9 = Image.open(BytesIO(response.content))
tkimage9 = ImageTk.PhotoImage(img9)
tk.Label(root10, image=tkimage9).pack()

exit_button = tk.Button(root10, text = "Submit", command = root10.destroy)
exit_button.pack()

root10.mainloop()

# user input for exposure category 
root11 = tk.Tk()
root11.title('Exposure Category')
root11.geometry("1000x350")

clicked19 = tk.StringVar(root11)
clicked19.set("Choose Option")

question19 = tk.Label(root11, text = "What is the exposure category or your household?")
question19.pack()

drop19 = tk.OptionMenu(root11, clicked19, "Urban", "Suburban", "Rural")
drop19.pack()

response = requests.get('https://github.com/gfusco19/VR_V1/blob/main/exposure.PNG?raw=true')
img19 = Image.open(BytesIO(response.content))
tkimage19 = ImageTk.PhotoImage(img19)
tk.Label(root11, image=tkimage19).pack()

exit_button = tk.Button(root11, text = "Submit", command = root11.destroy)
exit_button.pack(side=BOTTOM)

root11.mainloop()

# user input for vegetation density
root12 = tk.Tk()
root12.title('Vegetation Density')
root12.geometry("600x410")

clicked20 = tk.StringVar(root12)
clicked20.set("Choose Option")

question20 = tk.Label(root12, text = "What type of vegetation density surrounds your household?")
question20.pack()

drop20 = tk.OptionMenu(root12, clicked20, "High", "Moderate", "Low", "Very Low")
drop20.pack()

response = requests.get('https://github.com/gfusco19/VR_V1/blob/main/vegetationdensity.jpg?raw=true')
img20 = Image.open(BytesIO(response.content))
tkimage20 = ImageTk.PhotoImage(img20)
tk.Label(root12, image=tkimage20).pack()

exit_button = tk.Button(root12, text = "Submit", command = root12.destroy)
exit_button.pack()

root12.mainloop()

# user input for garage, windows and roof sheathing
root13 = tk.Tk()
root13.title('Openings and Sheathing')
root13.geometry("500x410")

clicked21 = tk.StringVar(root13)
clicked21.set("Choose Option")

clicked22 = tk.StringVar(root13)
clicked22.set("Choose Option")

clicked27 = tk.StringVar(root13)
clicked27.set("Choose Option")

clicked28 = tk.StringVar(root13)
clicked28.set("Choose Option")

clicked31 = tk.StringVar(root13)
clicked31.set("Choose Option")

question21 = tk.Label(root13, text = "What strength roof sheathing does your structure have?")
question21.pack()

drop21 = tk.OptionMenu(root13, clicked21, "High (8d with 6/6 nail pattern)", "Moderate (8d with 6/12 nail pattern)", "Low (6d with 6/12 nail pattern)")
drop21.pack()


question22 = tk.Label(root13, text = "Is your garage door braced or impact resistant?")
question22.pack()

drop22 = tk.OptionMenu(root13, clicked22, "Yes", "No")
drop22.pack()

question29 = tk.Label(root13, text = "Does your house have a basement?")
question29.pack()

drop29 = tk.OptionMenu(root13, clicked31, "Yes", "No")
drop29.pack()

question23 = tk.Label(root13, text = "Is your home located in a hurricane prone area?")
question23.pack()

drop23 = tk.OptionMenu(root13, clicked27, "Yes", "No")
drop23.pack()

question24 = tk.Label(root13, text = "Is your home located near any open water?")
question24.pack()

drop24 = tk.OptionMenu(root13, clicked28, "Yes", "No")
drop24.pack()

exit_button = tk.Button(root13, text = "Submit", command = root13.destroy)
exit_button.pack()

root13.mainloop()

hurricane_prone = clicked27.get()
if hurricane_prone in ['Yes']:
    hurricane_prone = 1
elif hurricane_prone in ['No']:
    hurricane_prone = 2
    
basement = clicked31.get()
if basement in ['Yes']:
    basement = 1
elif basement in ['No']:
    basement = 2
    
open_water = clicked28.get()
if open_water in ['Yes']:
    open_water = 1
elif open_water in ['No']:
    open_water = 2
    
exposure = clicked19.get()
if exposure in ['Urban']:
    exposure = 1
elif exposure in ['Suburban']:
    exposure = 2
elif exposure in ['Rural']:
    exposure = 3 
    
vegetation = clicked20.get()
if vegetation in ['High']:
    vegetation = 1
elif vegetation in ['Moderate']:
    vegetation = 2
elif vegetation in ['Low']:
    vegetation = 3
elif vegetation in ['Very Low']:
    vegetation = 4

if exposure == 1 or 2:
    exposure_category = 1 #B
elif vegetation == 1 or 2:
    exposure_category = 1 #B
elif exposure == 3 and hurricane_prone == 1:
    exposure_category = 2 #C
elif open_water == 1 and hurricane_prone == 1:
    expsore_category = 2 #C
elif exposure == 3 and hurricane_prone == 2:
    exposure_category = 3 #D
elif open_water == 1 and hurricane_prone == 2:
    exposure_category = 3 #D
else:
    exposure_category = 3
    

# input for location and escarpment
root14 = tk.Tk()
root14.title('Location')
root14.geometry("550x150")
question23 = tk.Label(root14, text = "Enter the decimal coordinates to your structure. You may find your coordinates using this link")
question23.pack()
question24 = tk.Label(root14, text = "https://www.whatsmygps.com/")
question24.pack()
question25 = tk.Label(root14, text = "Lattitude:")
question25.pack(side=LEFT)
entry1 = tk.Entry(root14)
entry1.pack(side=LEFT)
question26 = tk.Label(root14, text = "Longitude:")
question26.pack(side=LEFT)
entry2 = tk.Entry(root14)
entry2.pack(side=LEFT)

exit_button = tk.Button(root14, text = "Submit", command = writeCoordinates)
exit_button.pack(side=LEFT)


root14.mainloop()

arcpy.env.overwriteOutput = True
mxd = arcpy.mapping.MapDocument(r"C:\Users\giova\Dropbox\Research\Graduate School\contours_map.mxd")

mxd_H1 = arcpy.mapping.MapDocument(r"C:\Users\giova\Dropbox\Research\Graduate School\storm_surge_H1.mxd")
mxd_H2 = arcpy.mapping.MapDocument(r"C:\Users\giova\Dropbox\Research\Graduate School\storm_surge_H2.mxd")
mxd_H3 = arcpy.mapping.MapDocument(r"C:\Users\giova\Dropbox\Research\Graduate School\storm_surge_H3.mxd")
mxd_H4 = arcpy.mapping.MapDocument(r"C:\Users\giova\Dropbox\Research\Graduate School\storm_surge_H4.mxd")
mxd_H5 = arcpy.mapping.MapDocument(r"C:\Users\giova\Dropbox\Research\Graduate School\storm_surge_H5.mxd")

file1 = open("Hurricane_Category", "r+")
category = file1.readline()
category = float(category)

if category == 1:
    mxd2 = mxd_H1
elif category == 2:
    mxd2 = mxd_H2
elif category == 3:
    mxd2 = mxd_H3
elif category == 4:
    mxd2 = mxd_H4
elif category == 5:
    mxd2 = mxd_H5

df = arcpy.mapping.ListDataFrames(mxd,"*")[0]
df2 = arcpy.mapping.ListDataFrames(mxd2,"*")[0]

gp = arcgisscripting.create()
inTxt = r"C:\Users\giova\Dropbox\Research\Graduate School\Coordinates_up"
inSep = "."
point = r"C:\Users\giova\Dropbox\Research\Graduate School\point.shp"
gp.CreateFeaturesFromTextFile(inTxt, inSep, point, "#")
newlayer = arcpy.mapping.Layer(r"C:\Users\giova\Dropbox\Research\Graduate School\point.shp")

arcpy.mapping.AddLayer(df, newlayer, "AUTO_ARRANGE")
Layer = arcpy.mapping.ListLayers(mxd,'point',df)[0]
ext = Layer.getExtent()
df.panToExtent(ext)
df.scale = 50000
arcpy.mapping.ExportToPNG(mxd,r"C:\Users\giova\Dropbox\Research\Graduate School\contours_map_example.png")

arcpy.mapping.AddLayer(df2, newlayer, "AUTO_ARRANGE")
Layer2 = arcpy.mapping.ListLayers(mxd2,'point',df2)[0]
ext = Layer2.getExtent()
df2.panToExtent(ext)
df2.scale = 10000
arcpy.mapping.ExportToPNG(mxd2,r"C:\Users\giova\Dropbox\Research\Graduate School\hazard_map_image.png")



# topographic map
root15 = tk.Tk()
root15.title('Topographic Factor')
root15.geometry("750x1000")
root15.attributes('-fullscreen',True)

img = Image.open(r"C:\Users\giova\Dropbox\Research\Graduate School\contours_map_example.png")
img = img.crop((20,195,796,830))
tkimage = ImageTk.PhotoImage(img)
tk.Label(root15, image=tkimage).pack()

img2 = Image.open(r"C:\Users\giova\Dropbox\Research\Graduate School\feature.png")
img2 = img2.resize((550,200))
tkimage2 = ImageTk.PhotoImage(img2)
tk.Label(root15, image=tkimage2).pack()

clicked23 = tk.StringVar(root15)
clicked23.set("Choose Option")

clicked29 = tk.StringVar(root15)
clicked29.set("Choose Option")

question4 = tk.Label(root15, text = "\nIs your house located in the upper half of a hill or ridge \n or near the crest of an escarpment?")
question4.pack()

drop4 = tk.OptionMenu(root15,clicked23, "Yes", "No")
drop4.pack()

question5 = tk.Label(root15, text = "\nIs the feature your house located on a hill, ridge, or escarpment?")
question5.pack()

drop5 = tk.OptionMenu(root15,clicked29, "Hill", "Ridge", "Escarpment", "N/A")
drop5.pack()

exit_button = tk.Button(root15, text = "Submit", command = root15.destroy)
exit_button.pack()

root15.mainloop()

feature_type = clicked29.get()
if feature_type in ['Hill']:
    feature_type = 1
elif feature_type in ['Ridge']:
    feature_type = 2
elif feature_type in ['Escarpment']:
    feature_type = 3
elif feature_type in ['N/A']:
    feature_type = 4

if feature_type == 4:
    K_zt = 1.0

topo_1 = clicked23.get()
if topo_1 in ['No']:
    K_zt = 1.0
if topo_1 in ['Yes']:
    root15 = tk.Tk()
    root15.title('Topographic Factor')
    root15.geometry("750x800")
    root15.attributes('-fullscreen',True)
    
    img = Image.open(r"C:\Users\giova\Dropbox\Research\Graduate School\contours_map_example.png")
    img = img.crop((20,180,796,846))
    tkimage = ImageTk.PhotoImage(img)
    tk.Label(root15, image=tkimage).pack()
    
    img2 = Image.open(r"C:\Users\giova\Dropbox\Research\Graduate School\feature.png")
    img2 = img2.resize((550,200))
    tkimage2 = ImageTk.PhotoImage(img2)
    tk.Label(root15, image=tkimage2).pack()
    
    clicked24 = tk.StringVar(root15)
    clicked24.set("Choose Option")
    
    question4 = tk.Label(root15, text = "\nIs the hill, ridge or escarpment unobstructed by other topographic features of \n comparable height within two miles of the feature?")
    question4.pack()
    
    drop4 = tk.OptionMenu(root15,clicked24, "Yes", "No")
    drop4.pack()
    
    exit_button = tk.Button(root15, text = "Submit", command = root15.destroy)
    exit_button.pack()
    
    root15.mainloop()
    
    topo_2 = clicked24.get()
    if topo_2 in ['Yes']:
        root15 = tk.Tk()
        root15.title('Topographic Factor')
        root15.geometry("750x800")
        root15.attributes('-fullscreen',True)
        
        img = Image.open(r"C:\Users\giova\Dropbox\Research\Graduate School\contours_map_example.png")
        img = img.crop((20,180,796,846))
        tkimage = ImageTk.PhotoImage(img)
        tk.Label(root15, image=tkimage).pack()
        
        img2 = Image.open(r"C:\Users\giova\Dropbox\Research\Graduate School\feature.png")
        img2 = img2.resize((550,200))
        tkimage2 = ImageTk.PhotoImage(img2)
        tk.Label(root15, image=tkimage2).pack()
        
        question25 = tk.Label(root15, text = "Lh (Distance upwind of crest to where the difference in ground elevation is half the height of hill or escarpment):")
        question25.pack()
        entry3 = tk.Entry(root15)
        entry3.pack()
        question26 = tk.Label(root15, text = "H (Height of hill or escarpment relative to the upwind terrain):")
        question26.pack()
        entry4 = tk.Entry(root15)
        entry4.pack()
        question27 = tk.Label(root15, text = "z (Height above local ground level):")
        question27.pack()
        entry5 = tk.Entry(root15)
        entry5.pack()
        question28 = tk.Label(root15, text = "x (Distance (upwind or downwind) from the crest to the building site):")
        question28.pack()
        entry6 = tk.Entry(root15)
        entry6.pack()
        
        exit_button = tk.Button(root15, text = "Submit", command = submitAnswers)
        exit_button.pack()
        
        root15.mainloop()
        
    if topo_2 in ['No']:
        root15 = tk.Tk()
        root15.title('Topographic Factor')
        root15.geometry("750x800")
        root15.attributes('-fullscreen',True)
        
        img = Image.open(r"C:\Users\giova\Dropbox\Research\Graduate School\contours_map_example.png")
        img = img.crop((20,180,796,846))
        tkimage = ImageTk.PhotoImage(img)
        tk.Label(root15, image=tkimage).pack()
        
        img2 = Image.open(r"C:\Users\giova\Dropbox\Research\Graduate School\feature.png")
        img2 = img2.resize((550,200))
        tkimage2 = ImageTk.PhotoImage(img2)
        tk.Label(root15, image=tkimage2).pack()
        
        clicked26 = tk.StringVar(root15)
        clicked26.set("Choose Option")
        
        question4 = tk.Label(root15, text = "Does the hill, ridge or escarpment protrude above other topographic features within \n a two mile radius by a factor of two or more?")
        question4.pack()
        
        drop4 = tk.OptionMenu(root15,clicked26, "Yes", "No")
        drop4.pack()
        
        exit_button = tk.Button(root15, text = "Submit", command = root15.destroy)
        exit_button.pack()
        
        root15.mainloop()
        
        topo_3 = clicked26.get()
        if topo_3 in ['No']:
            K_zt = 1.0
        if topo_3 in ['Yes']:
            root15 = tk.Tk()
            root15.title('Topographic Factor')
            root15.geometry("750x800")
            root15.attributes('-fullscreen',True)
            
            img = Image.open(r"C:\Users\giova\Dropbox\Research\Graduate School\contours_map_example.png")
            img = img.crop((20,180,796,846))
            tkimage = ImageTk.PhotoImage(img)
            tk.Label(root15, image=tkimage).pack()
            
            img2 = Image.open(r"C:\Users\giova\Dropbox\Research\Graduate School\feature.png")
            img2 = img2.resize((550,200))
            tkimage2 = ImageTk.PhotoImage(img2)
            tk.Label(root15, image=tkimage2).pack()
            
            question25 = tk.Label(root15, text = "Lh (Distance upwind of crest to where the difference in ground elevation is half the height of hill or escarpment):")
            question25.pack()
            entry3 = tk.Entry(root15)
            entry3.pack()
            question26 = tk.Label(root15, text = "H (Height of hill or escarpment relative to the upwind terrain):")
            question26.pack()
            entry4 = tk.Entry(root15)
            entry4.pack()
            question27 = tk.Label(root15, text = "z (Height above local ground level):")
            question27.pack()
            entry5 = tk.Entry(root15)
            entry5.pack()
            question28 = tk.Label(root15, text = "x (Distance (upwind or downwind) from the crest to the building site):")
            question28.pack()
            entry6 = tk.Entry(root15)
            entry6.pack()
                
            exit_button = tk.Button(root15, text = "Submit", command = submitAnswers)
            exit_button.pack()
            
            root15.mainloop()

    

root16 = tk.Tk()
root16.title('Storm Surge')
root16.geometry("750x800")

img = Image.open(r"C:\Users\giova\Dropbox\Research\Graduate School\hazard_map_image.png")
img = img.crop((20,195,796,830))
tkimage = ImageTk.PhotoImage(img)
tk.Label(root16, image=tkimage).pack()

clicked30 = tk.StringVar(root16)
clicked30.set("Choose Option")

question5 = tk.Label(root16, text = "\nIn what map color is your house located?")
question5.pack()

drop5 = tk.OptionMenu(root16,clicked30, "White", "Blue", "Yellow", "Orange", "Red", "Striped")
drop5.pack()

exit_button = tk.Button(root16, text = "Submit", command = root16.destroy)
exit_button.pack()

root16.mainloop()

surge = clicked30.get()
if surge in ['White']:
    ds = 0
elif surge in ['Blue']:
    ds = round(random.uniform(0.01,3),2)
elif surge in ['Yellow']:
    ds = round(random.uniform(3.01,6),2)
elif surge in ['Orange']:
    ds = round(random.uniform(6.01,9),2)
elif surge in ['Red']:
    ds = round(random.uniform(9.01,18),2)
elif surge in ['Striped']:
    ds = round(random.uniform(9.01,18),2)
else:
    sys.exit("Please select valid surge category option") 
    

# translate user input to integer form
walls = clicked1.get()
if walls in ['Wood Frame']:
    walls = 1
elif walls in ['Concrete Block']:
    walls = 2
else:
    sys.exit("Please select valid framing option")
    
roof = clicked2.get()
if roof in ['Asphalt Shingles']:
    roof = 1
elif roof in ['Metal Roofing']:
    roof = 2
elif roof in ['Concrete Tiles']:
    roof = 3
elif roof in ['Clay Tiles']:
    roof = 4
else:
    sys.exit("Please select valid roof cover option")

connections = clicked3.get()
if connections in ['Hurricane Straps']:
    connections = 1
elif connections in ['Toe Nailing']:
    connections = 2
else:
    sys.exit("Please select valid connections option")  


sheath_strength = clicked21.get()
if sheath_strength in ['High (8d with 6/6 nail pattern)']:
    sheath_strength = 1
elif sheath_strength in ['Moderate (8d with 6/12 nail pattern)']:
    sheath_strength = 2
elif sheath_strength in ['Low (6d with 6/12 nail pattern)']:
    sheath_strength = 3
else:
    sys.exit("Please select valid sheathing strenght option") 

garage_strength = clicked22.get()
if garage_strength in ['Yes']:
    garage_strength = 1
elif garage_strength in ['No']:
    garage_strength = 2
else:
    sys.exit("Please select valid garage strength option") 

# randomize the wind direction
direction = round(random.uniform(1,8),0)


# predefined values for wall height, roof pitch, length and width
height = 10
roof_pitch = 22.62
length = 60
width = 44
a = width*0.1

# determine a randomized wind speed based on the category of storm 
if category == 1:
    wind = random.uniform(74,95)
elif category == 2:
    wind = random.uniform(96,110)
elif category == 3:
    wind = random.uniform(111,129)
elif category == 4:
    wind = random.uniform(130,156)
elif category == 5:
    wind = random.uniform(157,185)

# randomize the pressure coefficients
# matrix of pressure coefficients = [internal pressure, roof zone 1, roof zone 2, roof zone 3, wall C&C winward,
# wall C&C side leading, wall C&C side, wall C&C leeward, MWFRS Case A 1, MWFRS Case A 2, MWFRS Case A 3, 
# MWFRS Case A 4, MWFRS Case A 1E, MWFRS Case A 2E, MWFRS Case A 3E,
# MWFRS Case A 4E, MWFRS Case B 1, MWFRS Case B 2, MWFRS Case B 3, 
# MWFRS Case B 4, MWFRS Case B 5, MWFRS Case B 6, MWFRS Case B 1E, MWFRS Case B 2E, MWFRS Case B 3E,
# MWFRS Case B 4E, MWFRS Case B 5E, MWFRS Case B 6E]
z = np.random.normal(0, 1, size = (1,28))
cp = [0.18, -0.9, -2.1, -2.1, 1.0, -1.4, -1.1, -0.8, 0.538, -0.456, -0.467, -0.414, 0.771, -0.722, -0.648, -0.598, -0.450, -0.690, -0.370, -0.450, 0.400, -0.290, -0.480, -1.070, -0.530, -0.480, 0.610, -0.430]
cp_rand = ((z*0.1)+1)*cp

# velocity pressure of roof mean height calculation
qh = 0.00256*0.85*K_zt*wind**2 

# design pressure calculation for roof sheathing
p_sheath_zone1 = qh*0.8*(cp_rand[0,1]-cp_rand[0,0])
p_sheath_zone2 = qh*0.8*(cp_rand[0,2]-cp_rand[0,0])
p_sheath_zone3 = qh*0.8*(cp_rand[0,3]-cp_rand[0,0])

# design pressure calculation for roof cover
p_cover_zone1 = qh*0.8*(cp_rand[0,1]-0)
p_cover_zone2 = qh*0.8*(cp_rand[0,2]-0)
p_cover_zone3 = qh*0.8*(cp_rand[0,3]-0)


# design pressure calculations for walls (MWFRS)
p_caseA1_MWFRS = qh*0.8*(0.85*cp_rand[0,8]-cp_rand[0,0])
p_caseA2_MWFRS = qh*0.8*(0.85*cp_rand[0,9]-cp_rand[0,0])
p_caseA3_MWFRS = qh*0.8*(0.85*cp_rand[0,10]-cp_rand[0,0])
p_caseA4_MWFRS = qh*0.8*(0.85*cp_rand[0,11]-cp_rand[0,0])
p_caseA1E_MWFRS = qh*0.8*(0.85*cp_rand[0,12]-cp_rand[0,0])
p_caseA2E_MWFRS = qh*0.8*(0.85*cp_rand[0,13]-cp_rand[0,0])
p_caseA3E_MWFRS = qh*0.8*(0.85*cp_rand[0,14]-cp_rand[0,0])
p_caseA4E_MWFRS = qh*0.8*(0.85*cp_rand[0,15]-cp_rand[0,0])

p_caseB1_MWFRS = qh*0.8*(0.85*cp_rand[0,16]-cp_rand[0,0])
p_caseB2_MWFRS = qh*0.8*(0.85*cp_rand[0,17]-cp_rand[0,0])
p_caseB3_MWFRS = qh*0.8*(0.85*cp_rand[0,18]-cp_rand[0,0])
p_caseB4_MWFRS = qh*0.8*(0.85*cp_rand[0,19]-cp_rand[0,0])
p_caseB5_MWFRS = qh*0.8*(0.85*cp_rand[0,20]-cp_rand[0,0])
p_caseB6_MWFRS = qh*0.8*(0.85*cp_rand[0,21]-cp_rand[0,0])
p_caseB1E_MWFRS = qh*0.8*(0.85*cp_rand[0,22]-cp_rand[0,0])
p_caseB2E_MWFRS = qh*0.8*(0.85*cp_rand[0,23]-cp_rand[0,0])
p_caseB3E_MWFRS = qh*0.8*(0.85*cp_rand[0,24]-cp_rand[0,0])
p_caseB4E_MWFRS = qh*0.8*(0.85*cp_rand[0,25]-cp_rand[0,0])
p_caseB5E_MWFRS = qh*0.8*(0.85*cp_rand[0,26]-cp_rand[0,0])
p_caseB6E_MWFRS = qh*0.8*(0.85*cp_rand[0,27]-cp_rand[0,0])


# design pressure calculations for walls and openings (C&C)
p_windward_CC = qh*0.8*(cp_rand[0,4]-cp_rand[0,0])
p_sideleading_CC = qh*0.8*(cp_rand[0,5]-cp_rand[0,0])
p_side_CC = qh*0.8*(cp_rand[0,6]-cp_rand[0,0])
p_leeward_CC = qh*0.8*(cp_rand[0,7]-cp_rand[0,0])

# impact for windows 
N_A = 0
A = scipy.stats.norm(135,15).cdf(wind)
B = 0.0016*wind
D = scipy.stats.norm(70,10).cdf(wind)
vegetation_factor = 0.0032*(wind**2)-0.4948*wind+30.57
vegetation_factor = vegetation_factor/100


# application of loads to components based on wind direction
if direction == 1:
    cover_loads = [p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2,
                   p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2,
                   p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2,
                   p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2,
                   p_cover_zone3, p_cover_zone3, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone3,
                   p_cover_zone3, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone3, p_cover_zone3]
    
    sheath_loads = [p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2,
                   p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2,
                   p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2,
                   p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2,
                   p_sheath_zone3, p_sheath_zone3, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone3,
                   p_sheath_zone3, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone3, p_sheath_zone3]
    
    if exposure == 1:
        N_A = N_A + 768*(1/8)
    elif exposure == 2:
        N_A = N_A + 768*(1/8)
    elif exposure == 3:
        N_A = N_A + 385*(0/4)
    
    if vegetation == 1:
        N_A = N_A + 23100*vegetation_factor*(1/8)
    elif vegetation == 2:
        N_A = N_A + 2200*vegetation_factor*(1/8)
    elif vegetation == 3:
        N_A = N_A + 420*vegetation_factor*(1/8)    
    elif vegetation == 4:
        N_A = N_A + 45*vegetation_factor*(1/8)        
        
    front_window_loads = [p_windward_CC, p_windward_CC, p_windward_CC]
    front_door_load = p_windward_CC
    garage_door_load = p_windward_CC
    leftside_window_loads = [p_sideleading_CC, p_side_CC, p_side_CC, p_side_CC]
    rightside_window_loads = [p_sideleading_CC, p_side_CC, p_side_CC, p_side_CC]
    back_window_loads = [p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC]
    back_door_load = p_leeward_CC
    prob_front = 1 - math.exp(-A*N_A*B*((3.5*5)/(60*10))*D)
    prob_right = 0
    prob_left = 0
    prob_back = 0
    
elif direction == 2:
    cover_loads = [p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone3, p_cover_zone3, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2,
                   p_cover_zone3, p_cover_zone3, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2,
                   p_cover_zone3, p_cover_zone3, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2]
    
    sheath_loads = [p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone3, p_sheath_zone3, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2,
                   p_sheath_zone3, p_sheath_zone3, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2,
                   p_sheath_zone3, p_sheath_zone3, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2]

    if exposure == 1:
        N_A = N_A + 768*(1.5/8)
    elif exposure == 2:
        N_A = N_A + 768*(1.5/8)
    elif exposure == 3:
        N_A = N_A + 385*(1/4)
    
    if vegetation == 1:
        N_A = N_A + 23100*vegetation_factor*(1.5/8)
    elif vegetation == 2:
        N_A = N_A + 2200*vegetation_factor*(1.5/8)
    elif vegetation == 3:
        N_A = N_A + 420*vegetation_factor*(1.5/8)    
    elif vegetation == 4:
        N_A = N_A + 45*vegetation_factor*(1.5/8)

    front_window_loads = [p_windward_CC, p_windward_CC, p_windward_CC]
    front_door_load = p_windward_CC
    garage_door_load = p_windward_CC
    leftside_window_loads = [p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC]
    rightside_window_loads = [p_sideleading_CC, p_side_CC, p_side_CC, p_side_CC]
    back_window_loads = [p_sideleading_CC, p_side_CC, p_side_CC, p_side_CC]
    back_door_load = p_side_CC
    prob_front = 1 - math.exp(-A*N_A*B*((3.5*5)/((60*10)+(44*10)+(44*0.5*9.167))*D))
    prob_right = 0
    prob_left = 1 - math.exp(-A*N_A*B*((3.5*3.5)/((60*10)+(44*10)+(44*0.5*9.167))*D))
    prob_back = 0
    
elif direction == 3:
    cover_loads = [p_cover_zone3, p_cover_zone3, p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone3, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone3, p_cover_zone3, p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone3, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone3, p_cover_zone3, p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone3, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone3, p_cover_zone3, p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone3, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1]
    
    sheath_loads = [p_sheath_zone3, p_sheath_zone3, p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone3, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone3, p_sheath_zone3, p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone3, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone3, p_sheath_zone3, p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone3, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone3, p_sheath_zone3, p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone3, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1]

    if exposure == 1:
        N_A = N_A + 768*(1/8)
    elif exposure == 2:
        N_A = N_A + 768*(1/8)
    elif exposure == 3:
        N_A = N_A + 385*(0/4)
    
    if vegetation == 1:
        N_A = N_A + 23100*vegetation_factor*(1/8)
    elif vegetation == 2:
        N_A = N_A + 2200*vegetation_factor*(1/8)
    elif vegetation == 3:
        N_A = N_A + 420*vegetation_factor*(1/8)    
    elif vegetation == 4:
        N_A = N_A + 45*vegetation_factor*(1/8)
    
    front_window_loads = [p_side_CC, p_side_CC, p_side_CC]
    front_door_load = p_side_CC
    garage_door_load = p_side_CC
    leftside_window_loads = [p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC]
    rightside_window_loads = [p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC]
    back_window_loads = [p_sideleading_CC, p_side_CC, p_side_CC, p_side_CC]
    back_door_load = p_side_CC
    prob_front = 0
    prob_right = 0
    prob_left = 1 - math.exp(-A*N_A*B*((3.5*3.5)/((44*10)+(44*0.5*9.167))*D))
    prob_back = 0
    
elif direction == 4:
    cover_loads = [p_cover_zone3, p_cover_zone3, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2,
                   p_cover_zone3, p_cover_zone3, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2,
                   p_cover_zone3, p_cover_zone3, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2,
                   p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1]
    
    sheath_loads = [p_sheath_zone3, p_sheath_zone3, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2,
                   p_sheath_zone3, p_sheath_zone3, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2,
                   p_sheath_zone3, p_sheath_zone3, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2,
                   p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1]

    if exposure == 1:
        N_A = N_A + 768*(1.5/8)
    elif exposure == 2:
        N_A = N_A + 768*(1.5/8)
    elif exposure == 3:
        N_A = N_A + 385*(1/4)
    
    if vegetation == 1:
        N_A = N_A + 23100*vegetation_factor*(1.5/8)
    elif vegetation == 2:
        N_A = N_A + 2200*vegetation_factor*(1.5/8)
    elif vegetation == 3:
        N_A = N_A + 420*vegetation_factor*(1.5/8)    
    elif vegetation == 4:
        N_A = N_A + 45*vegetation_factor*(1.5/8)

    front_window_loads = [p_side_CC, p_side_CC, p_side_CC]
    front_door_load = p_side_CC
    garage_door_load = p_side_CC
    leftside_window_loads = [p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC]
    rightside_window_loads = [p_sideleading_CC, p_side_CC, p_side_CC, p_side_CC]
    back_window_loads = [p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC]
    back_door_load = p_windward_CC
    prob_front = 0
    prob_right = 0
    prob_left = 1 - math.exp(-A*N_A*B*((3.5*3.5)/((60*10)+(44*10)+(44*0.5*9.167))*D))
    prob_back = 1 - math.exp(-A*N_A*B*((3.5*5)/((60*10)+(44*10)+(44*0.5*9.167))*D))

elif direction == 5:
    cover_loads = [p_cover_zone3, p_cover_zone3, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone3,
                   p_cover_zone3, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone3, p_cover_zone3,
                   p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2,
                   p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2,
                   p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2,
                   p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1]
    
    sheath_loads = [p_sheath_zone3, p_sheath_zone3, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone3,
                   p_sheath_zone3, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone3, p_sheath_zone3,
                   p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2,
                   p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2,
                   p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2,
                   p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1]

    if exposure == 1:
        N_A = N_A + 768*(1/8)
    elif exposure == 2:
        N_A = N_A + 768*(1/8)
    elif exposure == 3:
        N_A = N_A + 385*(0/4)
    
    if vegetation == 1:
        N_A = N_A + 23100*vegetation_factor*(1/8)
    elif vegetation == 2:
        N_A = N_A + 2200*vegetation_factor*(1/8)
    elif vegetation == 3:
        N_A = N_A + 420*vegetation_factor*(1/8)    
    elif vegetation == 4:
        N_A = N_A + 45*vegetation_factor*(1/8)
    
    front_window_loads = [p_leeward_CC, p_leeward_CC, p_leeward_CC]
    front_door_load = p_leeward_CC
    garage_door_load = p_leeward_CC
    leftside_window_loads = [p_sideleading_CC, p_side_CC, p_side_CC, p_side_CC]
    rightside_window_loads = [p_sideleading_CC, p_side_CC, p_side_CC, p_side_CC]
    back_window_loads = [p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC]
    back_door_load = p_windward_CC
    prob_front = 0
    prob_right = 0
    prob_left = 0
    prob_back = 1 - math.exp(-A*N_A*B*((3.5*5)/((60*10))*D))
    
elif direction == 6:
    cover_loads = [p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone3, p_cover_zone3,
                   p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone3, p_cover_zone3,
                   p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone3, p_cover_zone3,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1]
    
    sheath_loads = [p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone3, p_sheath_zone3,
                   p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone3, p_sheath_zone3,
                   p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone3, p_sheath_zone3,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1]

    if exposure == 1:
        N_A = N_A + 768*(1.5/8)
    elif exposure == 2:
        N_A = N_A + 768*(1.5/8)
    elif exposure == 3:
        N_A = N_A + 385*(1/4)
    
    if vegetation == 1:
        N_A = N_A + 23100*vegetation_factor*(1.5/8)
    elif vegetation == 2:
        N_A = N_A + 2200*vegetation_factor*(1.5/8)
    elif vegetation == 3:
        N_A = N_A + 420*vegetation_factor*(1.5/8)    
    elif vegetation == 4:
        N_A = N_A + 45*vegetation_factor*(1.5/8)
    
    front_window_loads = [p_side_CC, p_side_CC, p_side_CC]
    front_door_load = p_side_CC
    garage_door_load = p_side_CC
    leftside_window_loads = [p_sideleading_CC, p_side_CC, p_side_CC, p_side_CC]
    rightside_window_loads = [p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC]
    back_window_loads = [p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC]
    back_door_load = p_windward_CC
    prob_front = 0
    prob_right = 1 - math.exp(-A*N_A*B*((3.5*3.5)/((60*10)+(44*10)+(44*0.5*9.167))*D))
    prob_left = 0
    prob_back = 1 - math.exp(-A*N_A*B*((3.5*5)/((60*10)+(44*10)+(44*0.5*9.167))*D))
    
elif direction == 7:
    cover_loads = [p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone3,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2, p_cover_zone3, p_cover_zone3,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone3,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2, p_cover_zone3, p_cover_zone3,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone3,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2, p_cover_zone3, p_cover_zone3,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone3,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2, p_cover_zone3, p_cover_zone3]
    
    sheath_loads = [p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone3,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2, p_sheath_zone3, p_sheath_zone3,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone3,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2, p_sheath_zone3, p_sheath_zone3,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone3,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2, p_sheath_zone3, p_sheath_zone3,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone3,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2, p_sheath_zone3, p_sheath_zone3]
  
    if exposure == 1:
        N_A = N_A + 768*(1/8)
    elif exposure == 2:
        N_A = N_A + 768*(1/8)
    elif exposure == 3:
        N_A = N_A + 385*(0/4)
    
    if vegetation == 1:
        N_A = N_A + 23100*vegetation_factor*(1/8)
    elif vegetation == 2:
        N_A = N_A + 2200*vegetation_factor*(1/8)
    elif vegetation == 3:
        N_A = N_A + 420*vegetation_factor*(1/8)    
    elif vegetation == 4:
        N_A = N_A + 45*vegetation_factor*(1/8)    
    
    front_window_loads = [p_side_CC, p_side_CC, p_side_CC]
    front_door_load = p_side_CC
    garage_door_load = p_side_CC
    leftside_window_loads = [p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC]
    rightside_window_loads = [p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC]
    back_window_loads = [p_sideleading_CC, p_side_CC, p_side_CC, p_side_CC]
    back_door_load = p_side_CC
    prob_front = 0
    prob_right = 1 - math.exp(-A*N_A*B*((3.5*3.5)/((44*10)+(44*0.5*9.167))*D))
    prob_left = 0
    prob_back = 0
    
elif direction == 8:
    cover_loads = [p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2,
                   p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone3, p_cover_zone3,
                   p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone3, p_cover_zone3,
                   p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone3, p_cover_zone3]
    
    sheath_loads = [p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2,
                   p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone3, p_sheath_zone3,
                   p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone3, p_sheath_zone3,
                   p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone3, p_sheath_zone3]

    if exposure == 1:
        N_A = N_A + 768*(1.5/8)
    elif exposure == 2:
        N_A = N_A + 768*(1.5/8)
    elif exposure == 3:
        N_A = N_A + 385*(1/4)
    
    if vegetation == 1:
        N_A = N_A + 23100*vegetation_factor*(1.5/8)
    elif vegetation == 2:
        N_A = N_A + 2200*vegetation_factor*(1.5/8)
    elif vegetation == 3:
        N_A = N_A + 420*vegetation_factor*(1.5/8)    
    elif vegetation == 4:
        N_A = N_A + 45*vegetation_factor*(1.5/8)

    front_window_loads = [p_windward_CC, p_windward_CC, p_windward_CC]
    front_door_load = p_windward_CC
    garage_door_load = p_windward_CC
    leftside_window_loads = [p_sideleading_CC, p_side_CC, p_side_CC, p_side_CC]
    rightside_window_loads = [p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC]
    back_window_loads = [p_sideleading_CC, p_side_CC, p_side_CC, p_side_CC]
    back_door_load = p_side_CC
    prob_front = 1 - math.exp(-A*N_A*B*((3.5*5)/((60*10)+(44*10)+(44*0.5*9.167))*D))
    prob_right = 1 - math.exp(-A*N_A*B*((3.5*3.5)/((60*10)+(44*10)+(44*0.5*9.167))*D))
    prob_left = 0
    prob_back = 0


# sheathing capacities
if sheath_strength == 1:
    sheath_mean_capacity = 181.9
elif sheath_strength == 2:
    sheath_mean_capacity = 103.0
elif sheath_strength == 3:
    sheath_mean_capacity = 54.6
sheath_COV = 0.11
sheath_std = sheath_COV*sheath_mean_capacity
upper_sheath_limit = sheath_mean_capacity + 2*sheath_std
lower_sheath_limit = sheath_mean_capacity - 2*sheath_std
sheath_capacity = np.random.lognormal(sheath_mean_capacity, sheath_std, size = (96))

# remove any capacities that are outside of two standard deviations from the mean
too_high_indices = np.where(sheath_capacity > upper_sheath_limit)
while np.any(too_high_indices):
    sheath_capacity[too_high_indices] = np.random.normal(
        sheath_mean_capacity, sheath_std, size=len(too_high_indices))
    too_high_indices = np.where(sheath_capacity > upper_sheath_limit)

too_low_indices = np.where(sheath_capacity < lower_sheath_limit)
while np.any(too_low_indices):
    sheath_capacity[too_low_indices] = np.random.normal(
        sheath_mean_capacity, sheath_std, size=len(too_low_indices))
    too_low_indices = np.where(sheath_capacity < lower_sheath_limit)

    # multiply loads by -1 (because uplifts were negative)
sheath_loads = np.array(sheath_loads)*-1

    # create a matrix with an element for each sheathing component and assign all values to be 1
    # 1 = not failed, 0 = failed
    # if the load is greater than the capacity, replace the 1 with a 0
failed_sheath = np.full(96, 1, dtype = int)
for i in range(len(failed_sheath)):
    if sheath_loads[i] > sheath_capacity[i]:
        failed_sheath[i] = 0

# cover capacities
if roof == 1:
    cover_mean_capacity = 75.4
    cover_COV = 0.4
    cover_std = cover_COV*cover_mean_capacity
    upper_cover_limit = cover_mean_capacity + 2*cover_std
    lower_cover_limit = cover_mean_capacity - 2*cover_std
    cover_capacity = np.random.normal(cover_mean_capacity, cover_std, size = (96))
    
    too_high_indices = np.where(cover_capacity > upper_cover_limit)
    while np.any(too_high_indices):
        cover_capacity[too_high_indices] = np.random.normal(
            cover_mean_capacity, cover_std, size=len(too_high_indices))
        too_high_indices = np.where(cover_capacity > upper_cover_limit)

    too_low_indices = np.where(cover_capacity < lower_cover_limit)
    while np.any(too_low_indices):
        cover_capacity[too_low_indices] = np.random.normal(
            cover_mean_capacity, cover_std, size=len(too_low_indices))
        too_low_indices = np.where(cover_capacity < lower_cover_limit)
elif roof == 2: 
    cover_mean_capacity = 176
    cover_COV = 0.4
    cover_std = cover_COV*cover_mean_capacity
    upper_cover_limit = cover_mean_capacity + 2*cover_std
    lower_cover_limit = cover_mean_capacity - 2*cover_std
    cover_capacity = np.random.normal(cover_mean_capacity, cover_std, size = (96))
    
    too_high_indices = np.where(cover_capacity > upper_cover_limit)
    while np.any(too_high_indices):
        cover_capacity[too_high_indices] = np.random.normal(
            cover_mean_capacity, cover_std, size=len(too_high_indices))
        too_high_indices = np.where(cover_capacity > upper_cover_limit)

    too_low_indices = np.where(cover_capacity < lower_cover_limit)
    while np.any(too_low_indices):
        cover_capacity[too_low_indices] = np.random.normal(
            cover_mean_capacity, cover_std, size=len(too_low_indices))
        too_low_indices = np.where(cover_capacity < lower_cover_limit)
elif roof == 3:
    cover_mean_capacity = 152.9
    cover_COV = 0.4
    cover_std = cover_COV*cover_mean_capacity
    upper_cover_limit = cover_mean_capacity + 2*cover_std
    lower_cover_limit = cover_mean_capacity - 2*cover_std
    cover_capacity = np.random.normal(cover_mean_capacity, cover_std, size = (96))
    
    too_high_indices = np.where(cover_capacity > upper_cover_limit)
    while np.any(too_high_indices):
        cover_capacity[too_high_indices] = np.random.normal(
            cover_mean_capacity, cover_std, size=len(too_high_indices))
        too_high_indices = np.where(cover_capacity > upper_cover_limit)

    too_low_indices = np.where(cover_capacity < lower_cover_limit)
    while np.any(too_low_indices):
        cover_capacity[too_low_indices] = np.random.normal(
            cover_mean_capacity, cover_std, size=len(too_low_indices))
        too_low_indices = np.where(cover_capacity < lower_cover_limit)
elif roof == 4:
    cover_mean_capacity = 124.2
    cover_COV = 0.4
    cover_std = cover_COV*cover_mean_capacity
    upper_cover_limit = cover_mean_capacity + 2*cover_std
    lower_cover_limit = cover_mean_capacity - 2*cover_std
    cover_capacity = np.random.normal(cover_mean_capacity, cover_std, size = (96))
    
    too_high_indices = np.where(cover_capacity > upper_cover_limit)
    while np.any(too_high_indices):
        cover_capacity[too_high_indices] = np.random.normal(
            cover_mean_capacity, cover_std, size=len(too_high_indices))
        too_high_indices = np.where(cover_capacity > upper_cover_limit)

    too_low_indices = np.where(cover_capacity < lower_cover_limit)
    while np.any(too_low_indices):
        cover_capacity[too_low_indices] = np.random.normal(
            cover_mean_capacity, cover_std, size=len(too_low_indices))
        too_low_indices = np.where(cover_capacity < lower_cover_limit)

cover_loads = np.array(cover_loads)*-1

failed_cover = np.full(96, 1, dtype = int)
for i in range(len(failed_cover)):
    if cover_loads[i] > cover_capacity[i]:
        failed_cover[i] = 0
    elif failed_sheath[i] == 0:
        failed_cover[i] = 0
        
if roof == 3:
    D_cover = scipy.stats.norm(114.75,0.75).cdf(wind)
    prob_cover = 1 - math.exp(-A*N_A*B*((4*8)/((60*24))*D_cover))
elif roof == 4:
    D_cover = scipy.stats.norm(95.2,2.67).cdf(wind)
    prob_cover = 1 - math.exp(-A*N_A*B*((4*8)/((60*24))*D_cover))
else:
    prob_cover = 0

if direction == 1:
    prob_front_cover = np.full(48,prob_cover)
    prob_back_cover = np.full(48,0)
elif direction == 2:
    prob_front_cover = np.full(48,prob_cover)
    prob_back_cover = np.full(48,0)
elif direction == 3:
    prob_front_cover = np.full(48,0)
    prob_back_cover = np.full(48,0)
elif direction == 4:
    prob_front_cover = np.full(48,0)
    prob_back_cover = np.full(48,prob_cover)
elif direction == 5:
    prob_front_cover = np.full(48,0)
    prob_back_cover = np.full(48,prob_cover)
elif direction == 6:
    prob_front_cover = np.full(48,0)
    prob_back_cover = np.full(48,prob_cover)
elif direction == 7:
    prob_front_cover = np.full(48,0)
    prob_back_cover = np.full(48,0)    
elif direction == 8:
    prob_front_cover = np.full(48,prob_cover)
    prob_back_cover = np.full(48,0)
    
prob_total_cover = np.concatenate([prob_front_cover, prob_back_cover])
cover_rand = np.random.rand(96)
for i in range(len(failed_cover)):
    if cover_rand[i] < prob_total_cover[i]:
        failed_cover[i] = 0

# opening capacities
# doors
door_mean_capacity = 100
door_COV = 0.2
door_std = door_COV*door_mean_capacity
upper_door_limit = door_mean_capacity + 2*door_std
lower_door_limit = door_mean_capacity - 2*door_std
door_capacity = np.random.normal(door_mean_capacity, door_std, size = (2))

too_high_indices = np.where(door_capacity > upper_door_limit)
while np.any(too_high_indices):
    door_capacity[too_high_indices] = np.random.normal(
        door_mean_capacity, door_std, size=len(too_high_indices))
    too_high_indices = np.where(door_capacity > upper_door_limit)

too_low_indices = np.where(door_capacity < lower_door_limit)
while np.any(too_low_indices):
    door_capacity[too_low_indices] = np.random.normal(
        door_mean_capacity, door_std, size=len(too_low_indices))
    too_low_indices = np.where(door_capacity < lower_door_limit)

front_door_load = abs(front_door_load)
back_door_load = abs(back_door_load)

if front_door_load > door_capacity[0]:
    front_door_fail = 0
elif front_door_load < door_capacity[0]:
    front_door_fail = 1

if back_door_load > door_capacity[1]:
    back_door_fail = 0
elif back_door_load < door_capacity[1]:
    back_door_fail = 1
    
# garage door
if garage_strength == 1:
    garage_mean_capacity = 20
elif garage_strength == 2:
    garage_mean_capacity = 10
garage_COV = 0.2
garage_std = garage_COV*garage_mean_capacity
upper_garage_limit = garage_mean_capacity + 2*garage_std
lower_garage_limit = garage_mean_capacity - 2*garage_std
garage_capacity = np.random.normal(garage_mean_capacity, garage_std, size = (1))

too_high_indices = np.where(garage_capacity > upper_garage_limit)
while np.any(too_high_indices):
    garage_capacity[too_high_indices] = np.random.normal(
        garage_mean_capacity, garage_std, size=len(too_high_indices))
    too_high_indices = np.where(garage_capacity > upper_garage_limit)

too_low_indices = np.where(garage_capacity < lower_garage_limit)
while np.any(too_low_indices):
    garage_capacity[too_low_indices] = np.random.normal(
        garage_mean_capacity, garage_std, size=len(too_low_indices))
    too_low_indices = np.where(garage_capacity < lower_garage_limit)

garage_door_load = abs(garage_door_load)

if garage_door_load > garage_capacity:
    garage_fail = 0
elif garage_door_load < garage_capacity:
    garage_fail = 1

# small windows
sidewindow_mean_capacity = 104.4
sidewindow_COV = 0.2
sidewindow_std = sidewindow_COV*sidewindow_mean_capacity
upper_sidewindow_limit = sidewindow_mean_capacity + 2*sidewindow_std
lower_sidewindow_limit = sidewindow_mean_capacity - 2*sidewindow_std
leftsidewindow_capacity = np.random.normal(sidewindow_mean_capacity, sidewindow_std, size = (4))
rightsidewindow_capacity = np.random.normal(sidewindow_mean_capacity, sidewindow_std, size = (4))

too_high_indices = np.where(leftsidewindow_capacity > upper_sidewindow_limit)
while np.any(too_high_indices):
    leftsidewindow_capacity[too_high_indices] = np.random.normal(
        sidewindow_mean_capacity, sidewindow_std, size=len(too_high_indices))
    too_high_indices = np.where(leftsidewindow_capacity > upper_sidewindow_limit)

too_low_indices = np.where(leftsidewindow_capacity < lower_sidewindow_limit)
while np.any(too_low_indices):
    leftsidewindow_capacity[too_low_indices] = np.random.normal(
        sidewindow_mean_capacity, sidewindow_std, size=len(too_low_indices))
    too_low_indices = np.where(leftsidewindow_capacity < lower_sidewindow_limit)
    
too_high_indices = np.where(rightsidewindow_capacity > upper_sidewindow_limit)
while np.any(too_high_indices):
    rightsidewindow_capacity[too_high_indices] = np.random.normal(
        sidewindow_mean_capacity, sidewindow_std, size=len(too_high_indices))
    too_high_indices = np.where(rightsidewindow_capacity > upper_sidewindow_limit)

too_low_indices = np.where(rightsidewindow_capacity < lower_sidewindow_limit)
while np.any(too_low_indices):
    rightsidewindow_capacity[too_low_indices] = np.random.normal(
        sidewindow_mean_capacity, sidewindow_std, size=len(too_low_indices))
    too_low_indices = np.where(rightsidewindow_capacity < lower_sidewindow_limit)

leftsidewindow_loads = np.abs(leftside_window_loads)
rightsidewindow_loads = np.abs(rightside_window_loads)

failed_leftwindows = np.full(4, 1)
for i in range(len(failed_leftwindows)):
    if leftsidewindow_loads[i] > leftsidewindow_capacity[i]:
        failed_leftwindows[i] = 0
failed_rightwindows = np.full(4, 1)
for i in range(len(failed_rightwindows)):
    if rightsidewindow_loads[i] > rightsidewindow_capacity[i]:
        failed_rightwindows[i] = 0  
 
right_rand = np.random.rand(4)
left_rand = np.random.rand(4)

for i in range(len(failed_leftwindows)):
    if left_rand[i] < prob_left:
        failed_leftwindows[i] = 0
for i in range(len(failed_rightwindows)):
    if right_rand[i] < prob_right:
        failed_rightwindows[i] = 0
 
# medium windows
mediumwindow_mean_capacity = 69.6
mediumwindow_COV = 0.2
mediumwindow_std = mediumwindow_COV*mediumwindow_mean_capacity
upper_mediumwindow_limit = mediumwindow_mean_capacity + 2*mediumwindow_std
lower_mediumwindow_limit = mediumwindow_mean_capacity - 2*mediumwindow_std
front_mediumwindow_capacity = np.random.normal(mediumwindow_mean_capacity, mediumwindow_std, size = (3))
back_mediumwindow_capacity = np.random.normal(mediumwindow_mean_capacity, mediumwindow_std, size = (4))

too_high_indices = np.where(front_mediumwindow_capacity > upper_mediumwindow_limit)
while np.any(too_high_indices):
    front_mediumwindow_capacity[too_high_indices] = np.random.normal(
        mediumwindow_mean_capacity, mediumwindow_std, size=len(too_high_indices))
    too_high_indices = np.where(front_mediumwindow_capacity > upper_mediumwindow_limit)

too_low_indices = np.where(front_mediumwindow_capacity < lower_mediumwindow_limit)
while np.any(too_low_indices):
    front_mediumwindow_capacity[too_low_indices] = np.random.normal(
        mediumwindow_mean_capacity, mediumwindow_std, size=len(too_low_indices))
    too_low_indices = np.where(front_mediumwindow_capacity < lower_mediumwindow_limit)

too_high_indices = np.where(back_mediumwindow_capacity > upper_mediumwindow_limit)
while np.any(too_high_indices):
    back_mediumwindow_capacity[too_high_indices] = np.random.normal(
        mediumwindow_mean_capacity, mediumwindow_std, size=len(too_high_indices))
    too_high_indices = np.where(back_mediumwindow_capacity > upper_mediumwindow_limit)

too_low_indices = np.where(back_mediumwindow_capacity < lower_mediumwindow_limit)
while np.any(too_low_indices):
    back_mediumwindow_capacity[too_low_indices] = np.random.normal(
        mediumwindow_mean_capacity, mediumwindow_std, size=len(too_low_indices))
    too_low_indices = np.where(back_mediumwindow_capacity < lower_mediumwindow_limit)

front_mediumwindow_loads = np.abs(front_window_loads)
back_mediumwindow_loads = np.abs(back_window_loads)

failed_frontwindows = np.full(3, 1)
for i in range(len(failed_frontwindows)):
    if front_mediumwindow_loads[i] > front_mediumwindow_capacity[i]:
        failed_frontwindows[i] = 0
failed_backwindows = np.full(4, 1)
for i in range(len(failed_backwindows)):
    if back_mediumwindow_loads[i] > back_mediumwindow_capacity[i]:
        failed_backwindows[i] = 0

front_rand = np.random.rand(3)
back_rand = np.random.rand(4)

for i in range(len(failed_frontwindows)):
    if front_rand[i] < prob_front:
        failed_frontwindows[i] = 0
for i in range(len(failed_backwindows)):
    if back_rand[i] < prob_back:
        failed_backwindows[i] = 0

# connections
for i in range(len(sheath_loads)):
    if sheath_loads[i]>sheath_capacity[i]:
        sheath_loads[i] = 0
        if sheath_loads[i] != 0:
            sheath_loads[i] = sheath_loads[i]-10
    
left_end_truss = (sheath_loads[0]*4+sheath_loads[8]*4+sheath_loads[16]*4+sheath_loads[24]*4+sheath_loads[32]*4+sheath_loads[40]*4+sheath_loads[48]*4+sheath_loads[56]*4+sheath_loads[64]*4+sheath_loads[72]*4+sheath_loads[80]*4+sheath_loads[88]*4)/8
right_end_truss = (sheath_loads[7]*4+sheath_loads[15]*4+sheath_loads[23]*4+sheath_loads[31]*4+sheath_loads[39]*4+sheath_loads[47]*4+sheath_loads[55]*4+sheath_loads[63]*4+sheath_loads[71]*4+sheath_loads[79]*4+sheath_loads[87]*4+sheath_loads[95]*4)/8
bottom_1 = ((sheath_loads[0]+sheath_loads[0])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[8]+sheath_loads[8])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[16]+sheath_loads[16])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[24]+sheath_loads[24])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[32]+sheath_loads[32])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[40]+sheath_loads[40])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[48]+sheath_loads[48])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[56]+sheath_loads[56])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[64]+sheath_loads[64])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[72]+sheath_loads[72])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[80]+sheath_loads[80])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[88]+sheath_loads[88])*(math.cos(math.radians(22.62))*46)*4)/44
top_1 = ((sheath_loads[0]+sheath_loads[0])*4+
         (sheath_loads[8]+sheath_loads[8])*4+
         (sheath_loads[16]+sheath_loads[16])*4+
         (sheath_loads[24]+sheath_loads[24])*4+
         (sheath_loads[32]+sheath_loads[32])*4+
         (sheath_loads[40]+sheath_loads[40])*4+
         (sheath_loads[48]+sheath_loads[48])*4+
         (sheath_loads[56]+sheath_loads[56])*4+
         (sheath_loads[64]+sheath_loads[64])*4+
         (sheath_loads[72]+sheath_loads[72])*4+
         (sheath_loads[80]+sheath_loads[80])*4+
         (sheath_loads[88]+sheath_loads[88])*4)-bottom_1

bottom_2 = ((sheath_loads[0]+sheath_loads[1])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[8]+sheath_loads[8])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[16]+sheath_loads[17])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[24]+sheath_loads[24])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[32]+sheath_loads[33])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[40]+sheath_loads[40])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[48]+sheath_loads[49])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[56]+sheath_loads[56])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[64]+sheath_loads[65])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[72]+sheath_loads[72])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[80]+sheath_loads[81])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[88]+sheath_loads[88])*(math.cos(math.radians(22.62))*46)*4)/44
top_2 = ((sheath_loads[0]+sheath_loads[1])*4+
         (sheath_loads[8]+sheath_loads[8])*4+
         (sheath_loads[16]+sheath_loads[17])*4+
         (sheath_loads[24]+sheath_loads[24])*4+
         (sheath_loads[32]+sheath_loads[33])*4+
         (sheath_loads[40]+sheath_loads[40])*4+
         (sheath_loads[48]+sheath_loads[49])*4+
         (sheath_loads[56]+sheath_loads[56])*4+
         (sheath_loads[64]+sheath_loads[65])*4+
         (sheath_loads[72]+sheath_loads[72])*4+
         (sheath_loads[80]+sheath_loads[81])*4+
         (sheath_loads[88]+sheath_loads[88])*4)-bottom_2     

bottom_3 = ((sheath_loads[1]+sheath_loads[1])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[8]+sheath_loads[8])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[17]+sheath_loads[17])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[24]+sheath_loads[24])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[33]+sheath_loads[33])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[40]+sheath_loads[40])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[49]+sheath_loads[49])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[56]+sheath_loads[56])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[65]+sheath_loads[65])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[72]+sheath_loads[72])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[81]+sheath_loads[81])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[88]+sheath_loads[88])*(math.cos(math.radians(22.62))*46)*4)/44
top_3 = ((sheath_loads[1]+sheath_loads[1])*4+
         (sheath_loads[8]+sheath_loads[8])*4+
         (sheath_loads[17]+sheath_loads[17])*4+
         (sheath_loads[24]+sheath_loads[24])*4+
         (sheath_loads[33]+sheath_loads[33])*4+
         (sheath_loads[40]+sheath_loads[40])*4+
         (sheath_loads[49]+sheath_loads[49])*4+
         (sheath_loads[56]+sheath_loads[56])*4+
         (sheath_loads[65]+sheath_loads[65])*4+
         (sheath_loads[72]+sheath_loads[72])*4+
         (sheath_loads[81]+sheath_loads[81])*4+
         (sheath_loads[88]+sheath_loads[88])*4)-bottom_3     

bottom_4 = ((sheath_loads[1]+sheath_loads[1])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[8]+sheath_loads[9])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[17]+sheath_loads[17])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[24]+sheath_loads[25])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[33]+sheath_loads[33])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[40]+sheath_loads[41])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[49]+sheath_loads[49])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[56]+sheath_loads[57])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[65]+sheath_loads[65])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[72]+sheath_loads[73])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[81]+sheath_loads[81])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[88]+sheath_loads[89])*(math.cos(math.radians(22.62))*46)*4)/44
top_4 = ((sheath_loads[1]+sheath_loads[1])*4+
         (sheath_loads[8]+sheath_loads[9])*4+
         (sheath_loads[17]+sheath_loads[17])*4+
         (sheath_loads[24]+sheath_loads[25])*4+
         (sheath_loads[33]+sheath_loads[33])*4+
         (sheath_loads[40]+sheath_loads[41])*4+
         (sheath_loads[49]+sheath_loads[49])*4+
         (sheath_loads[56]+sheath_loads[57])*4+
         (sheath_loads[65]+sheath_loads[65])*4+
         (sheath_loads[72]+sheath_loads[73])*4+
         (sheath_loads[81]+sheath_loads[81])*4+
         (sheath_loads[88]+sheath_loads[89])*4)-bottom_4  

bottom_5 = ((sheath_loads[1]+sheath_loads[1])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[9]+sheath_loads[9])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[17]+sheath_loads[17])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[25]+sheath_loads[25])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[33]+sheath_loads[33])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[41]+sheath_loads[41])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[49]+sheath_loads[49])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[57]+sheath_loads[57])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[65]+sheath_loads[65])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[73]+sheath_loads[73])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[81]+sheath_loads[81])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[89]+sheath_loads[89])*(math.cos(math.radians(22.62))*46)*4)/44
top_5 = ((sheath_loads[1]+sheath_loads[1])*4+
         (sheath_loads[9]+sheath_loads[9])*4+
         (sheath_loads[17]+sheath_loads[17])*4+
         (sheath_loads[25]+sheath_loads[25])*4+
         (sheath_loads[33]+sheath_loads[33])*4+
         (sheath_loads[41]+sheath_loads[41])*4+
         (sheath_loads[49]+sheath_loads[49])*4+
         (sheath_loads[57]+sheath_loads[57])*4+
         (sheath_loads[65]+sheath_loads[65])*4+
         (sheath_loads[73]+sheath_loads[73])*4+
         (sheath_loads[81]+sheath_loads[81])*4+
         (sheath_loads[89]+sheath_loads[89])*4)-bottom_5 

bottom_6 = ((sheath_loads[1]+sheath_loads[2])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[9]+sheath_loads[9])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[17]+sheath_loads[18])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[25]+sheath_loads[25])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[33]+sheath_loads[34])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[41]+sheath_loads[41])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[49]+sheath_loads[50])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[57]+sheath_loads[57])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[65]+sheath_loads[66])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[73]+sheath_loads[73])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[81]+sheath_loads[82])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[89]+sheath_loads[89])*(math.cos(math.radians(22.62))*46)*4)/44
top_6 = ((sheath_loads[1]+sheath_loads[2])*4+
         (sheath_loads[9]+sheath_loads[9])*4+
         (sheath_loads[17]+sheath_loads[18])*4+
         (sheath_loads[25]+sheath_loads[25])*4+
         (sheath_loads[33]+sheath_loads[34])*4+
         (sheath_loads[41]+sheath_loads[41])*4+
         (sheath_loads[49]+sheath_loads[50])*4+
         (sheath_loads[57]+sheath_loads[57])*4+
         (sheath_loads[65]+sheath_loads[66])*4+
         (sheath_loads[73]+sheath_loads[73])*4+
         (sheath_loads[81]+sheath_loads[82])*4+
         (sheath_loads[89]+sheath_loads[89])*4)-bottom_6 

bottom_7 = ((sheath_loads[2]+sheath_loads[2])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[9]+sheath_loads[9])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[18]+sheath_loads[18])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[25]+sheath_loads[25])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[34]+sheath_loads[34])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[41]+sheath_loads[41])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[50]+sheath_loads[50])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[57]+sheath_loads[57])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[66]+sheath_loads[66])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[73]+sheath_loads[73])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[82]+sheath_loads[82])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[89]+sheath_loads[89])*(math.cos(math.radians(22.62))*46)*4)/44
top_7 = ((sheath_loads[2]+sheath_loads[2])*4+
         (sheath_loads[9]+sheath_loads[9])*4+
         (sheath_loads[18]+sheath_loads[18])*4+
         (sheath_loads[25]+sheath_loads[25])*4+
         (sheath_loads[35]+sheath_loads[34])*4+
         (sheath_loads[41]+sheath_loads[41])*4+
         (sheath_loads[50]+sheath_loads[50])*4+
         (sheath_loads[57]+sheath_loads[57])*4+
         (sheath_loads[66]+sheath_loads[66])*4+
         (sheath_loads[73]+sheath_loads[73])*4+
         (sheath_loads[82]+sheath_loads[82])*4+
         (sheath_loads[89]+sheath_loads[89])*4)-bottom_7 

bottom_8 = ((sheath_loads[2]+sheath_loads[2])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[9]+sheath_loads[10])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[18]+sheath_loads[18])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[25]+sheath_loads[26])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[34]+sheath_loads[34])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[41]+sheath_loads[42])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[50]+sheath_loads[50])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[57]+sheath_loads[58])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[66]+sheath_loads[66])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[73]+sheath_loads[74])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[82]+sheath_loads[82])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[89]+sheath_loads[90])*(math.cos(math.radians(22.62))*46)*4)/44
top_8 = ((sheath_loads[2]+sheath_loads[2])*4+
         (sheath_loads[9]+sheath_loads[10])*4+
         (sheath_loads[18]+sheath_loads[18])*4+
         (sheath_loads[25]+sheath_loads[26])*4+
         (sheath_loads[35]+sheath_loads[34])*4+
         (sheath_loads[41]+sheath_loads[42])*4+
         (sheath_loads[50]+sheath_loads[50])*4+
         (sheath_loads[57]+sheath_loads[58])*4+
         (sheath_loads[66]+sheath_loads[66])*4+
         (sheath_loads[73]+sheath_loads[74])*4+
         (sheath_loads[82]+sheath_loads[82])*4+
         (sheath_loads[89]+sheath_loads[90])*4)-bottom_8 

bottom_9 = ((sheath_loads[2]+sheath_loads[2])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[10]+sheath_loads[10])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[18]+sheath_loads[18])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[26]+sheath_loads[26])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[34]+sheath_loads[34])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[42]+sheath_loads[42])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[50]+sheath_loads[50])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[58]+sheath_loads[58])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[66]+sheath_loads[66])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[74]+sheath_loads[74])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[82]+sheath_loads[82])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[90]+sheath_loads[90])*(math.cos(math.radians(22.62))*46)*4)/44
top_9 = ((sheath_loads[2]+sheath_loads[2])*4+
         (sheath_loads[10]+sheath_loads[10])*4+
         (sheath_loads[18]+sheath_loads[18])*4+
         (sheath_loads[26]+sheath_loads[26])*4+
         (sheath_loads[35]+sheath_loads[34])*4+
         (sheath_loads[42]+sheath_loads[42])*4+
         (sheath_loads[50]+sheath_loads[50])*4+
         (sheath_loads[58]+sheath_loads[58])*4+
         (sheath_loads[66]+sheath_loads[66])*4+
         (sheath_loads[74]+sheath_loads[74])*4+
         (sheath_loads[82]+sheath_loads[82])*4+
         (sheath_loads[90]+sheath_loads[90])*4)-bottom_9 

bottom_10 = ((sheath_loads[2]+sheath_loads[3])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[10]+sheath_loads[10])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[18]+sheath_loads[19])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[26]+sheath_loads[26])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[34]+sheath_loads[35])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[42]+sheath_loads[42])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[50]+sheath_loads[51])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[58]+sheath_loads[58])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[66]+sheath_loads[67])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[74]+sheath_loads[74])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[82]+sheath_loads[83])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[90]+sheath_loads[90])*(math.cos(math.radians(22.62))*46)*4)/44
top_10 = ((sheath_loads[2]+sheath_loads[3])*4+
         (sheath_loads[10]+sheath_loads[10])*4+
         (sheath_loads[18]+sheath_loads[19])*4+
         (sheath_loads[26]+sheath_loads[26])*4+
         (sheath_loads[34]+sheath_loads[35])*4+
         (sheath_loads[42]+sheath_loads[42])*4+
         (sheath_loads[50]+sheath_loads[51])*4+
         (sheath_loads[58]+sheath_loads[58])*4+
         (sheath_loads[66]+sheath_loads[67])*4+
         (sheath_loads[74]+sheath_loads[74])*4+
         (sheath_loads[82]+sheath_loads[83])*4+
         (sheath_loads[90]+sheath_loads[90])*4)-bottom_10 

bottom_11 = ((sheath_loads[3]+sheath_loads[3])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[10]+sheath_loads[10])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[19]+sheath_loads[19])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[26]+sheath_loads[26])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[35]+sheath_loads[35])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[42]+sheath_loads[42])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[51]+sheath_loads[51])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[58]+sheath_loads[58])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[67]+sheath_loads[67])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[74]+sheath_loads[74])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[83]+sheath_loads[83])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[90]+sheath_loads[90])*(math.cos(math.radians(22.62))*46)*4)/44
top_11 = ((sheath_loads[3]+sheath_loads[3])*4+
         (sheath_loads[10]+sheath_loads[10])*4+
         (sheath_loads[19]+sheath_loads[19])*4+
         (sheath_loads[26]+sheath_loads[26])*4+
         (sheath_loads[35]+sheath_loads[35])*4+
         (sheath_loads[42]+sheath_loads[42])*4+
         (sheath_loads[51]+sheath_loads[51])*4+
         (sheath_loads[58]+sheath_loads[58])*4+
         (sheath_loads[67]+sheath_loads[67])*4+
         (sheath_loads[74]+sheath_loads[74])*4+
         (sheath_loads[83]+sheath_loads[83])*4+
         (sheath_loads[90]+sheath_loads[90])*4)-bottom_11 

bottom_12 = ((sheath_loads[3]+sheath_loads[3])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[10]+sheath_loads[11])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[19]+sheath_loads[19])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[26]+sheath_loads[27])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[35]+sheath_loads[35])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[42]+sheath_loads[43])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[51]+sheath_loads[51])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[58]+sheath_loads[59])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[67]+sheath_loads[67])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[74]+sheath_loads[75])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[83]+sheath_loads[83])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[90]+sheath_loads[91])*(math.cos(math.radians(22.62))*46)*4)/44
top_12 = ((sheath_loads[3]+sheath_loads[3])*4+
         (sheath_loads[10]+sheath_loads[11])*4+
         (sheath_loads[19]+sheath_loads[19])*4+
         (sheath_loads[26]+sheath_loads[27])*4+
         (sheath_loads[35]+sheath_loads[35])*4+
         (sheath_loads[42]+sheath_loads[43])*4+
         (sheath_loads[51]+sheath_loads[51])*4+
         (sheath_loads[58]+sheath_loads[59])*4+
         (sheath_loads[67]+sheath_loads[67])*4+
         (sheath_loads[74]+sheath_loads[75])*4+
         (sheath_loads[83]+sheath_loads[83])*4+
         (sheath_loads[90]+sheath_loads[91])*4)-bottom_12 

bottom_13 = ((sheath_loads[3]+sheath_loads[3])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[11]+sheath_loads[11])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[19]+sheath_loads[19])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[27]+sheath_loads[27])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[35]+sheath_loads[35])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[43]+sheath_loads[43])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[51]+sheath_loads[51])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[59]+sheath_loads[59])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[67]+sheath_loads[67])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[75]+sheath_loads[75])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[83]+sheath_loads[83])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[91]+sheath_loads[91])*(math.cos(math.radians(22.62))*46)*4)/44
top_13 = ((sheath_loads[3]+sheath_loads[3])*4+
         (sheath_loads[11]+sheath_loads[11])*4+
         (sheath_loads[19]+sheath_loads[19])*4+
         (sheath_loads[27]+sheath_loads[27])*4+
         (sheath_loads[35]+sheath_loads[35])*4+
         (sheath_loads[43]+sheath_loads[43])*4+
         (sheath_loads[51]+sheath_loads[51])*4+
         (sheath_loads[59]+sheath_loads[59])*4+
         (sheath_loads[67]+sheath_loads[67])*4+
         (sheath_loads[75]+sheath_loads[75])*4+
         (sheath_loads[83]+sheath_loads[83])*4+
         (sheath_loads[91]+sheath_loads[91])*4)-bottom_13 

bottom_14 = ((sheath_loads[3]+sheath_loads[4])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[11]+sheath_loads[11])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[19]+sheath_loads[20])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[27]+sheath_loads[27])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[35]+sheath_loads[36])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[43]+sheath_loads[43])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[51]+sheath_loads[52])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[59]+sheath_loads[59])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[67]+sheath_loads[68])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[75]+sheath_loads[75])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[83]+sheath_loads[84])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[91]+sheath_loads[91])*(math.cos(math.radians(22.62))*46)*4)/44
top_14 = ((sheath_loads[3]+sheath_loads[4])*4+
         (sheath_loads[11]+sheath_loads[11])*4+
         (sheath_loads[19]+sheath_loads[20])*4+
         (sheath_loads[27]+sheath_loads[27])*4+
         (sheath_loads[35]+sheath_loads[36])*4+
         (sheath_loads[43]+sheath_loads[43])*4+
         (sheath_loads[51]+sheath_loads[52])*4+
         (sheath_loads[59]+sheath_loads[59])*4+
         (sheath_loads[67]+sheath_loads[68])*4+
         (sheath_loads[75]+sheath_loads[75])*4+
         (sheath_loads[83]+sheath_loads[84])*4+
         (sheath_loads[91]+sheath_loads[91])*4)-bottom_14 

bottom_15 = ((sheath_loads[4]+sheath_loads[4])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[11]+sheath_loads[11])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[20]+sheath_loads[20])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[27]+sheath_loads[27])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[36]+sheath_loads[36])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[43]+sheath_loads[43])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[52]+sheath_loads[52])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[59]+sheath_loads[59])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[68]+sheath_loads[68])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[75]+sheath_loads[75])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[84]+sheath_loads[84])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[91]+sheath_loads[91])*(math.cos(math.radians(22.62))*46)*4)/44
top_15 = ((sheath_loads[4]+sheath_loads[4])*4+
         (sheath_loads[11]+sheath_loads[11])*4+
         (sheath_loads[20]+sheath_loads[20])*4+
         (sheath_loads[27]+sheath_loads[27])*4+
         (sheath_loads[36]+sheath_loads[36])*4+
         (sheath_loads[43]+sheath_loads[43])*4+
         (sheath_loads[52]+sheath_loads[52])*4+
         (sheath_loads[59]+sheath_loads[59])*4+
         (sheath_loads[68]+sheath_loads[68])*4+
         (sheath_loads[75]+sheath_loads[75])*4+
         (sheath_loads[84]+sheath_loads[84])*4+
         (sheath_loads[91]+sheath_loads[91])*4)-bottom_15 

bottom_16 = ((sheath_loads[4]+sheath_loads[4])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[11]+sheath_loads[12])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[20]+sheath_loads[20])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[27]+sheath_loads[28])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[36]+sheath_loads[36])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[43]+sheath_loads[44])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[52]+sheath_loads[52])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[59]+sheath_loads[60])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[68]+sheath_loads[68])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[75]+sheath_loads[76])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[84]+sheath_loads[84])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[91]+sheath_loads[92])*(math.cos(math.radians(22.62))*46)*4)/44
top_16 = ((sheath_loads[4]+sheath_loads[4])*4+
         (sheath_loads[11]+sheath_loads[12])*4+
         (sheath_loads[20]+sheath_loads[20])*4+
         (sheath_loads[27]+sheath_loads[28])*4+
         (sheath_loads[36]+sheath_loads[36])*4+
         (sheath_loads[43]+sheath_loads[44])*4+
         (sheath_loads[52]+sheath_loads[52])*4+
         (sheath_loads[59]+sheath_loads[60])*4+
         (sheath_loads[68]+sheath_loads[68])*4+
         (sheath_loads[75]+sheath_loads[76])*4+
         (sheath_loads[84]+sheath_loads[84])*4+
         (sheath_loads[91]+sheath_loads[92])*4)-bottom_16 

bottom_17 = ((sheath_loads[4]+sheath_loads[4])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[12]+sheath_loads[12])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[20]+sheath_loads[20])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[28]+sheath_loads[28])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[36]+sheath_loads[36])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[44]+sheath_loads[44])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[52]+sheath_loads[52])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[60]+sheath_loads[60])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[68]+sheath_loads[68])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[76]+sheath_loads[76])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[84]+sheath_loads[84])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[92]+sheath_loads[92])*(math.cos(math.radians(22.62))*46)*4)/44
top_17 = ((sheath_loads[4]+sheath_loads[4])*4+
         (sheath_loads[12]+sheath_loads[12])*4+
         (sheath_loads[20]+sheath_loads[20])*4+
         (sheath_loads[28]+sheath_loads[28])*4+
         (sheath_loads[36]+sheath_loads[36])*4+
         (sheath_loads[44]+sheath_loads[44])*4+
         (sheath_loads[52]+sheath_loads[52])*4+
         (sheath_loads[60]+sheath_loads[60])*4+
         (sheath_loads[68]+sheath_loads[68])*4+
         (sheath_loads[76]+sheath_loads[76])*4+
         (sheath_loads[84]+sheath_loads[84])*4+
         (sheath_loads[92]+sheath_loads[92])*4)-bottom_17 

bottom_18 = ((sheath_loads[4]+sheath_loads[5])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[12]+sheath_loads[12])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[20]+sheath_loads[21])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[28]+sheath_loads[28])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[36]+sheath_loads[37])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[44]+sheath_loads[44])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[52]+sheath_loads[53])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[60]+sheath_loads[60])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[68]+sheath_loads[69])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[76]+sheath_loads[76])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[84]+sheath_loads[85])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[92]+sheath_loads[92])*(math.cos(math.radians(22.62))*46)*4)/44
top_18 = ((sheath_loads[4]+sheath_loads[5])*4+
         (sheath_loads[12]+sheath_loads[12])*4+
         (sheath_loads[20]+sheath_loads[21])*4+
         (sheath_loads[28]+sheath_loads[28])*4+
         (sheath_loads[36]+sheath_loads[37])*4+
         (sheath_loads[44]+sheath_loads[44])*4+
         (sheath_loads[52]+sheath_loads[53])*4+
         (sheath_loads[60]+sheath_loads[60])*4+
         (sheath_loads[68]+sheath_loads[69])*4+
         (sheath_loads[76]+sheath_loads[76])*4+
         (sheath_loads[84]+sheath_loads[85])*4+
         (sheath_loads[92]+sheath_loads[92])*4)-bottom_18 

bottom_19 = ((sheath_loads[5]+sheath_loads[5])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[12]+sheath_loads[12])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[21]+sheath_loads[21])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[28]+sheath_loads[28])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[37]+sheath_loads[37])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[44]+sheath_loads[44])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[53]+sheath_loads[53])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[60]+sheath_loads[60])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[69]+sheath_loads[69])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[76]+sheath_loads[76])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[85]+sheath_loads[85])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[92]+sheath_loads[92])*(math.cos(math.radians(22.62))*46)*4)/44
top_19 = ((sheath_loads[5]+sheath_loads[5])*4+
         (sheath_loads[12]+sheath_loads[12])*4+
         (sheath_loads[21]+sheath_loads[21])*4+
         (sheath_loads[28]+sheath_loads[28])*4+
         (sheath_loads[37]+sheath_loads[37])*4+
         (sheath_loads[44]+sheath_loads[44])*4+
         (sheath_loads[53]+sheath_loads[53])*4+
         (sheath_loads[60]+sheath_loads[60])*4+
         (sheath_loads[69]+sheath_loads[69])*4+
         (sheath_loads[76]+sheath_loads[76])*4+
         (sheath_loads[85]+sheath_loads[85])*4+
         (sheath_loads[92]+sheath_loads[92])*4)-bottom_19 

bottom_20 = ((sheath_loads[5]+sheath_loads[5])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[12]+sheath_loads[13])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[21]+sheath_loads[21])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[28]+sheath_loads[29])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[37]+sheath_loads[37])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[44]+sheath_loads[45])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[53]+sheath_loads[53])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[60]+sheath_loads[61])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[69]+sheath_loads[69])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[76]+sheath_loads[77])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[85]+sheath_loads[85])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[92]+sheath_loads[93])*(math.cos(math.radians(22.62))*46)*4)/44
top_20 = ((sheath_loads[5]+sheath_loads[5])*4+
         (sheath_loads[12]+sheath_loads[13])*4+
         (sheath_loads[21]+sheath_loads[21])*4+
         (sheath_loads[28]+sheath_loads[29])*4+
         (sheath_loads[37]+sheath_loads[37])*4+
         (sheath_loads[44]+sheath_loads[45])*4+
         (sheath_loads[53]+sheath_loads[53])*4+
         (sheath_loads[60]+sheath_loads[61])*4+
         (sheath_loads[69]+sheath_loads[69])*4+
         (sheath_loads[76]+sheath_loads[77])*4+
         (sheath_loads[85]+sheath_loads[85])*4+
         (sheath_loads[92]+sheath_loads[93])*4)-bottom_20

bottom_21 = ((sheath_loads[5]+sheath_loads[5])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[13]+sheath_loads[13])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[21]+sheath_loads[21])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[29]+sheath_loads[29])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[37]+sheath_loads[37])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[45]+sheath_loads[45])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[53]+sheath_loads[53])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[61]+sheath_loads[61])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[69]+sheath_loads[69])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[77]+sheath_loads[77])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[85]+sheath_loads[85])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[93]+sheath_loads[93])*(math.cos(math.radians(22.62))*46)*4)/44
top_21 = ((sheath_loads[5]+sheath_loads[5])*4+
         (sheath_loads[13]+sheath_loads[13])*4+
         (sheath_loads[21]+sheath_loads[21])*4+
         (sheath_loads[29]+sheath_loads[29])*4+
         (sheath_loads[37]+sheath_loads[37])*4+
         (sheath_loads[45]+sheath_loads[45])*4+
         (sheath_loads[53]+sheath_loads[53])*4+
         (sheath_loads[61]+sheath_loads[61])*4+
         (sheath_loads[69]+sheath_loads[69])*4+
         (sheath_loads[77]+sheath_loads[77])*4+
         (sheath_loads[85]+sheath_loads[85])*4+
         (sheath_loads[93]+sheath_loads[93])*4)-bottom_21

bottom_22 = ((sheath_loads[5]+sheath_loads[6])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[13]+sheath_loads[13])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[21]+sheath_loads[22])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[29]+sheath_loads[29])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[37]+sheath_loads[38])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[45]+sheath_loads[45])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[53]+sheath_loads[54])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[61]+sheath_loads[61])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[69]+sheath_loads[70])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[77]+sheath_loads[77])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[85]+sheath_loads[86])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[93]+sheath_loads[93])*(math.cos(math.radians(22.62))*46)*4)/44
top_22 = ((sheath_loads[5]+sheath_loads[6])*4+
         (sheath_loads[13]+sheath_loads[13])*4+
         (sheath_loads[21]+sheath_loads[22])*4+
         (sheath_loads[29]+sheath_loads[29])*4+
         (sheath_loads[37]+sheath_loads[38])*4+
         (sheath_loads[45]+sheath_loads[45])*4+
         (sheath_loads[53]+sheath_loads[54])*4+
         (sheath_loads[61]+sheath_loads[61])*4+
         (sheath_loads[69]+sheath_loads[70])*4+
         (sheath_loads[77]+sheath_loads[77])*4+
         (sheath_loads[85]+sheath_loads[86])*4+
         (sheath_loads[93]+sheath_loads[93])*4)-bottom_22

bottom_23 = ((sheath_loads[6]+sheath_loads[6])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[13]+sheath_loads[13])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[22]+sheath_loads[22])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[29]+sheath_loads[29])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[38]+sheath_loads[38])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[45]+sheath_loads[45])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[54]+sheath_loads[54])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[61]+sheath_loads[61])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[70]+sheath_loads[70])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[77]+sheath_loads[77])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[86]+sheath_loads[86])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[93]+sheath_loads[93])*(math.cos(math.radians(22.62))*46)*4)/44
top_23 = ((sheath_loads[6]+sheath_loads[6])*4+
         (sheath_loads[13]+sheath_loads[13])*4+
         (sheath_loads[22]+sheath_loads[22])*4+
         (sheath_loads[29]+sheath_loads[29])*4+
         (sheath_loads[38]+sheath_loads[38])*4+
         (sheath_loads[45]+sheath_loads[45])*4+
         (sheath_loads[54]+sheath_loads[54])*4+
         (sheath_loads[61]+sheath_loads[61])*4+
         (sheath_loads[70]+sheath_loads[70])*4+
         (sheath_loads[77]+sheath_loads[77])*4+
         (sheath_loads[86]+sheath_loads[86])*4+
         (sheath_loads[93]+sheath_loads[93])*4)-bottom_23

bottom_24 = ((sheath_loads[6]+sheath_loads[6])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[13]+sheath_loads[14])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[22]+sheath_loads[22])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[29]+sheath_loads[30])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[38]+sheath_loads[38])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[45]+sheath_loads[46])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[54]+sheath_loads[54])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[61]+sheath_loads[62])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[70]+sheath_loads[70])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[77]+sheath_loads[78])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[86]+sheath_loads[86])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[93]+sheath_loads[94])*(math.cos(math.radians(22.62))*46)*4)/44
top_24 = ((sheath_loads[6]+sheath_loads[6])*4+
         (sheath_loads[13]+sheath_loads[14])*4+
         (sheath_loads[22]+sheath_loads[22])*4+
         (sheath_loads[29]+sheath_loads[30])*4+
         (sheath_loads[38]+sheath_loads[38])*4+
         (sheath_loads[45]+sheath_loads[46])*4+
         (sheath_loads[54]+sheath_loads[54])*4+
         (sheath_loads[61]+sheath_loads[62])*4+
         (sheath_loads[70]+sheath_loads[70])*4+
         (sheath_loads[77]+sheath_loads[78])*4+
         (sheath_loads[86]+sheath_loads[86])*4+
         (sheath_loads[93]+sheath_loads[94])*4)-bottom_24

bottom_25 = ((sheath_loads[6]+sheath_loads[6])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[14]+sheath_loads[14])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[22]+sheath_loads[22])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[30]+sheath_loads[30])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[38]+sheath_loads[38])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[46]+sheath_loads[46])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[54]+sheath_loads[54])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[62]+sheath_loads[62])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[70]+sheath_loads[70])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[78]+sheath_loads[78])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[86]+sheath_loads[86])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[94]+sheath_loads[94])*(math.cos(math.radians(22.62))*46)*4)/44
top_25 = ((sheath_loads[6]+sheath_loads[6])*4+
         (sheath_loads[14]+sheath_loads[14])*4+
         (sheath_loads[22]+sheath_loads[22])*4+
         (sheath_loads[30]+sheath_loads[30])*4+
         (sheath_loads[38]+sheath_loads[38])*4+
         (sheath_loads[46]+sheath_loads[46])*4+
         (sheath_loads[54]+sheath_loads[54])*4+
         (sheath_loads[62]+sheath_loads[62])*4+
         (sheath_loads[70]+sheath_loads[70])*4+
         (sheath_loads[78]+sheath_loads[78])*4+
         (sheath_loads[86]+sheath_loads[86])*4+
         (sheath_loads[94]+sheath_loads[94])*4)-bottom_25

bottom_26 = ((sheath_loads[6]+sheath_loads[7])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[14]+sheath_loads[14])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[22]+sheath_loads[23])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[30]+sheath_loads[30])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[38]+sheath_loads[39])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[46]+sheath_loads[46])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[54]+sheath_loads[55])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[62]+sheath_loads[62])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[70]+sheath_loads[71])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[78]+sheath_loads[78])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[86]+sheath_loads[87])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[94]+sheath_loads[94])*(math.cos(math.radians(22.62))*46)*4)/44
top_26 = ((sheath_loads[6]+sheath_loads[7])*4+
         (sheath_loads[14]+sheath_loads[14])*4+
         (sheath_loads[22]+sheath_loads[23])*4+
         (sheath_loads[30]+sheath_loads[30])*4+
         (sheath_loads[38]+sheath_loads[39])*4+
         (sheath_loads[46]+sheath_loads[46])*4+
         (sheath_loads[54]+sheath_loads[55])*4+
         (sheath_loads[62]+sheath_loads[62])*4+
         (sheath_loads[70]+sheath_loads[71])*4+
         (sheath_loads[78]+sheath_loads[78])*4+
         (sheath_loads[86]+sheath_loads[87])*4+
         (sheath_loads[94]+sheath_loads[94])*4)-bottom_26

bottom_27 = ((sheath_loads[7]+sheath_loads[7])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[14]+sheath_loads[14])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[23]+sheath_loads[23])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[30]+sheath_loads[30])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[39]+sheath_loads[39])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[46]+sheath_loads[46])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[55]+sheath_loads[55])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[62]+sheath_loads[62])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[71]+sheath_loads[71])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[78]+sheath_loads[78])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[87]+sheath_loads[87])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[94]+sheath_loads[94])*(math.cos(math.radians(22.62))*46)*4)/44
top_27 = ((sheath_loads[7]+sheath_loads[7])*4+
         (sheath_loads[14]+sheath_loads[14])*4+
         (sheath_loads[23]+sheath_loads[23])*4+
         (sheath_loads[30]+sheath_loads[30])*4+
         (sheath_loads[39]+sheath_loads[39])*4+
         (sheath_loads[46]+sheath_loads[46])*4+
         (sheath_loads[55]+sheath_loads[55])*4+
         (sheath_loads[62]+sheath_loads[62])*4+
         (sheath_loads[71]+sheath_loads[71])*4+
         (sheath_loads[78]+sheath_loads[78])*4+
         (sheath_loads[87]+sheath_loads[87])*4+
         (sheath_loads[94]+sheath_loads[94])*4)-bottom_27

bottom_28 = ((sheath_loads[7]+sheath_loads[7])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[14]+sheath_loads[15])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[23]+sheath_loads[23])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[30]+sheath_loads[31])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[39]+sheath_loads[39])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[46]+sheath_loads[47])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[55]+sheath_loads[55])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[62]+sheath_loads[63])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[71]+sheath_loads[71])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[78]+sheath_loads[79])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[87]+sheath_loads[87])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[94]+sheath_loads[95])*(math.cos(math.radians(22.62))*46)*4)/44
top_28 = ((sheath_loads[7]+sheath_loads[7])*4+
         (sheath_loads[14]+sheath_loads[15])*4+
         (sheath_loads[23]+sheath_loads[23])*4+
         (sheath_loads[30]+sheath_loads[31])*4+
         (sheath_loads[39]+sheath_loads[39])*4+
         (sheath_loads[46]+sheath_loads[47])*4+
         (sheath_loads[55]+sheath_loads[55])*4+
         (sheath_loads[62]+sheath_loads[63])*4+
         (sheath_loads[71]+sheath_loads[71])*4+
         (sheath_loads[78]+sheath_loads[79])*4+
         (sheath_loads[87]+sheath_loads[87])*4+
         (sheath_loads[94]+sheath_loads[95])*4)-bottom_28

bottom_29 = ((sheath_loads[7]+sheath_loads[7])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[15]+sheath_loads[15])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[23]+sheath_loads[23])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[32]+sheath_loads[31])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[39]+sheath_loads[39])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[47]+sheath_loads[47])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[55]+sheath_loads[55])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[63]+sheath_loads[63])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[71]+sheath_loads[71])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[79]+sheath_loads[79])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[87]+sheath_loads[87])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[95]+sheath_loads[95])*(math.cos(math.radians(22.62))*46)*4)/44
top_29 = ((sheath_loads[7]+sheath_loads[7])*4+
         (sheath_loads[15]+sheath_loads[15])*4+
         (sheath_loads[23]+sheath_loads[23])*4+
         (sheath_loads[31]+sheath_loads[31])*4+
         (sheath_loads[39]+sheath_loads[39])*4+
         (sheath_loads[47]+sheath_loads[47])*4+
         (sheath_loads[55]+sheath_loads[55])*4+
         (sheath_loads[63]+sheath_loads[63])*4+
         (sheath_loads[71]+sheath_loads[71])*4+
         (sheath_loads[79]+sheath_loads[79])*4+
         (sheath_loads[87]+sheath_loads[87])*4+
         (sheath_loads[95]+sheath_loads[95])*4)-bottom_29

connection_loads = [left_end_truss, top_1, top_2, top_3, top_4, top_5, top_6, top_7, top_8, top_9, top_10, top_11,
                    top_12, top_13, top_14, top_15, top_16, top_17, top_18, top_19, top_20, top_21, top_22, top_23,
                    top_24, top_25, top_26, top_27, top_28, top_29, right_end_truss, right_end_truss, right_end_truss,
                    right_end_truss, right_end_truss, right_end_truss, right_end_truss, right_end_truss, bottom_29,
                    bottom_28, bottom_27, bottom_26, bottom_25, bottom_24, bottom_23, bottom_22, bottom_21, bottom_20,
                    bottom_19, bottom_18, bottom_17, bottom_16, bottom_15, bottom_14, bottom_13, bottom_12, bottom_11,
                    bottom_10, bottom_9, bottom_8, bottom_7, bottom_6, bottom_5, bottom_4, bottom_3, bottom_2, 
                    bottom_1, left_end_truss, left_end_truss, left_end_truss, left_end_truss, left_end_truss,
                    left_end_truss, left_end_truss]

if walls == 1: # concrete block
    if connections == 1: # hurricane straps
        connection_COV = 0.2
        batch_COV = 0.05
        
        side_mean = 4200
        side_std = side_mean*connection_COV
        upper_side_limit = side_mean + 2*side_std
        lower_side_limit = side_mean - 2*side_std
        
        gable_mean = 1920
        gable_std = side_mean*connection_COV
        upper_gable_limit = gable_mean + 2*gable_std
        lower_gable_limit = gable_mean - 2*gable_std
        
        side = np.random.normal(side_mean, side_std, size = (1))
        too_high_indices = np.where(side > upper_side_limit)
        while np.any(too_high_indices):
            side[too_high_indices] = np.random.normal(
                side_mean, side_std, size=len(too_high_indices))
            too_high_indices = np.where(side > upper_side_limit)
        
        too_low_indices = np.where(side < lower_side_limit)
        while np.any(too_low_indices):
            side[too_low_indices] = np.random.normal(
                side_mean, side_std, size=len(too_low_indices))
            too_low_indices = np.where(side < lower_side_limit)
    
        gable = np.random.normal(gable_mean, gable_std, size = (1))
        too_high_indices = np.where(gable > upper_gable_limit)
        while np.any(too_high_indices):
            gable[too_high_indices] = np.random.normal(
                gable_mean, gable_std, size=len(too_high_indices))
            too_high_indices = np.where(gable > upper_gable_limit)
        
        too_low_indices = np.where(gable < lower_gable_limit)
        while np.any(too_low_indices):
            side[too_low_indices] = np.random.normal(
                gable_mean, gable_std, size=len(too_low_indices))
            too_low_indices = np.where(gable < lower_gable_limit)  
        
        new_side_std = batch_COV*side
        new_gable_std = batch_COV*gable
        new_upper_side_limit = side + 2*new_side_std
        new_lower_side_limit = side - 2*new_side_std
        new_upper_gable_limit = gable + 2*new_gable_std
        new_lower_gable_limit = gable - 2*new_gable_std        
        
        side_conn_capacities = np.random.normal(side, new_side_std, size = (58))
        too_high_indices = np.where(side_conn_capacities > new_upper_side_limit)        
        while np.any(too_high_indices):
            side_conn_capacities[too_high_indices] = np.random.normal(
                side, new_side_std, size=len(too_high_indices))
            too_high_indices = np.where(side_conn_capacities > new_upper_side_limit)
        
        too_low_indices = np.where(side_conn_capacities < new_lower_side_limit)
        while np.any(too_low_indices):
            side_conn_capacities[too_low_indices] = np.random.normal(
                side, new_side_std, size=len(too_low_indices))
            too_low_indices = np.where(side_conn_capacities < new_lower_side_limit)         
    
        gable_conn_capacities = np.random.normal(gable, new_gable_std, size = (16))
        too_high_indices = np.where(gable_conn_capacities > new_upper_gable_limit)        
        while np.any(too_high_indices):
            gable_conn_capacities[too_high_indices] = np.random.normal(
                gable, new_gable_std, size=len(too_high_indices))
            too_high_indices = np.where(gable_conn_capacities > new_upper_gable_limit)
        
        too_low_indices = np.where(gable_conn_capacities < new_lower_gable_limit)
        while np.any(too_low_indices):
            gable_conn_capacities[too_low_indices] = np.random.normal(
                gable, new_gable_std, size=len(too_low_indices))
            too_low_indices = np.where(gable_conn_capacities < new_lower_gable_limit)         
        
    
        connection_capacities = [gable_conn_capacities[0], side_conn_capacities[0], side_conn_capacities[1],
                                  side_conn_capacities[2], side_conn_capacities[3], side_conn_capacities[4],
                                  side_conn_capacities[5], side_conn_capacities[6], side_conn_capacities[7],
                                  side_conn_capacities[8], side_conn_capacities[9], side_conn_capacities[10],
                                  side_conn_capacities[11], side_conn_capacities[12], side_conn_capacities[13],
                                  side_conn_capacities[14], side_conn_capacities[15], side_conn_capacities[16],
                                  side_conn_capacities[17], side_conn_capacities[18], side_conn_capacities[19],
                                  side_conn_capacities[20], side_conn_capacities[21], side_conn_capacities[22],
                                  side_conn_capacities[23], side_conn_capacities[24], side_conn_capacities[25],
                                  side_conn_capacities[26], side_conn_capacities[27], side_conn_capacities[28],
                                  gable_conn_capacities[1], gable_conn_capacities[2], gable_conn_capacities[3], 
                                  gable_conn_capacities[4], gable_conn_capacities[5], gable_conn_capacities[6], 
                                  gable_conn_capacities[7], gable_conn_capacities[8],
                                  side_conn_capacities[29], side_conn_capacities[30],
                                  side_conn_capacities[31], side_conn_capacities[32], side_conn_capacities[33],
                                  side_conn_capacities[34], side_conn_capacities[35], side_conn_capacities[36],
                                  side_conn_capacities[37], side_conn_capacities[38], side_conn_capacities[39],
                                  side_conn_capacities[40], side_conn_capacities[41], side_conn_capacities[42],
                                  side_conn_capacities[43], side_conn_capacities[44], side_conn_capacities[45],
                                  side_conn_capacities[46], side_conn_capacities[47], side_conn_capacities[48],
                                  side_conn_capacities[49], side_conn_capacities[50], side_conn_capacities[51],
                                  side_conn_capacities[52], side_conn_capacities[53], side_conn_capacities[54],
                                  side_conn_capacities[55], side_conn_capacities[56], side_conn_capacities[57],   
                                  gable_conn_capacities[9], gable_conn_capacities[10], 
                                  gable_conn_capacities[11], gable_conn_capacities[12], gable_conn_capacities[13], 
                                  gable_conn_capacities[14], gable_conn_capacities[15]]
    elif connections == 2: # hurricane straps
        connection_COV = 0.2
        batch_COV = 0.05
        
        side_mean = 3195
        side_std = side_mean*connection_COV
        upper_side_limit = side_mean + 2*side_std
        lower_side_limit = side_mean - 2*side_std
        
        gable_mean = 675
        gable_std = side_mean*connection_COV
        upper_gable_limit = gable_mean + 2*gable_std
        lower_gable_limit = gable_mean - 2*gable_std
        
        side = np.random.normal(side_mean, side_std, size = (1))
        too_high_indices = np.where(side > upper_side_limit)
        while np.any(too_high_indices):
            side[too_high_indices] = np.random.normal(
                side_mean, side_std, size=len(too_high_indices))
            too_high_indices = np.where(side > upper_side_limit)
        
        too_low_indices = np.where(side < lower_side_limit)
        while np.any(too_low_indices):
            side[too_low_indices] = np.random.normal(
                side_mean, side_std, size=len(too_low_indices))
            too_low_indices = np.where(side < lower_side_limit)
    
        gable = np.random.normal(gable_mean, gable_std, size = (1))
        too_high_indices = np.where(gable > upper_gable_limit)
        while np.any(too_high_indices):
            gable[too_high_indices] = np.random.normal(
                gable_mean, gable_std, size=len(too_high_indices))
            too_high_indices = np.where(gable > upper_gable_limit)
        
        too_low_indices = np.where(gable < lower_gable_limit)
        while np.any(too_low_indices):
            side[too_low_indices] = np.random.normal(
                gable_mean, gable_std, size=len(too_low_indices))
            too_low_indices = np.where(gable < lower_gable_limit)  
        
        new_side_std = batch_COV*side
        new_gable_std = batch_COV*gable
        new_upper_side_limit = side + 2*new_side_std
        new_lower_side_limit = side - 2*new_side_std
        new_upper_gable_limit = gable + 2*new_gable_std
        new_lower_gable_limit = gable - 2*new_gable_std        
        
        side_conn_capacities = np.random.normal(side, new_side_std, size = (58))
        too_high_indices = np.where(side_conn_capacities > new_upper_side_limit)        
        while np.any(too_high_indices):
            side_conn_capacities[too_high_indices] = np.random.normal(
                side, new_side_std, size=len(too_high_indices))
            too_high_indices = np.where(side_conn_capacities > new_upper_side_limit)
        
        too_low_indices = np.where(side_conn_capacities < new_lower_side_limit)
        while np.any(too_low_indices):
            side_conn_capacities[too_low_indices] = np.random.normal(
                side, new_side_std, size=len(too_low_indices))
            too_low_indices = np.where(side_conn_capacities < new_lower_side_limit)         
    
        gable_conn_capacities = np.random.normal(gable, new_gable_std, size = (16))
        too_high_indices = np.where(gable_conn_capacities > new_upper_gable_limit)        
        while np.any(too_high_indices):
            gable_conn_capacities[too_high_indices] = np.random.normal(
                gable, new_gable_std, size=len(too_high_indices))
            too_high_indices = np.where(gable_conn_capacities > new_upper_gable_limit)
        
        too_low_indices = np.where(gable_conn_capacities < new_lower_gable_limit)
        while np.any(too_low_indices):
            gable_conn_capacities[too_low_indices] = np.random.normal(
                gable, new_gable_std, size=len(too_low_indices))
            too_low_indices = np.where(gable_conn_capacities < new_lower_gable_limit)         
        
    
        connection_capacities = [gable_conn_capacities[0], side_conn_capacities[0], side_conn_capacities[1],
                                  side_conn_capacities[2], side_conn_capacities[3], side_conn_capacities[4],
                                  side_conn_capacities[5], side_conn_capacities[6], side_conn_capacities[7],
                                  side_conn_capacities[8], side_conn_capacities[9], side_conn_capacities[10],
                                  side_conn_capacities[11], side_conn_capacities[12], side_conn_capacities[13],
                                  side_conn_capacities[14], side_conn_capacities[15], side_conn_capacities[16],
                                  side_conn_capacities[17], side_conn_capacities[18], side_conn_capacities[19],
                                  side_conn_capacities[20], side_conn_capacities[21], side_conn_capacities[22],
                                  side_conn_capacities[23], side_conn_capacities[24], side_conn_capacities[25],
                                  side_conn_capacities[26], side_conn_capacities[27], side_conn_capacities[28],
                                  gable_conn_capacities[1], gable_conn_capacities[2], gable_conn_capacities[3], 
                                  gable_conn_capacities[4], gable_conn_capacities[5], gable_conn_capacities[6], 
                                  gable_conn_capacities[7], gable_conn_capacities[8],
                                  side_conn_capacities[29], side_conn_capacities[30],
                                  side_conn_capacities[31], side_conn_capacities[32], side_conn_capacities[33],
                                  side_conn_capacities[34], side_conn_capacities[35], side_conn_capacities[36],
                                  side_conn_capacities[37], side_conn_capacities[38], side_conn_capacities[39],
                                  side_conn_capacities[40], side_conn_capacities[41], side_conn_capacities[42],
                                  side_conn_capacities[43], side_conn_capacities[44], side_conn_capacities[45],
                                  side_conn_capacities[46], side_conn_capacities[47], side_conn_capacities[48],
                                  side_conn_capacities[49], side_conn_capacities[50], side_conn_capacities[51],
                                  side_conn_capacities[52], side_conn_capacities[53], side_conn_capacities[54],
                                  side_conn_capacities[55], side_conn_capacities[56], side_conn_capacities[57],   
                                  gable_conn_capacities[9], gable_conn_capacities[10], 
                                  gable_conn_capacities[11], gable_conn_capacities[12], gable_conn_capacities[13], 
                                  gable_conn_capacities[14], gable_conn_capacities[15]]
if walls == 2: # wood frame
    if connections == 1: # hurricane straps
        connection_COV = 0.2
        batch_COV = 0.05
        
        side_mean = 3720
        side_std = side_mean*connection_COV
        upper_side_limit = side_mean + 2*side_std
        lower_side_limit = side_mean - 2*side_std
        
        gable_mean = 3780
        gable_std = side_mean*connection_COV
        upper_gable_limit = gable_mean + 2*gable_std
        lower_gable_limit = gable_mean - 2*gable_std
        
        side = np.random.normal(side_mean, side_std, size = (1))
        too_high_indices = np.where(side > upper_side_limit)
        while np.any(too_high_indices):
            side[too_high_indices] = np.random.normal(
                side_mean, side_std, size=len(too_high_indices))
            too_high_indices = np.where(side > upper_side_limit)
        
        too_low_indices = np.where(side < lower_side_limit)
        while np.any(too_low_indices):
            side[too_low_indices] = np.random.normal(
                side_mean, side_std, size=len(too_low_indices))
            too_low_indices = np.where(side < lower_side_limit)
    
        gable = np.random.normal(gable_mean, gable_std, size = (1))
        too_high_indices = np.where(gable > upper_gable_limit)
        while np.any(too_high_indices):
            gable[too_high_indices] = np.random.normal(
                gable_mean, gable_std, size=len(too_high_indices))
            too_high_indices = np.where(gable > upper_gable_limit)
        
        too_low_indices = np.where(gable < lower_gable_limit)
        while np.any(too_low_indices):
            side[too_low_indices] = np.random.normal(
                gable_mean, gable_std, size=len(too_low_indices))
            too_low_indices = np.where(gable < lower_gable_limit)  
        
        new_side_std = batch_COV*side
        new_gable_std = batch_COV*gable
        new_upper_side_limit = side + 2*new_side_std
        new_lower_side_limit = side - 2*new_side_std
        new_upper_gable_limit = gable + 2*new_gable_std
        new_lower_gable_limit = gable - 2*new_gable_std        
        
        side_conn_capacities = np.random.normal(side, new_side_std, size = (58))
        too_high_indices = np.where(side_conn_capacities > new_upper_side_limit)        
        while np.any(too_high_indices):
            side_conn_capacities[too_high_indices] = np.random.normal(
                side, new_side_std, size=len(too_high_indices))
            too_high_indices = np.where(side_conn_capacities > new_upper_side_limit)
        
        too_low_indices = np.where(side_conn_capacities < new_lower_side_limit)
        while np.any(too_low_indices):
            side_conn_capacities[too_low_indices] = np.random.normal(
                side, new_side_std, size=len(too_low_indices))
            too_low_indices = np.where(side_conn_capacities < new_lower_side_limit)         
    
        gable_conn_capacities = np.random.normal(gable, new_gable_std, size = (16))
        too_high_indices = np.where(gable_conn_capacities > new_upper_gable_limit)        
        while np.any(too_high_indices):
            gable_conn_capacities[too_high_indices] = np.random.normal(
                gable, new_gable_std, size=len(too_high_indices))
            too_high_indices = np.where(gable_conn_capacities > new_upper_gable_limit)
        
        too_low_indices = np.where(gable_conn_capacities < new_lower_gable_limit)
        while np.any(too_low_indices):
            gable_conn_capacities[too_low_indices] = np.random.normal(
                gable, new_gable_std, size=len(too_low_indices))
            too_low_indices = np.where(gable_conn_capacities < new_lower_gable_limit)         
        
    
        connection_capacities = [gable_conn_capacities[0], side_conn_capacities[0], side_conn_capacities[1],
                                  side_conn_capacities[2], side_conn_capacities[3], side_conn_capacities[4],
                                  side_conn_capacities[5], side_conn_capacities[6], side_conn_capacities[7],
                                  side_conn_capacities[8], side_conn_capacities[9], side_conn_capacities[10],
                                  side_conn_capacities[11], side_conn_capacities[12], side_conn_capacities[13],
                                  side_conn_capacities[14], side_conn_capacities[15], side_conn_capacities[16],
                                  side_conn_capacities[17], side_conn_capacities[18], side_conn_capacities[19],
                                  side_conn_capacities[20], side_conn_capacities[21], side_conn_capacities[22],
                                  side_conn_capacities[23], side_conn_capacities[24], side_conn_capacities[25],
                                  side_conn_capacities[26], side_conn_capacities[27], side_conn_capacities[28],
                                  gable_conn_capacities[1], gable_conn_capacities[2], gable_conn_capacities[3], 
                                  gable_conn_capacities[4], gable_conn_capacities[5], gable_conn_capacities[6], 
                                  gable_conn_capacities[7], gable_conn_capacities[8],
                                  side_conn_capacities[29], side_conn_capacities[30],
                                  side_conn_capacities[31], side_conn_capacities[32], side_conn_capacities[33],
                                  side_conn_capacities[34], side_conn_capacities[35], side_conn_capacities[36],
                                  side_conn_capacities[37], side_conn_capacities[38], side_conn_capacities[39],
                                  side_conn_capacities[40], side_conn_capacities[41], side_conn_capacities[42],
                                  side_conn_capacities[43], side_conn_capacities[44], side_conn_capacities[45],
                                  side_conn_capacities[46], side_conn_capacities[47], side_conn_capacities[48],
                                  side_conn_capacities[49], side_conn_capacities[50], side_conn_capacities[51],
                                  side_conn_capacities[52], side_conn_capacities[53], side_conn_capacities[54],
                                  side_conn_capacities[55], side_conn_capacities[56], side_conn_capacities[57],   
                                  gable_conn_capacities[9], gable_conn_capacities[10], 
                                  gable_conn_capacities[11], gable_conn_capacities[12], gable_conn_capacities[13], 
                                  gable_conn_capacities[14], gable_conn_capacities[15]]
    elif connections == 2: # hurricane straps
        connection_COV = 0.2
        batch_COV = 0.05
        
        side_mean = 2070
        side_std = side_mean*connection_COV
        upper_side_limit = side_mean + 2*side_std
        lower_side_limit = side_mean - 2*side_std
        
        gable_mean = 1950
        gable_std = side_mean*connection_COV
        upper_gable_limit = gable_mean + 2*gable_std
        lower_gable_limit = gable_mean - 2*gable_std
        
        side = np.random.normal(side_mean, side_std, size = (1))
        too_high_indices = np.where(side > upper_side_limit)
        while np.any(too_high_indices):
            side[too_high_indices] = np.random.normal(
                side_mean, side_std, size=len(too_high_indices))
            too_high_indices = np.where(side > upper_side_limit)
        
        too_low_indices = np.where(side < lower_side_limit)
        while np.any(too_low_indices):
            side[too_low_indices] = np.random.normal(
                side_mean, side_std, size=len(too_low_indices))
            too_low_indices = np.where(side < lower_side_limit)
    
        gable = np.random.normal(gable_mean, gable_std, size = (1))
        too_high_indices = np.where(gable > upper_gable_limit)
        while np.any(too_high_indices):
            gable[too_high_indices] = np.random.normal(
                gable_mean, gable_std, size=len(too_high_indices))
            too_high_indices = np.where(gable > upper_gable_limit)
        
        too_low_indices = np.where(gable < lower_gable_limit)
        while np.any(too_low_indices):
            side[too_low_indices] = np.random.normal(
                gable_mean, gable_std, size=len(too_low_indices))
            too_low_indices = np.where(gable < lower_gable_limit)  
        
        new_side_std = batch_COV*side
        new_gable_std = batch_COV*gable
        new_upper_side_limit = side + 2*new_side_std
        new_lower_side_limit = side - 2*new_side_std
        new_upper_gable_limit = gable + 2*new_gable_std
        new_lower_gable_limit = gable - 2*new_gable_std        
        
        side_conn_capacities = np.random.normal(side, new_side_std, size = (58))
        too_high_indices = np.where(side_conn_capacities > new_upper_side_limit)        
        while np.any(too_high_indices):
            side_conn_capacities[too_high_indices] = np.random.normal(
                side, new_side_std, size=len(too_high_indices))
            too_high_indices = np.where(side_conn_capacities > new_upper_side_limit)
        
        too_low_indices = np.where(side_conn_capacities < new_lower_side_limit)
        while np.any(too_low_indices):
            side_conn_capacities[too_low_indices] = np.random.normal(
                side, new_side_std, size=len(too_low_indices))
            too_low_indices = np.where(side_conn_capacities < new_lower_side_limit)         
    
        gable_conn_capacities = np.random.normal(gable, new_gable_std, size = (16))
        too_high_indices = np.where(gable_conn_capacities > new_upper_gable_limit)        
        while np.any(too_high_indices):
            gable_conn_capacities[too_high_indices] = np.random.normal(
                gable, new_gable_std, size=len(too_high_indices))
            too_high_indices = np.where(gable_conn_capacities > new_upper_gable_limit)
        
        too_low_indices = np.where(gable_conn_capacities < new_lower_gable_limit)
        while np.any(too_low_indices):
            gable_conn_capacities[too_low_indices] = np.random.normal(
                gable, new_gable_std, size=len(too_low_indices))
            too_low_indices = np.where(gable_conn_capacities < new_lower_gable_limit)         
        
    
        connection_capacities = [gable_conn_capacities[0], side_conn_capacities[0], side_conn_capacities[1],
                                  side_conn_capacities[2], side_conn_capacities[3], side_conn_capacities[4],
                                  side_conn_capacities[5], side_conn_capacities[6], side_conn_capacities[7],
                                  side_conn_capacities[8], side_conn_capacities[9], side_conn_capacities[10],
                                  side_conn_capacities[11], side_conn_capacities[12], side_conn_capacities[13],
                                  side_conn_capacities[14], side_conn_capacities[15], side_conn_capacities[16],
                                  side_conn_capacities[17], side_conn_capacities[18], side_conn_capacities[19],
                                  side_conn_capacities[20], side_conn_capacities[21], side_conn_capacities[22],
                                  side_conn_capacities[23], side_conn_capacities[24], side_conn_capacities[25],
                                  side_conn_capacities[26], side_conn_capacities[27], side_conn_capacities[28],
                                  gable_conn_capacities[1], gable_conn_capacities[2], gable_conn_capacities[3], 
                                  gable_conn_capacities[4], gable_conn_capacities[5], gable_conn_capacities[6], 
                                  gable_conn_capacities[7], gable_conn_capacities[8],
                                  side_conn_capacities[29], side_conn_capacities[30],
                                  side_conn_capacities[31], side_conn_capacities[32], side_conn_capacities[33],
                                  side_conn_capacities[34], side_conn_capacities[35], side_conn_capacities[36],
                                  side_conn_capacities[37], side_conn_capacities[38], side_conn_capacities[39],
                                  side_conn_capacities[40], side_conn_capacities[41], side_conn_capacities[42],
                                  side_conn_capacities[43], side_conn_capacities[44], side_conn_capacities[45],
                                  side_conn_capacities[46], side_conn_capacities[47], side_conn_capacities[48],
                                  side_conn_capacities[49], side_conn_capacities[50], side_conn_capacities[51],
                                  side_conn_capacities[52], side_conn_capacities[53], side_conn_capacities[54],
                                  side_conn_capacities[55], side_conn_capacities[56], side_conn_capacities[57],   
                                  gable_conn_capacities[9], gable_conn_capacities[10], 
                                  gable_conn_capacities[11], gable_conn_capacities[12], gable_conn_capacities[13], 
                                  gable_conn_capacities[14], gable_conn_capacities[15]]

failed_connections = np.full(74,1)
for i in range(len(failed_connections)):
    if connection_loads[i] > connection_capacities[i]:
        failed_connections[i] = 0
        connection_loads[i-1] = connection_loads[i-1] + (connection_loads[i]/2)
        connection_loads[i+1] = connection_loads[i+1] + (connection_loads[i]/2)
        connection_loads[i] = 0
        
zz = np.count_nonzero(failed_connections==0)
if zz != 0:
    zz_old = zz + 1
    while zz > zz_old:
        zz_old = zz
        for i in range(len(failed_connections)):
            if connection_loads[i] > connection_capacities[i]:
                failed_connections[i] = 0
                connection_loads[i-1] = connection_loads[i-1] + (connection_loads[i]/2)
                connection_loads[i+1] = connection_loads[i+1] + (connection_loads[i]/2)
                connection_loads[i] = 0
        zz = np.count_nonzero(failed_connections==0)

back_wall_connections = [failed_connections[1],failed_connections[2],failed_connections[3],failed_connections[4],failed_connections[5],
                     failed_connections[6],failed_connections[7],failed_connections[8],failed_connections[9],failed_connections[10],
                     failed_connections[11],failed_connections[12],failed_connections[13],failed_connections[14],failed_connections[15],
                     failed_connections[16],failed_connections[17],failed_connections[18],failed_connections[19],failed_connections[20],
                     failed_connections[21],failed_connections[22],failed_connections[23],failed_connections[24],failed_connections[25],    
                     failed_connections[26],failed_connections[27],failed_connections[28]]; 
front_wall_connections = [failed_connections[37],failed_connections[38],failed_connections[39],failed_connections[40],failed_connections[41],
                    failed_connections[42],failed_connections[43],failed_connections[44],failed_connections[45],failed_connections[46],
                    failed_connections[47],failed_connections[48],failed_connections[49],failed_connections[50],failed_connections[51],
                    failed_connections[52],failed_connections[53],failed_connections[54],failed_connections[55],failed_connections[56],
                    failed_connections[57],failed_connections[58],failed_connections[59],failed_connections[60],failed_connections[61],
                    failed_connections[62],failed_connections[63],failed_connections[64]]; 
right_wall_connections = [failed_connections[29],failed_connections[30],failed_connections[31],failed_connections[32],failed_connections[33],
                    failed_connections[34],failed_connections[35],failed_connections[36]];
left_wall_connections = [failed_connections[65],failed_connections[66],failed_connections[67],failed_connections[68],failed_connections[69],
                    failed_connections[70],failed_connections[71],failed_connections[0]];
back_fail_conn_count = np.count_nonzero(back_wall_connections==0)
front_fail_conn_count = np.count_nonzero(front_wall_connections==0)
right_fail_conn_count = np.count_nonzero(right_wall_connections==0)
left_fail_conn_count = np.count_nonzero(left_wall_connections==0)

## wall uplift
back_wall_uplift = (connection_loads[1]+connection_loads[2]+connection_loads[3]+connection_loads[4]+connection_loads[5]+
                     connection_loads[6]+connection_loads[7]+connection_loads[8]+connection_loads[9]+connection_loads[10]+
                     connection_loads[11]+connection_loads[12]+connection_loads[13]+connection_loads[14]+connection_loads[15]+
                     connection_loads[16]+connection_loads[17]+connection_loads[18]+connection_loads[19]+connection_loads[20]+
                     connection_loads[21]+connection_loads[22]+connection_loads[23]+connection_loads[24]+connection_loads[25]+    
                     connection_loads[26]+connection_loads[27]+connection_loads[28])/60; 
front_wall_uplift = (connection_loads[37]+connection_loads[38]+connection_loads[39]+connection_loads[40]+connection_loads[41]+
                    connection_loads[42]+connection_loads[43]+connection_loads[44]+connection_loads[45]+connection_loads[46]+
                    connection_loads[47]+connection_loads[48]+connection_loads[49]+connection_loads[50]+connection_loads[51]+
                    connection_loads[52]+connection_loads[53]+connection_loads[54]+connection_loads[55]+connection_loads[56]+
                    connection_loads[57]+connection_loads[58]+connection_loads[59]+connection_loads[60]+connection_loads[61]+    
                    connection_loads[62]+connection_loads[63]+connection_loads[64])/60; 
right_wall_uplift = (connection_loads[29]+connection_loads[30]+connection_loads[31]+connection_loads[32]+connection_loads[33]+
                    connection_loads[34]+connection_loads[35]+connection_loads[36])/44
left_wall_uplift = (connection_loads[65]+connection_loads[66]+connection_loads[67]+connection_loads[68]+connection_loads[69]+
                    connection_loads[70]+connection_loads[71]+connection_loads[0])/44

uplift_loads = [front_wall_uplift,left_wall_uplift,back_wall_uplift,right_wall_uplift]

## wall bending
if direction == 1:
    front_wall_bending = abs((p_windward_CC*10**2)/8)
    back_wall_bending = abs((p_leeward_CC*10**2)/8)
    left_wall_bending1 = abs((p_side_CC*19.167**2)/8)
    left_wall_bending2 = abs((p_sideleading_CC*11.833**2)/8)
    left_wall_bending = max(left_wall_bending1, left_wall_bending2)
    right_wall_bending = left_wall_bending
if direction == 2:
    front_wall_bending = abs((p_windward_CC*10**2)/8)
    back_wall_bending1 = abs((p_side_CC*10**2)/8)
    back_wall_bending2 = abs((p_sideleading_CC*10**2)/8)
    back_wall_bending = max(back_wall_bending1, back_wall_bending2)
    left_wall_bending = abs((p_windward_CC*19.167**2)/8)
    right_wall_bending1 = abs((p_side_CC*19.167**2)/8)
    right_wall_bending2 = abs((p_sideleading_CC*11.833**2)/8)
    right_wall_bending = max(right_wall_bending1, right_wall_bending2)
if direction == 3:
    front_wall_bending1 = abs((p_side_CC*10**2)/8)
    front_wall_bending2 = abs((p_sideleading_CC*10**2)/8)
    front_wall_bending = max(front_wall_bending1, front_wall_bending2)
    back_wall_bending = front_wall_bending
    left_wall_bending = abs((p_windward_CC*19.167**2)/8)
    right_wall_bending = abs((p_leeward_CC*19.167**2)/8)
if direction == 4:
    back_wall_bending = abs((p_windward_CC*10**2)/8)
    front_wall_bending1 = abs((p_side_CC*10**2)/8)
    front_wall_bending2 = abs((p_sideleading_CC*10**2)/8)
    front_wall_bending = max(front_wall_bending1, front_wall_bending2)
    left_wall_bending = abs((p_windward_CC*19.167**2)/8)
    right_wall_bending1 = abs((p_side_CC*19.167**2)/8)
    right_wall_bending2 = abs((p_sideleading_CC*11.833**2)/8)
    right_wall_bending = max(right_wall_bending1, right_wall_bending2)    
if direction == 5:
    back_wall_bending = abs((p_windward_CC*10**2)/8)
    front_wall_bending = abs((p_leeward_CC*10**2)/8)
    left_wall_bending1 = abs((p_side_CC*19.167**2)/8)
    left_wall_bending2 = abs((p_sideleading_CC*11.833**2)/8)
    left_wall_bending = max(left_wall_bending1, left_wall_bending2)
    right_wall_bending = left_wall_bending   
if direction == 6:
    back_wall_bending = abs((p_windward_CC*10**2)/8)
    front_wall_bending1 = abs((p_side_CC*10**2)/8)
    front_wall_bending2 = abs((p_sideleading_CC*10**2)/8)
    front_wall_bending = max(front_wall_bending1, front_wall_bending2)
    right_wall_bending = abs((p_windward_CC*19.167**2)/8)
    left_wall_bending1 = abs((p_side_CC*19.167**2)/8)
    left_wall_bending2 = abs((p_sideleading_CC*11.833**2)/8)
    left_wall_bending = max(left_wall_bending1, left_wall_bending2)     
if direction == 7:
    front_wall_bending1 = abs((p_side_CC*10**2)/8)
    front_wall_bending2 = abs((p_sideleading_CC*10**2)/8)
    front_wall_bending = max(front_wall_bending1, front_wall_bending2)
    back_wall_bending = front_wall_bending
    right_wall_bending = abs((p_windward_CC*19.167**2)/8)
    left_wall_bending = abs((p_leeward_CC*19.167**2)/8)    
if direction == 8:
    front_wall_bending = abs((p_windward_CC*10**2)/8)
    back_wall_bending1 = abs((p_side_CC*10**2)/8)
    back_wall_bending2 = abs((p_sideleading_CC*10**2)/8)
    back_wall_bending = max(back_wall_bending1, back_wall_bending2)
    right_wall_bending = abs((p_windward_CC*19.167**2)/8)
    left_wall_bending1 = abs((p_side_CC*19.167**2)/8)
    left_wall_bending2 = abs((p_sideleading_CC*11.833**2)/8)
    left_wall_bending = max(left_wall_bending1, left_wall_bending2)       

if back_fail_conn_count > 14:
    back_wall_bending = back_wall_bending*2.8
if front_fail_conn_count > 14:
    front_wall_bending = front_wall_bending*2.8
if right_fail_conn_count > 4:
    right_wall_bending = right_wall_bending*2.8
if left_fail_conn_count > 4:
    left_wall_bending = left_wall_bending*2.8
    
bending_loads = [front_wall_bending,left_wall_bending,back_wall_bending,right_wall_bending]

## lateral loads
if direction == 1:
    if front_fail_conn_count <= 14:
        front_lateral = p_windward_CC*3*30*10/2
    elif front_fail_conn_count > 14:
        front_lateral = p_windward_CC*0.5*30*10
        
    if left_fail_conn_count <= 4:
        left_lateral = (p_side_CC*3*22*14.583/2)-(p_side_CC*0.5*4.4*5.83)+(p_sideleading_CC*0.5*4.4*5.83)
    elif left_fail_conn_count > 4:
        left_lateral = (p_side_CC*0.5*22*14.583)-(p_side_CC*0.5*4.4*5.83)+(p_sideleading_CC*0.5*4.4*5.83)
        
    if back_fail_conn_count <= 14:
        back_lateral = p_leeward_CC*3*30*10/2
    elif back_fail_conn_count > 14:
        back_lateral = p_leeward_CC*0.5*30*10
        
    if right_fail_conn_count <= 4:
        right_lateral = (p_side_CC*3*22*14.583/2)-(p_side_CC*0.5*4.4*5.83)+(p_sideleading_CC*0.5*4.4*5.83)
    elif right_fail_conn_count > 4:
        right_lateral = (p_side_CC*0.5*22*14.583)-(p_side_CC*0.5*4.4*5.83)+(p_sideleading_CC*0.5*4.4*5.83)
if direction == 2:
    if front_fail_conn_count <= 14:
        front_lateral = p_windward_CC*3*30*10/2
    elif front_fail_conn_count > 14:
        front_lateral = p_windward_CC*0.5*30*10
        
    if left_fail_conn_count <= 4:
        left_lateral = p_windward_CC*3*22*14.583/2
    elif left_fail_conn_count > 4:
        left_lateral = p_windward_CC*0.5*22*14.583
        
    if back_fail_conn_count <= 14:
        back_lateral = (p_side_CC*3*30*10/2)-(p_side_CC*0.5*4.4*2.93)+(p_sideleading_CC*0.5*4.4*2.93)
    elif back_fail_conn_count > 14:
        back_lateral = (p_side_CC*0.5*30*10)-(p_side_CC*0.5*4.4*2.93)+(p_sideleading_CC*0.5*4.4*2.93)
    
    if right_fail_conn_count <= 4:
        right_lateral = (p_side_CC*3*22*14.583/2)-(p_side_CC*0.5*4.4*5.83)+(p_sideleading_CC*0.5*4.4*5.83)
    elif right_fail_conn_count > 4:
        right_lateral = (p_side_CC*0.5*22*14.583)-(p_side_CC*0.5*4.4*5.83)+(p_sideleading_CC*0.5*4.4*5.83)
if direction == 3:
    if front_fail_conn_count <= 14:
        front_lateral = (p_side_CC*3*30*10/2)-(p_side_CC*0.5*4.4*2.93)+(p_sideleading_CC*0.5*4.4*2.93)
    elif front_fail_conn_count > 14:
        front_lateral = (p_side_CC*0.5*30*10)-(p_side_CC*0.5*4.4*2.93)+(p_sideleading_CC*0.5*4.4*2.93)
        
    if left_fail_conn_count <= 4:
        left_lateral = p_windward_CC*3*22*14.583/2
    elif left_fail_conn_count > 4:
        left_lateral = p_windward_CC*0.5*22*14.583      
        
    if back_fail_conn_count <= 14:
        back_lateral = (p_side_CC*3*30*10/2)-(p_side_CC*0.5*4.4*2.93)+(p_sideleading_CC*0.5*4.4*2.93)
    elif back_fail_conn_count > 14:
        back_lateral = (p_side_CC*0.5*30*10)-(p_side_CC*0.5*4.4*2.93)+(p_sideleading_CC*0.5*4.4*2.93)   
        
    if right_fail_conn_count <= 4:
        right_lateral = p_leeward_CC*3*22*14.583/2
    elif right_fail_conn_count > 4:
        right_lateral = p_leeward_CC*0.5*22*14.583
if direction == 4:
    if front_fail_conn_count <= 14:
        front_lateral = (p_side_CC*3*30*10/2)-(p_side_CC*0.5*4.4*2.93)+(p_sideleading_CC*0.5*4.4*2.93)
    elif front_fail_conn_count > 14:
        front_lateral = (p_side_CC*0.5*30*10)-(p_side_CC*0.5*4.4*2.93)+(p_sideleading_CC*0.5*4.4*2.93)
        
    if left_fail_conn_count <= 4:
        left_lateral = p_windward_CC*3*22*14.583/2
    elif left_fail_conn_count > 4:
        left_lateral = p_windward_CC*0.5*22*14.583      
        
    if back_fail_conn_count <= 14:
        back_lateral = p_windward_CC*3*30*10/2
    elif back_fail_conn_count > 14:
        back_lateral = p_windward_CC*0.5*30*10
        
    if right_fail_conn_count <= 4:
        right_lateral = (p_side_CC*3*22*14.583/2)-(p_side_CC*0.5*4.4*5.83)+(p_sideleading_CC*0.5*4.4*5.83)
    elif right_fail_conn_count > 4:
        right_lateral = (p_side_CC*0.5*22*14.583)-(p_side_CC*0.5*4.4*5.83)+(p_sideleading_CC*0.5*4.4*5.83)
if direction == 5:
    if front_fail_conn_count <= 14:
        front_lateral = p_leeward_CC*3*30*10/2
    elif front_fail_conn_count > 14:
        front_lateral = p_leeward_CC*0.5*30*10
        
    if left_fail_conn_count <= 4:
        left_lateral = (p_side_CC*3*22*14.583/2)-(p_side_CC*0.5*4.4*5.83)+(p_sideleading_CC*0.5*4.4*5.83)
    elif left_fail_conn_count > 4:
        left_lateral = (p_side_CC*0.5*22*14.583)-(p_side_CC*0.5*4.4*5.83)+(p_sideleading_CC*0.5*4.4*5.83)
        
    if back_fail_conn_count <= 14:
        back_lateral = p_windward_CC*3*30*10/2
    elif back_fail_conn_count > 14:
        back_lateral = p_windward_CC*0.5*30*10
        
    if right_fail_conn_count <= 4:
        right_lateral = (p_side_CC*3*22*14.583/2)-(p_side_CC*0.5*4.4*5.83)+(p_sideleading_CC*0.5*4.4*5.83)
    elif right_fail_conn_count > 4:
        right_lateral = (p_side_CC*0.5*22*14.583)-(p_side_CC*0.5*4.4*5.83)+(p_sideleading_CC*0.5*4.4*5.83)
if direction == 6:
    if front_fail_conn_count <= 14:
        front_lateral = (p_side_CC*3*30*10/2)-(p_side_CC*0.5*4.4*2.93)+(p_sideleading_CC*0.5*4.4*2.93)
    elif front_fail_conn_count > 14:
        front_lateral = (p_side_CC*0.5*30*10)-(p_side_CC*0.5*4.4*2.93)+(p_sideleading_CC*0.5*4.4*2.93)
        
    if left_fail_conn_count <= 4:
        left_lateral = (p_side_CC*3*22*14.583/2)-(p_side_CC*0.5*4.4*5.83)+(p_sideleading_CC*0.5*4.4*5.83)
    elif left_fail_conn_count > 4:
        left_lateral = (p_side_CC*0.5*22*14.583)-(p_side_CC*0.5*4.4*5.83)+(p_sideleading_CC*0.5*4.4*5.83)
        
    if back_fail_conn_count <= 14:
        back_lateral = p_windward_CC*3*30*10/2
    elif back_fail_conn_count > 14:
        back_lateral = p_windward_CC*0.5*30*10
        
    if right_fail_conn_count <= 4:
        right_lateral = p_windward_CC*3*22*14.583/2
    elif right_fail_conn_count > 4:
        right_lateral = p_windward_CC*0.5*22*14.583 
if direction == 7:
    if front_fail_conn_count <= 14:
        front_lateral = (p_side_CC*3*30*10/2)-(p_side_CC*0.5*4.4*2.93)+(p_sideleading_CC*0.5*4.4*2.93)
    elif front_fail_conn_count > 14:
        front_lateral = (p_side_CC*0.5*30*10)-(p_side_CC*0.5*4.4*2.93)+(p_sideleading_CC*0.5*4.4*2.93)

    if left_fail_conn_count <= 4:
        left_lateral = p_leeward_CC*3*22*14.583/2
    elif left_fail_conn_count > 4:
        left_lateral = p_leeward_CC*0.5*22*14.583
        
    if back_fail_conn_count <= 14:
        back_lateral = (p_side_CC*3*30*10/2)-(p_side_CC*0.5*4.4*2.93)+(p_sideleading_CC*0.5*4.4*2.93)
    elif back_fail_conn_count > 14:
        back_lateral = (p_side_CC*0.5*30*10)-(p_side_CC*0.5*4.4*2.93)+(p_sideleading_CC*0.5*4.4*2.93)   

    if right_fail_conn_count <= 4:
        right_lateral = p_windward_CC*3*22*14.583/2
    elif right_fail_conn_count > 4:
        right_lateral = p_windward_CC*0.5*22*14.583 
if direction == 8:
    if front_fail_conn_count <= 14:
        front_lateral = p_windward_CC*3*30*10/2
    elif front_fail_conn_count > 14:
        front_lateral = p_windward_CC*0.5*30*10
        
    if left_fail_conn_count <= 4:
        left_lateral = (p_side_CC*3*22*14.583/2)-(p_side_CC*0.5*4.4*5.83)+(p_sideleading_CC*0.5*4.4*5.83)
    elif left_fail_conn_count > 4:
        left_lateral = (p_side_CC*0.5*22*14.583)-(p_side_CC*0.5*4.4*5.83)+(p_sideleading_CC*0.5*4.4*5.83)
        
    if back_fail_conn_count <= 14:
        back_lateral = (p_side_CC*3*30*10/2)-(p_side_CC*0.5*4.4*2.93)+(p_sideleading_CC*0.5*4.4*2.93)
    elif back_fail_conn_count > 14:
        back_lateral = (p_side_CC*0.5*30*10)-(p_side_CC*0.5*4.4*2.93)+(p_sideleading_CC*0.5*4.4*2.93)   

    if right_fail_conn_count <= 4:
        right_lateral = p_windward_CC*3*22*14.583/2
    elif right_fail_conn_count > 4:
        right_lateral = p_windward_CC*0.5*22*14.583 

front_lateral = abs(front_lateral)/45
left_lateral = abs(left_lateral)/33
back_lateral = abs(back_lateral)/45
right_lateral = abs(right_lateral)/33
lateral_loads = [front_lateral,left_lateral,back_lateral,right_lateral]

## wall sheathing
if direction == 1:
    wall_sheath_loads = [p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC,
                         p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, 
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC,
                         p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC,
                         p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC,
                         p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC,
                         p_leeward_CC, p_leeward_CC, p_leeward_CC,
                         p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, 
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC]
if direction == 2:
    wall_sheath_loads = [p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, 
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, 
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC]
if direction == 3:
    wall_sheath_loads = [p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, 
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, 
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC,
                         p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC,
                         p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC,
                         p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC,
                         p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC]
if direction == 4:
    wall_sheath_loads = [p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, 
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC,
                         p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, 
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC]
if direction == 5:
    wall_sheath_loads = [p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC,
                         p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC,
                         p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC,
                         p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC,
                         p_leeward_CC, p_leeward_CC, p_leeward_CC, 
                         p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, 
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC,
                         p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, 
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC]
if direction == 6:
    wall_sheath_loads = [p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, 
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, 
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC]
if direction == 7:
    wall_sheath_loads = [p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, 
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC,
                         p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC,
                         p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC,
                         p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC,
                         p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC,
                         p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, 
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC]
if direction == 8:
    wall_sheath_loads = [p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC,
                         p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, 
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, 
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC]
   
wall_sheath_loads = np.absolute(wall_sheath_loads)



## wall capacities and failure check
if walls ==1:
    lateral_mean_capacity = 1232
    lateral_COV = 0.25
    lateral_std = lateral_COV*lateral_mean_capacity
    upper_lateral_limit = lateral_mean_capacity + 2*lateral_std
    lower_lateral_limit = lateral_mean_capacity - 2*lateral_std
    lateral_capacity = np.random.normal(lateral_mean_capacity, lateral_std, size = (4))

    too_high_indices = np.where(lateral_capacity > upper_lateral_limit)
    while np.any(too_high_indices):
        lateral_capacity[too_high_indices] = np.random.normal(
            lateral_mean_capacity, lateral_std, size=len(too_high_indices))
        too_high_indices = np.where(lateral_capacity > upper_lateral_limit)
    
    too_low_indices = np.where(lateral_capacity < lower_lateral_limit)
    while np.any(too_low_indices):
        lateral_capacity[too_low_indices] = np.random.normal(
            lateral_mean_capacity, lateral_std, size=len(too_low_indices))
        too_low_indices = np.where(lateral_capacity < lower_lateral_limit)
        
    lateraladd_mean_capacity = 794
    lateraladd_COV = 0.25
    lateraladd_std = lateraladd_COV*lateraladd_mean_capacity
    upper_lateraladd_limit = lateraladd_mean_capacity + 2*lateraladd_std
    lower_lateraladd_limit = lateraladd_mean_capacity - 2*lateraladd_std
    lateraladd_capacity = np.random.normal(lateraladd_mean_capacity, lateraladd_std, size = (4))

    too_high_indices = np.where(lateraladd_capacity > upper_lateraladd_limit)
    while np.any(too_high_indices):
        lateraladd_mean_capacity[too_high_indices] = np.random.normal(
            lateraladd_capacity, lateraladd_std, size=len(too_high_indices))
        too_high_indices = np.where(lateraladd_capacity > upper_lateraladd_limit)
    
    too_low_indices = np.where(lateraladd_capacity < lower_lateraladd_limit)
    while np.any(too_low_indices):
        lateraladd_capacity[too_low_indices] = np.random.normal(
            lateraladd_mean_capacity, lateraladd_std, size=len(too_low_indices))
        too_low_indices = np.where(lateraladd_capacity < lower_lateraladd_limit)

    front_lateral_capacity = lateral_capacity[0] + lateraladd_capacity[0]
    left_lateral_capacity = lateral_capacity[1] + lateraladd_capacity[1]
    back_lateral_capacity = lateral_capacity[2] + lateraladd_capacity[2]
    right_lateral_capacity = lateral_capacity[3] + lateraladd_capacity[3]
    total_lateral_capacity = [front_lateral_capacity, left_lateral_capacity, back_lateral_capacity, right_lateral_capacity]
    
    uplift_mean_capacity = 616
    uplift_COV = 0.25
    uplift_std = uplift_COV*uplift_mean_capacity
    upper_uplift_limit = uplift_mean_capacity + 2*uplift_std
    lower_uplift_limit = uplift_mean_capacity - 2*uplift_std
    uplift_capacity = np.random.normal(uplift_mean_capacity, uplift_std, size = (4))

    too_high_indices = np.where(uplift_capacity > upper_uplift_limit)
    while np.any(too_high_indices):
        uplift_capacity[too_high_indices] = np.random.normal(
            uplift_mean_capacity, uplift_std, size=len(too_high_indices))
        too_high_indices = np.where(uplift_capacity > upper_uplift_limit)
    
    too_low_indices = np.where(uplift_capacity < lower_uplift_limit)
    while np.any(too_low_indices):
        uplift_capacity[too_low_indices] = np.random.normal(
            uplift_mean_capacity, uplift_std, size=len(too_low_indices))
        too_low_indices = np.where(uplift_capacity < lower_uplift_limit)
        
    upliftadd_mean_capacity = 397
    upliftadd_COV = 0.25
    upliftadd_std = upliftadd_COV*upliftadd_mean_capacity
    upper_upliftadd_limit = upliftadd_mean_capacity + 2*upliftadd_std
    lower_upliftadd_limit = upliftadd_mean_capacity - 2*upliftadd_std
    upliftadd_capacity = np.random.normal(upliftadd_mean_capacity, upliftadd_std, size = (4))

    too_high_indices = np.where(upliftadd_capacity > upper_upliftadd_limit)
    while np.any(too_high_indices):
        upliftadd_capacity[too_high_indices] = np.random.normal(
            upliftadd_mean_capacity, upliftadd_std, size=len(too_high_indices))
        too_high_indices = np.where(upliftadd_capacity > upper_upliftadd_limit)
    
    too_low_indices = np.where(upliftadd_capacity < lower_upliftadd_limit)
    while np.any(too_low_indices):
        upliftadd_capacity[too_low_indices] = np.random.normal(
            upliftadd_mean_capacity, upliftadd_std, size=len(too_low_indices))
        too_low_indices = np.where(upliftadd_capacity < lower_upliftadd_limit)

    front_uplift_capacity = uplift_capacity[0] + upliftadd_capacity[0]  
    left_uplift_capacity = uplift_capacity[1] + upliftadd_capacity[1] 
    back_uplift_capacity = uplift_capacity[2] + upliftadd_capacity[2] 
    right_uplift_capacity = uplift_capacity[3] + upliftadd_capacity[3] 
    total_uplift_capacity = [front_uplift_capacity, left_uplift_capacity, back_uplift_capacity, right_uplift_capacity]

    wallsheath_mean_capacity = 126
    wallsheath_COV = 0.4
    wallsheath_std = wallsheath_COV*wallsheath_mean_capacity
    upper_wallsheath_limit = wallsheath_mean_capacity + 2*wallsheath_std
    lower_wallsheath_limit = wallsheath_mean_capacity - 2*wallsheath_std
    wall_sheath_capacity = np.random.normal(wallsheath_mean_capacity, wallsheath_std, size = (118))

    too_high_indices = np.where(wall_sheath_capacity > upper_wallsheath_limit)
    while np.any(too_high_indices):
        wall_sheath_capacity[too_high_indices] = np.random.normal(
            wallsheath_mean_capacity, wallsheath_std, size=len(too_high_indices))
        too_high_indices = np.where(wall_sheath_capacity > upper_wallsheath_limit)
    
    too_low_indices = np.where(wall_sheath_capacity < lower_wallsheath_limit)
    while np.any(too_low_indices):
        wall_sheath_capacity[too_low_indices] = np.random.normal(
            wallsheath_mean_capacity, wallsheath_std, size=len(too_low_indices))
        too_low_indices = np.where(wall_sheath_capacity < lower_wallsheath_limit)
        
    failed_walls_uplift = np.full(4, 1)
    for i in range(len(failed_walls_uplift)):
        if uplift_loads[i] > total_uplift_capacity[i]:
            failed_walls_uplift[i] = 0
    failed_walls_lateral = np.full(4, 1)
    for i in range(len(failed_walls_lateral)):
        if lateral_loads[i] > total_lateral_capacity[i]:
            failed_walls_lateral[i] = 0
    failed_walls_sheath = np.full(118, 1, dtype = int)
    for i in range(len(failed_walls_sheath)):
        if wall_sheath_loads[i] > wall_sheath_capacity[i]:
            failed_walls_sheath[i] = 0
            
    failed_walls = np.full(4, 1)
    for i in range(len(failed_walls)):
        if failed_walls_uplift[i] < 1:
            failed_walls[i] = 0
        if failed_walls_lateral[i] < 1:
            failed_walls[i] = 0

        
        
elif walls == 2:
    uplift_mean_capacity = 4000
    uplift_COV = 0.2
    uplift_std = uplift_COV*uplift_mean_capacity
    upper_uplift_limit = uplift_mean_capacity + 2*uplift_std
    lower_uplift_limit = uplift_mean_capacity - 2*uplift_std
    uplift_capacity = np.random.normal(uplift_mean_capacity, uplift_std, size = (4))

    too_high_indices = np.where(uplift_capacity > upper_uplift_limit)
    while np.any(too_high_indices):
        uplift_capacity[too_high_indices] = np.random.normal(
            uplift_mean_capacity, uplift_std, size=len(too_high_indices))
        too_high_indices = np.where(uplift_capacity > upper_uplift_limit)
    
    too_low_indices = np.where(uplift_capacity < lower_uplift_limit)
    while np.any(too_low_indices):
        uplift_capacity[too_low_indices] = np.random.normal(
            uplift_mean_capacity, uplift_std, size=len(too_low_indices))
        too_low_indices = np.where(uplift_capacity < lower_uplift_limit)
        
    front_uplift_capacity = uplift_capacity[0]
    left_uplift_capacity = uplift_capacity[1]
    back_uplift_capacity = uplift_capacity[2]
    right_uplift_capacity = uplift_capacity[3]
    total_uplift_capacity = [front_uplift_capacity, left_uplift_capacity, back_uplift_capacity, right_uplift_capacity]
        
    bending_mean_capacity = 11588
    bending_COV = 0.2
    bending_std = bending_COV*bending_mean_capacity
    upper_bending_limit = bending_mean_capacity + 2*bending_std
    lower_bending_limit = bending_mean_capacity - 2*bending_std
    bending_capacity = np.random.normal(bending_mean_capacity, bending_std, size = (4))

    too_high_indices = np.where(bending_capacity > upper_bending_limit)
    while np.any(too_high_indices):
        bending_capacity[too_high_indices] = np.random.normal(
            bending_mean_capacity, bending_std, size=len(too_high_indices))
        too_high_indices = np.where(bending_capacity > upper_bending_limit)
    
    too_low_indices = np.where(bending_capacity < lower_bending_limit)
    while np.any(too_low_indices):
        bending_capacity[too_low_indices] = np.random.normal(
            bending_mean_capacity, bending_std, size=len(too_low_indices))
        too_low_indices = np.where(bending_capacity < lower_bending_limit)
        
    front_bending_capacity = bending_capacity[0]
    left_bending_capacity = bending_capacity[1]
    back_bending_capacity = bending_capacity[2]
    right_bending_capacity = bending_capacity[3]
    total_bending_capacity = [front_bending_capacity, left_bending_capacity, back_bending_capacity, right_bending_capacity]

    u_front = (front_wall_bending/front_bending_capacity)+(front_wall_uplift/front_uplift_capacity)
    u_left = (left_wall_bending/left_bending_capacity)+(left_wall_uplift/left_uplift_capacity)
    u_back = (back_wall_bending/back_bending_capacity)+(back_wall_uplift/back_uplift_capacity)
    u_right = (right_wall_bending/right_bending_capacity)+(right_wall_uplift/right_uplift_capacity)
    u = [u_front, u_left, u_back, u_right]
    
    failed_walls_u = np.full(4, 1)
    for i in range(len(failed_walls_u)):
        if u[i] > 1:
            failed_walls_u[i] = 0
            
    failed_walls = failed_walls_u
    
    failed_walls_sheath = np.full(118, 1)
            
 
    
## internal pressure recalculation
initial_failures = [garage_fail, front_door_fail, back_door_fail, failed_frontwindows[0], failed_frontwindows[1],
                    failed_frontwindows[2], failed_leftwindows[0], failed_leftwindows[1], failed_leftwindows[2],
                    failed_leftwindows[3], failed_backwindows[0], failed_backwindows[1], failed_backwindows[2],
                    failed_backwindows[3], failed_rightwindows[0], failed_rightwindows[1], failed_rightwindows[2],
                    failed_rightwindows[3]]
failed_openings_count = 18 - np.count_nonzero(initial_failures)

if failed_openings_count == 0:
    cp_rand[0,0] = cp_rand[0,0]
else:
    if garage_fail == 1:
        gar = 0
    elif garage_fail == 0:
        gar = 1
        
    open_failures = [front_door_fail, back_door_fail, failed_frontwindows[0], failed_frontwindows[1],
                    failed_frontwindows[2], failed_leftwindows[0], failed_leftwindows[1], failed_leftwindows[2],
                    failed_leftwindows[3], failed_backwindows[0], failed_backwindows[1], failed_backwindows[2],
                    failed_backwindows[3], failed_rightwindows[0], failed_rightwindows[1], failed_rightwindows[2],
                    failed_rightwindows[3]]
    n = 17 - np.count_nonzero(open_failures)    

    front_failures = [front_door_fail, failed_frontwindows[0], failed_frontwindows[1],failed_frontwindows[2]]   
    a1 = 4 - np.count_nonzero(front_failures)
    left_failures = [failed_leftwindows[1], failed_leftwindows[2], failed_leftwindows[3]]
    a2 = 3 - np.count_nonzero(left_failures)
    b2 = 1 - np.count_nonzero(failed_leftwindows[0])
    back_failures = [back_door_fail, failed_backwindows[1], failed_backwindows[2], failed_backwindows[3]]
    a3 = 4 - np.count_nonzero(back_failures)
    b3 = 1 - np.count_nonzero(failed_backwindows[0])
    right_failures = [failed_rightwindows[1], failed_rightwindows[2], failed_rightwindows[3]]
    a4 = 3 - np.count_nonzero(right_failures)
    b4 = 1 - np.count_nonzero(failed_rightwindows[0])
    
    if direction == 1:
        pg = cp_rand[0,4]
        
        pi1 = a1*cp_rand[0,4]
        pi2 = a2*cp_rand[0,6]+b2*cp_rand[0,5]
        pi3 = a3*cp_rand[0,7]+b3*cp_rand[0,7]
        pi4 = a4*cp_rand[0,6]+b4*cp_rand[0,5]
        
    if direction == 2:
        pg = cp_rand[0,4]
        
        pi1 = a1*cp_rand[0,4]
        pi2 = a2*cp_rand[0,4]+b2*cp_rand[0,4]
        pi3 = a3*cp_rand[0,6]+b3*cp_rand[0,5]
        pi4 = a4*cp_rand[0,6]+b4*cp_rand[0,5]
        
    if direction == 3: 
        pg = cp_rand[0,5]
        
        pi1 = a1*cp_rand[0,6]
        pi2 = a2*cp_rand[0,4]+b2*cp_rand[0,4]
        pi3 = a3*cp_rand[0,6]+b3*cp_rand[0,5]
        pi4 = a4*cp_rand[0,7]+b4*cp_rand[0,7]
        
    if direction == 4:
        pg = cp_rand[0,5]
        
        pi1 = a1*cp_rand[0,6]
        pi2 = a2*cp_rand[0,4]+b2*cp_rand[0,4]
        pi3 = a3*cp_rand[0,4]+b3*cp_rand[0,4]
        pi4 = a4*cp_rand[0,6]+b4*cp_rand[0,5]
        
    if direction == 5:
        pg = cp_rand[0,7]
        
        pi1 = a1*cp_rand[0,7]
        pi2 = a2*cp_rand[0,6]+b2*cp_rand[0,5]
        pi3 = a3*cp_rand[0,4]+b3*cp_rand[0,4]
        pi4 = a4*cp_rand[0,6]+b4*cp_rand[0,5]
        
    if direction == 6:
        pg = cp_rand[0,6]
        
        pi1 = a1*cp_rand[0,6]
        pi2 = a2*cp_rand[0,6]+b2*cp_rand[0,5]
        pi3 = a3*cp_rand[0,4]+b3*cp_rand[0,4]
        pi4 = a4*cp_rand[0,4]+b4*cp_rand[0,4]
        
    if direction == 7:
        pg = cp_rand[0,6]
        
        pi1 = a1*cp_rand[0,6]
        pi2 = a2*cp_rand[0,7]+b2*cp_rand[0,7]
        pi3 = a3*cp_rand[0,7]+b3*cp_rand[0,7]
        pi4 = a4*cp_rand[0,4]+b4*cp_rand[0,4]
        
    if direction == 8:
        pg = cp_rand[0,4]

        pi1 = a1*cp_rand[0,4]
        pi2 = a2*cp_rand[0,6]+b2*cp_rand[0,5]
        pi3 = a3*cp_rand[0,6]+b3*cp_rand[0,5]
        pi4 = a4*cp_rand[0,4]+b4*cp_rand[0,4]

    pi = pi1 + pi2 + pi3 + pi4
    
    pi_old = cp_rand[0,0]
    cp_rand[0,0] = (4*gar*pg + pi)/(n+4*gar)
    
## recalculate loads
# design pressure calculation for roof sheathing
p_sheath_zone1 = qh*0.8*(cp_rand[0,1]-cp_rand[0,0])
p_sheath_zone2 = qh*0.8*(cp_rand[0,2]-cp_rand[0,0])
p_sheath_zone3 = qh*0.8*(cp_rand[0,3]-cp_rand[0,0])

# design pressure calculation for roof cover
p_cover_zone1 = qh*0.8*(cp_rand[0,1]-0)
p_cover_zone2 = qh*0.8*(cp_rand[0,2]-0)
p_cover_zone3 = qh*0.8*(cp_rand[0,3]-0)


# design pressure calculations for walls (MWFRS)
p_caseA1_MWFRS = qh*0.8*(0.85*cp_rand[0,8]-cp_rand[0,0])
p_caseA2_MWFRS = qh*0.8*(0.85*cp_rand[0,9]-cp_rand[0,0])
p_caseA3_MWFRS = qh*0.8*(0.85*cp_rand[0,10]-cp_rand[0,0])
p_caseA4_MWFRS = qh*0.8*(0.85*cp_rand[0,11]-cp_rand[0,0])
p_caseA1E_MWFRS = qh*0.8*(0.85*cp_rand[0,12]-cp_rand[0,0])
p_caseA2E_MWFRS = qh*0.8*(0.85*cp_rand[0,13]-cp_rand[0,0])
p_caseA3E_MWFRS = qh*0.8*(0.85*cp_rand[0,14]-cp_rand[0,0])
p_caseA4E_MWFRS = qh*0.8*(0.85*cp_rand[0,15]-cp_rand[0,0])

p_caseB1_MWFRS = qh*0.8*(0.85*cp_rand[0,16]-cp_rand[0,0])
p_caseB2_MWFRS = qh*0.8*(0.85*cp_rand[0,17]-cp_rand[0,0])
p_caseB3_MWFRS = qh*0.8*(0.85*cp_rand[0,18]-cp_rand[0,0])
p_caseB4_MWFRS = qh*0.8*(0.85*cp_rand[0,19]-cp_rand[0,0])
p_caseB5_MWFRS = qh*0.8*(0.85*cp_rand[0,20]-cp_rand[0,0])
p_caseB6_MWFRS = qh*0.8*(0.85*cp_rand[0,21]-cp_rand[0,0])
p_caseB1E_MWFRS = qh*0.8*(0.85*cp_rand[0,22]-cp_rand[0,0])
p_caseB2E_MWFRS = qh*0.8*(0.85*cp_rand[0,23]-cp_rand[0,0])
p_caseB3E_MWFRS = qh*0.8*(0.85*cp_rand[0,24]-cp_rand[0,0])
p_caseB4E_MWFRS = qh*0.8*(0.85*cp_rand[0,25]-cp_rand[0,0])
p_caseB5E_MWFRS = qh*0.8*(0.85*cp_rand[0,26]-cp_rand[0,0])
p_caseB6E_MWFRS = qh*0.8*(0.85*cp_rand[0,27]-cp_rand[0,0])


# design pressure calculations for walls and openings (C&C)
p_windward_CC = qh*0.8*(cp_rand[0,4]-cp_rand[0,0])
p_sideleading_CC = qh*0.8*(cp_rand[0,5]-cp_rand[0,0])
p_side_CC = qh*0.8*(cp_rand[0,6]-cp_rand[0,0])
p_leeward_CC = qh*0.8*(cp_rand[0,7]-cp_rand[0,0])

# application of loads to components based on wind direction
if direction == 1:
    cover_loads = [p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2,
                   p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2,
                   p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2,
                   p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2,
                   p_cover_zone3, p_cover_zone3, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone3,
                   p_cover_zone3, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone3, p_cover_zone3]
    
    sheath_loads = [p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2,
                   p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2,
                   p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2,
                   p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2,
                   p_sheath_zone3, p_sheath_zone3, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone3,
                   p_sheath_zone3, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone3, p_sheath_zone3]
    
    front_window_loads = [p_windward_CC, p_windward_CC, p_windward_CC]
    front_door_load = p_windward_CC
    garage_door_load = p_windward_CC
    leftside_window_loads = [p_sideleading_CC, p_side_CC, p_side_CC, p_side_CC]
    rightside_window_loads = [p_sideleading_CC, p_side_CC, p_side_CC, p_side_CC]
    back_window_loads = [p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC]
    back_door_load = p_leeward_CC

    
elif direction == 2:
    cover_loads = [p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone3, p_cover_zone3, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2,
                   p_cover_zone3, p_cover_zone3, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2,
                   p_cover_zone3, p_cover_zone3, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2]
    
    sheath_loads = [p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone3, p_sheath_zone3, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2,
                   p_sheath_zone3, p_sheath_zone3, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2,
                   p_sheath_zone3, p_sheath_zone3, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2]

    front_window_loads = [p_windward_CC, p_windward_CC, p_windward_CC]
    front_door_load = p_windward_CC
    garage_door_load = p_windward_CC
    leftside_window_loads = [p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC]
    rightside_window_loads = [p_sideleading_CC, p_side_CC, p_side_CC, p_side_CC]
    back_window_loads = [p_sideleading_CC, p_side_CC, p_side_CC, p_side_CC]
    back_door_load = p_side_CC

    
elif direction == 3:
    cover_loads = [p_cover_zone3, p_cover_zone3, p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone3, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone3, p_cover_zone3, p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone3, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone3, p_cover_zone3, p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone3, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone3, p_cover_zone3, p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone3, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1]
    
    sheath_loads = [p_sheath_zone3, p_sheath_zone3, p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone3, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone3, p_sheath_zone3, p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone3, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone3, p_sheath_zone3, p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone3, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone3, p_sheath_zone3, p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone3, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1]
  
    front_window_loads = [p_side_CC, p_side_CC, p_side_CC]
    front_door_load = p_side_CC
    garage_door_load = p_side_CC
    leftside_window_loads = [p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC]
    rightside_window_loads = [p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC]
    back_window_loads = [p_sideleading_CC, p_side_CC, p_side_CC, p_side_CC]
    back_door_load = p_side_CC

    
elif direction == 4:
    cover_loads = [p_cover_zone3, p_cover_zone3, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2,
                   p_cover_zone3, p_cover_zone3, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2,
                   p_cover_zone3, p_cover_zone3, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2,
                   p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1]
    
    sheath_loads = [p_sheath_zone3, p_sheath_zone3, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2,
                   p_sheath_zone3, p_sheath_zone3, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2,
                   p_sheath_zone3, p_sheath_zone3, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2,
                   p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1]

    front_window_loads = [p_side_CC, p_side_CC, p_side_CC]
    front_door_load = p_side_CC
    garage_door_load = p_side_CC
    leftside_window_loads = [p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC]
    rightside_window_loads = [p_sideleading_CC, p_side_CC, p_side_CC, p_side_CC]
    back_window_loads = [p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC]
    back_door_load = p_windward_CC


elif direction == 5:
    cover_loads = [p_cover_zone3, p_cover_zone3, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone3,
                   p_cover_zone3, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone3, p_cover_zone3,
                   p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2,
                   p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2,
                   p_cover_zone2, p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2,
                   p_cover_zone2, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1]
    
    sheath_loads = [p_sheath_zone3, p_sheath_zone3, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone3,
                   p_sheath_zone3, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone3, p_sheath_zone3,
                   p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2,
                   p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2,
                   p_sheath_zone2, p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2,
                   p_sheath_zone2, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1]
    
    front_window_loads = [p_leeward_CC, p_leeward_CC, p_leeward_CC]
    front_door_load = p_leeward_CC
    garage_door_load = p_leeward_CC
    leftside_window_loads = [p_sideleading_CC, p_side_CC, p_side_CC, p_side_CC]
    rightside_window_loads = [p_sideleading_CC, p_side_CC, p_side_CC, p_side_CC]
    back_window_loads = [p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC]
    back_door_load = p_windward_CC

    
elif direction == 6:
    cover_loads = [p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone3, p_cover_zone3,
                   p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone3, p_cover_zone3,
                   p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone3, p_cover_zone3,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1]
    
    sheath_loads = [p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone3, p_sheath_zone3,
                   p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone3, p_sheath_zone3,
                   p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone3, p_sheath_zone3,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1]
  
    front_window_loads = [p_side_CC, p_side_CC, p_side_CC]
    front_door_load = p_side_CC
    garage_door_load = p_side_CC
    leftside_window_loads = [p_sideleading_CC, p_side_CC, p_side_CC, p_side_CC]
    rightside_window_loads = [p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC]
    back_window_loads = [p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC]
    back_door_load = p_windward_CC
 
    
elif direction == 7:
    cover_loads = [p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone3,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2, p_cover_zone3, p_cover_zone3,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone3,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2, p_cover_zone3, p_cover_zone3,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone3,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2, p_cover_zone3, p_cover_zone3,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone3,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2, p_cover_zone3, p_cover_zone3]
    
    sheath_loads = [p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone3,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2, p_sheath_zone3, p_sheath_zone3,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone3,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2, p_sheath_zone3, p_sheath_zone3,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone3,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2, p_sheath_zone3, p_sheath_zone3,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone3,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2, p_sheath_zone3, p_sheath_zone3]
  
    front_window_loads = [p_side_CC, p_side_CC, p_side_CC]
    front_door_load = p_side_CC
    garage_door_load = p_side_CC
    leftside_window_loads = [p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC]
    rightside_window_loads = [p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC]
    back_window_loads = [p_sideleading_CC, p_side_CC, p_side_CC, p_side_CC]
    back_door_load = p_side_CC

    
elif direction == 8:
    cover_loads = [p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2,
                   p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone1, p_cover_zone2, p_cover_zone2,
                   p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone3, p_cover_zone3,
                   p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone3, p_cover_zone3,
                   p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone2, p_cover_zone3, p_cover_zone3]
    
    sheath_loads = [p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2,
                   p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone1, p_sheath_zone2, p_sheath_zone2,
                   p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone3, p_sheath_zone3,
                   p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone3, p_sheath_zone3,
                   p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone2, p_sheath_zone3, p_sheath_zone3]

    front_window_loads = [p_windward_CC, p_windward_CC, p_windward_CC]
    front_door_load = p_windward_CC
    garage_door_load = p_windward_CC
    leftside_window_loads = [p_sideleading_CC, p_side_CC, p_side_CC, p_side_CC]
    rightside_window_loads = [p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC]
    back_window_loads = [p_sideleading_CC, p_side_CC, p_side_CC, p_side_CC]
    back_door_load = p_side_CC


sheath_loads = np.array(sheath_loads)*-1
for i in range(len(failed_sheath)):
    if sheath_loads[i] > sheath_capacity[i]:
        failed_sheath[i] = 0

cover_loads = np.array(cover_loads)*-1
for i in range(len(failed_cover)):
    if cover_loads[i] > cover_capacity[i]:
        failed_cover[i] = 0
    elif failed_sheath[i] == 0:
        failed_cover[i] = 0
        
      
front_door_load = abs(front_door_load)
back_door_load = abs(back_door_load)
if front_door_load > door_capacity[0]:
    front_door_fail = 0
elif front_door_load < door_capacity[0]:
    front_door_fail = 1

if back_door_load > door_capacity[1]:
    back_door_fail = 0
elif back_door_load < door_capacity[1]:
    back_door_fail = 1

garage_door_load = abs(garage_door_load)
if garage_door_load > garage_capacity:
    garage_fail = 0
elif garage_door_load < garage_capacity:
    garage_fail = 1


leftsidewindow_loads = np.abs(leftside_window_loads)
rightsidewindow_loads = np.abs(rightside_window_loads)
for i in range(len(failed_leftwindows)):
    if leftsidewindow_loads[i] > leftsidewindow_capacity[i]:
        failed_leftwindows[i] = 0
for i in range(len(failed_rightwindows)):
    if rightsidewindow_loads[i] > rightsidewindow_capacity[i]:
        failed_rightwindows[i] = 0   
right_rand = np.random.rand(4)
left_rand = np.random.rand(4)
for i in range(len(failed_leftwindows)):
    if left_rand[i] < prob_left:
        failed_leftwindows[i] = 0
for i in range(len(failed_rightwindows)):
    if right_rand[i] < prob_right:
        failed_rightwindows[i] = 0

front_mediumwindow_loads = np.abs(front_window_loads)
back_mediumwindow_loads = np.abs(back_window_loads)
for i in range(len(failed_frontwindows)):
    if front_mediumwindow_loads[i] > front_mediumwindow_capacity[i]:
        failed_frontwindows[i] = 0
for i in range(len(failed_backwindows)):
    if back_mediumwindow_loads[i] > back_mediumwindow_capacity[i]:
        failed_backwindows[i] = 0
front_rand = np.random.rand(3)
back_rand = np.random.rand(4)
for i in range(len(failed_frontwindows)):
    if front_rand[i] < prob_front:
        failed_frontwindows[i] = 0
for i in range(len(failed_backwindows)):
    if back_rand[i] < prob_back:
        failed_backwindows[i] = 0


for i in range(len(sheath_loads)):
    if sheath_loads[i]>sheath_capacity[i]:
        sheath_loads[i] = 0
        if sheath_loads[i] != 0:
            sheath_loads[i] = sheath_loads[i]-10
    
left_end_truss = (sheath_loads[0]*4+sheath_loads[8]*4+sheath_loads[16]*4+sheath_loads[24]*4+sheath_loads[32]*4+sheath_loads[40]*4+sheath_loads[48]*4+sheath_loads[56]*4+sheath_loads[64]*4+sheath_loads[72]*4+sheath_loads[80]*4+sheath_loads[88]*4)/8
right_end_truss = (sheath_loads[7]*4+sheath_loads[15]*4+sheath_loads[23]*4+sheath_loads[31]*4+sheath_loads[39]*4+sheath_loads[47]*4+sheath_loads[55]*4+sheath_loads[63]*4+sheath_loads[71]*4+sheath_loads[79]*4+sheath_loads[87]*4+sheath_loads[95]*4)/8
bottom_1 = ((sheath_loads[0]+sheath_loads[0])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[8]+sheath_loads[8])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[16]+sheath_loads[16])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[24]+sheath_loads[24])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[32]+sheath_loads[32])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[40]+sheath_loads[40])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[48]+sheath_loads[48])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[56]+sheath_loads[56])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[64]+sheath_loads[64])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[72]+sheath_loads[72])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[80]+sheath_loads[80])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[88]+sheath_loads[88])*(math.cos(math.radians(22.62))*46)*4)/44
top_1 = ((sheath_loads[0]+sheath_loads[0])*4+
         (sheath_loads[8]+sheath_loads[8])*4+
         (sheath_loads[16]+sheath_loads[16])*4+
         (sheath_loads[24]+sheath_loads[24])*4+
         (sheath_loads[32]+sheath_loads[32])*4+
         (sheath_loads[40]+sheath_loads[40])*4+
         (sheath_loads[48]+sheath_loads[48])*4+
         (sheath_loads[56]+sheath_loads[56])*4+
         (sheath_loads[64]+sheath_loads[64])*4+
         (sheath_loads[72]+sheath_loads[72])*4+
         (sheath_loads[80]+sheath_loads[80])*4+
         (sheath_loads[88]+sheath_loads[88])*4)-bottom_1

bottom_2 = ((sheath_loads[0]+sheath_loads[1])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[8]+sheath_loads[8])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[16]+sheath_loads[17])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[24]+sheath_loads[24])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[32]+sheath_loads[33])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[40]+sheath_loads[40])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[48]+sheath_loads[49])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[56]+sheath_loads[56])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[64]+sheath_loads[65])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[72]+sheath_loads[72])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[80]+sheath_loads[81])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[88]+sheath_loads[88])*(math.cos(math.radians(22.62))*46)*4)/44
top_2 = ((sheath_loads[0]+sheath_loads[1])*4+
         (sheath_loads[8]+sheath_loads[8])*4+
         (sheath_loads[16]+sheath_loads[17])*4+
         (sheath_loads[24]+sheath_loads[24])*4+
         (sheath_loads[32]+sheath_loads[33])*4+
         (sheath_loads[40]+sheath_loads[40])*4+
         (sheath_loads[48]+sheath_loads[49])*4+
         (sheath_loads[56]+sheath_loads[56])*4+
         (sheath_loads[64]+sheath_loads[65])*4+
         (sheath_loads[72]+sheath_loads[72])*4+
         (sheath_loads[80]+sheath_loads[81])*4+
         (sheath_loads[88]+sheath_loads[88])*4)-bottom_2     

bottom_3 = ((sheath_loads[1]+sheath_loads[1])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[8]+sheath_loads[8])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[17]+sheath_loads[17])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[24]+sheath_loads[24])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[33]+sheath_loads[33])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[40]+sheath_loads[40])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[49]+sheath_loads[49])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[56]+sheath_loads[56])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[65]+sheath_loads[65])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[72]+sheath_loads[72])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[81]+sheath_loads[81])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[88]+sheath_loads[88])*(math.cos(math.radians(22.62))*46)*4)/44
top_3 = ((sheath_loads[1]+sheath_loads[1])*4+
         (sheath_loads[8]+sheath_loads[8])*4+
         (sheath_loads[17]+sheath_loads[17])*4+
         (sheath_loads[24]+sheath_loads[24])*4+
         (sheath_loads[33]+sheath_loads[33])*4+
         (sheath_loads[40]+sheath_loads[40])*4+
         (sheath_loads[49]+sheath_loads[49])*4+
         (sheath_loads[56]+sheath_loads[56])*4+
         (sheath_loads[65]+sheath_loads[65])*4+
         (sheath_loads[72]+sheath_loads[72])*4+
         (sheath_loads[81]+sheath_loads[81])*4+
         (sheath_loads[88]+sheath_loads[88])*4)-bottom_3     

bottom_4 = ((sheath_loads[1]+sheath_loads[1])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[8]+sheath_loads[9])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[17]+sheath_loads[17])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[24]+sheath_loads[25])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[33]+sheath_loads[33])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[40]+sheath_loads[41])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[49]+sheath_loads[49])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[56]+sheath_loads[57])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[65]+sheath_loads[65])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[72]+sheath_loads[73])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[81]+sheath_loads[81])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[88]+sheath_loads[89])*(math.cos(math.radians(22.62))*46)*4)/44
top_4 = ((sheath_loads[1]+sheath_loads[1])*4+
         (sheath_loads[8]+sheath_loads[9])*4+
         (sheath_loads[17]+sheath_loads[17])*4+
         (sheath_loads[24]+sheath_loads[25])*4+
         (sheath_loads[33]+sheath_loads[33])*4+
         (sheath_loads[40]+sheath_loads[41])*4+
         (sheath_loads[49]+sheath_loads[49])*4+
         (sheath_loads[56]+sheath_loads[57])*4+
         (sheath_loads[65]+sheath_loads[65])*4+
         (sheath_loads[72]+sheath_loads[73])*4+
         (sheath_loads[81]+sheath_loads[81])*4+
         (sheath_loads[88]+sheath_loads[89])*4)-bottom_4  

bottom_5 = ((sheath_loads[1]+sheath_loads[1])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[9]+sheath_loads[9])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[17]+sheath_loads[17])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[25]+sheath_loads[25])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[33]+sheath_loads[33])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[41]+sheath_loads[41])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[49]+sheath_loads[49])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[57]+sheath_loads[57])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[65]+sheath_loads[65])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[73]+sheath_loads[73])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[81]+sheath_loads[81])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[89]+sheath_loads[89])*(math.cos(math.radians(22.62))*46)*4)/44
top_5 = ((sheath_loads[1]+sheath_loads[1])*4+
         (sheath_loads[9]+sheath_loads[9])*4+
         (sheath_loads[17]+sheath_loads[17])*4+
         (sheath_loads[25]+sheath_loads[25])*4+
         (sheath_loads[33]+sheath_loads[33])*4+
         (sheath_loads[41]+sheath_loads[41])*4+
         (sheath_loads[49]+sheath_loads[49])*4+
         (sheath_loads[57]+sheath_loads[57])*4+
         (sheath_loads[65]+sheath_loads[65])*4+
         (sheath_loads[73]+sheath_loads[73])*4+
         (sheath_loads[81]+sheath_loads[81])*4+
         (sheath_loads[89]+sheath_loads[89])*4)-bottom_5 

bottom_6 = ((sheath_loads[1]+sheath_loads[2])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[9]+sheath_loads[9])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[17]+sheath_loads[18])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[25]+sheath_loads[25])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[33]+sheath_loads[34])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[41]+sheath_loads[41])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[49]+sheath_loads[50])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[57]+sheath_loads[57])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[65]+sheath_loads[66])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[73]+sheath_loads[73])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[81]+sheath_loads[82])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[89]+sheath_loads[89])*(math.cos(math.radians(22.62))*46)*4)/44
top_6 = ((sheath_loads[1]+sheath_loads[2])*4+
         (sheath_loads[9]+sheath_loads[9])*4+
         (sheath_loads[17]+sheath_loads[18])*4+
         (sheath_loads[25]+sheath_loads[25])*4+
         (sheath_loads[33]+sheath_loads[34])*4+
         (sheath_loads[41]+sheath_loads[41])*4+
         (sheath_loads[49]+sheath_loads[50])*4+
         (sheath_loads[57]+sheath_loads[57])*4+
         (sheath_loads[65]+sheath_loads[66])*4+
         (sheath_loads[73]+sheath_loads[73])*4+
         (sheath_loads[81]+sheath_loads[82])*4+
         (sheath_loads[89]+sheath_loads[89])*4)-bottom_6 

bottom_7 = ((sheath_loads[2]+sheath_loads[2])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[9]+sheath_loads[9])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[18]+sheath_loads[18])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[25]+sheath_loads[25])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[34]+sheath_loads[34])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[41]+sheath_loads[41])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[50]+sheath_loads[50])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[57]+sheath_loads[57])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[66]+sheath_loads[66])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[73]+sheath_loads[73])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[82]+sheath_loads[82])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[89]+sheath_loads[89])*(math.cos(math.radians(22.62))*46)*4)/44
top_7 = ((sheath_loads[2]+sheath_loads[2])*4+
         (sheath_loads[9]+sheath_loads[9])*4+
         (sheath_loads[18]+sheath_loads[18])*4+
         (sheath_loads[25]+sheath_loads[25])*4+
         (sheath_loads[35]+sheath_loads[34])*4+
         (sheath_loads[41]+sheath_loads[41])*4+
         (sheath_loads[50]+sheath_loads[50])*4+
         (sheath_loads[57]+sheath_loads[57])*4+
         (sheath_loads[66]+sheath_loads[66])*4+
         (sheath_loads[73]+sheath_loads[73])*4+
         (sheath_loads[82]+sheath_loads[82])*4+
         (sheath_loads[89]+sheath_loads[89])*4)-bottom_7 

bottom_8 = ((sheath_loads[2]+sheath_loads[2])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[9]+sheath_loads[10])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[18]+sheath_loads[18])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[25]+sheath_loads[26])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[34]+sheath_loads[34])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[41]+sheath_loads[42])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[50]+sheath_loads[50])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[57]+sheath_loads[58])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[66]+sheath_loads[66])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[73]+sheath_loads[74])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[82]+sheath_loads[82])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[89]+sheath_loads[90])*(math.cos(math.radians(22.62))*46)*4)/44
top_8 = ((sheath_loads[2]+sheath_loads[2])*4+
         (sheath_loads[9]+sheath_loads[10])*4+
         (sheath_loads[18]+sheath_loads[18])*4+
         (sheath_loads[25]+sheath_loads[26])*4+
         (sheath_loads[35]+sheath_loads[34])*4+
         (sheath_loads[41]+sheath_loads[42])*4+
         (sheath_loads[50]+sheath_loads[50])*4+
         (sheath_loads[57]+sheath_loads[58])*4+
         (sheath_loads[66]+sheath_loads[66])*4+
         (sheath_loads[73]+sheath_loads[74])*4+
         (sheath_loads[82]+sheath_loads[82])*4+
         (sheath_loads[89]+sheath_loads[90])*4)-bottom_8 

bottom_9 = ((sheath_loads[2]+sheath_loads[2])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[10]+sheath_loads[10])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[18]+sheath_loads[18])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[26]+sheath_loads[26])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[34]+sheath_loads[34])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[42]+sheath_loads[42])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[50]+sheath_loads[50])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[58]+sheath_loads[58])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[66]+sheath_loads[66])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[74]+sheath_loads[74])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[82]+sheath_loads[82])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[90]+sheath_loads[90])*(math.cos(math.radians(22.62))*46)*4)/44
top_9 = ((sheath_loads[2]+sheath_loads[2])*4+
         (sheath_loads[10]+sheath_loads[10])*4+
         (sheath_loads[18]+sheath_loads[18])*4+
         (sheath_loads[26]+sheath_loads[26])*4+
         (sheath_loads[35]+sheath_loads[34])*4+
         (sheath_loads[42]+sheath_loads[42])*4+
         (sheath_loads[50]+sheath_loads[50])*4+
         (sheath_loads[58]+sheath_loads[58])*4+
         (sheath_loads[66]+sheath_loads[66])*4+
         (sheath_loads[74]+sheath_loads[74])*4+
         (sheath_loads[82]+sheath_loads[82])*4+
         (sheath_loads[90]+sheath_loads[90])*4)-bottom_9 

bottom_10 = ((sheath_loads[2]+sheath_loads[3])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[10]+sheath_loads[10])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[18]+sheath_loads[19])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[26]+sheath_loads[26])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[34]+sheath_loads[35])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[42]+sheath_loads[42])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[50]+sheath_loads[51])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[58]+sheath_loads[58])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[66]+sheath_loads[67])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[74]+sheath_loads[74])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[82]+sheath_loads[83])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[90]+sheath_loads[90])*(math.cos(math.radians(22.62))*46)*4)/44
top_10 = ((sheath_loads[2]+sheath_loads[3])*4+
         (sheath_loads[10]+sheath_loads[10])*4+
         (sheath_loads[18]+sheath_loads[19])*4+
         (sheath_loads[26]+sheath_loads[26])*4+
         (sheath_loads[34]+sheath_loads[35])*4+
         (sheath_loads[42]+sheath_loads[42])*4+
         (sheath_loads[50]+sheath_loads[51])*4+
         (sheath_loads[58]+sheath_loads[58])*4+
         (sheath_loads[66]+sheath_loads[67])*4+
         (sheath_loads[74]+sheath_loads[74])*4+
         (sheath_loads[82]+sheath_loads[83])*4+
         (sheath_loads[90]+sheath_loads[90])*4)-bottom_10 

bottom_11 = ((sheath_loads[3]+sheath_loads[3])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[10]+sheath_loads[10])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[19]+sheath_loads[19])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[26]+sheath_loads[26])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[35]+sheath_loads[35])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[42]+sheath_loads[42])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[51]+sheath_loads[51])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[58]+sheath_loads[58])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[67]+sheath_loads[67])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[74]+sheath_loads[74])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[83]+sheath_loads[83])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[90]+sheath_loads[90])*(math.cos(math.radians(22.62))*46)*4)/44
top_11 = ((sheath_loads[3]+sheath_loads[3])*4+
         (sheath_loads[10]+sheath_loads[10])*4+
         (sheath_loads[19]+sheath_loads[19])*4+
         (sheath_loads[26]+sheath_loads[26])*4+
         (sheath_loads[35]+sheath_loads[35])*4+
         (sheath_loads[42]+sheath_loads[42])*4+
         (sheath_loads[51]+sheath_loads[51])*4+
         (sheath_loads[58]+sheath_loads[58])*4+
         (sheath_loads[67]+sheath_loads[67])*4+
         (sheath_loads[74]+sheath_loads[74])*4+
         (sheath_loads[83]+sheath_loads[83])*4+
         (sheath_loads[90]+sheath_loads[90])*4)-bottom_11 

bottom_12 = ((sheath_loads[3]+sheath_loads[3])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[10]+sheath_loads[11])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[19]+sheath_loads[19])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[26]+sheath_loads[27])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[35]+sheath_loads[35])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[42]+sheath_loads[43])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[51]+sheath_loads[51])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[58]+sheath_loads[59])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[67]+sheath_loads[67])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[74]+sheath_loads[75])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[83]+sheath_loads[83])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[90]+sheath_loads[91])*(math.cos(math.radians(22.62))*46)*4)/44
top_12 = ((sheath_loads[3]+sheath_loads[3])*4+
         (sheath_loads[10]+sheath_loads[11])*4+
         (sheath_loads[19]+sheath_loads[19])*4+
         (sheath_loads[26]+sheath_loads[27])*4+
         (sheath_loads[35]+sheath_loads[35])*4+
         (sheath_loads[42]+sheath_loads[43])*4+
         (sheath_loads[51]+sheath_loads[51])*4+
         (sheath_loads[58]+sheath_loads[59])*4+
         (sheath_loads[67]+sheath_loads[67])*4+
         (sheath_loads[74]+sheath_loads[75])*4+
         (sheath_loads[83]+sheath_loads[83])*4+
         (sheath_loads[90]+sheath_loads[91])*4)-bottom_12 

bottom_13 = ((sheath_loads[3]+sheath_loads[3])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[11]+sheath_loads[11])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[19]+sheath_loads[19])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[27]+sheath_loads[27])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[35]+sheath_loads[35])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[43]+sheath_loads[43])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[51]+sheath_loads[51])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[59]+sheath_loads[59])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[67]+sheath_loads[67])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[75]+sheath_loads[75])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[83]+sheath_loads[83])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[91]+sheath_loads[91])*(math.cos(math.radians(22.62))*46)*4)/44
top_13 = ((sheath_loads[3]+sheath_loads[3])*4+
         (sheath_loads[11]+sheath_loads[11])*4+
         (sheath_loads[19]+sheath_loads[19])*4+
         (sheath_loads[27]+sheath_loads[27])*4+
         (sheath_loads[35]+sheath_loads[35])*4+
         (sheath_loads[43]+sheath_loads[43])*4+
         (sheath_loads[51]+sheath_loads[51])*4+
         (sheath_loads[59]+sheath_loads[59])*4+
         (sheath_loads[67]+sheath_loads[67])*4+
         (sheath_loads[75]+sheath_loads[75])*4+
         (sheath_loads[83]+sheath_loads[83])*4+
         (sheath_loads[91]+sheath_loads[91])*4)-bottom_13 

bottom_14 = ((sheath_loads[3]+sheath_loads[4])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[11]+sheath_loads[11])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[19]+sheath_loads[20])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[27]+sheath_loads[27])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[35]+sheath_loads[36])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[43]+sheath_loads[43])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[51]+sheath_loads[52])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[59]+sheath_loads[59])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[67]+sheath_loads[68])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[75]+sheath_loads[75])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[83]+sheath_loads[84])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[91]+sheath_loads[91])*(math.cos(math.radians(22.62))*46)*4)/44
top_14 = ((sheath_loads[3]+sheath_loads[4])*4+
         (sheath_loads[11]+sheath_loads[11])*4+
         (sheath_loads[19]+sheath_loads[20])*4+
         (sheath_loads[27]+sheath_loads[27])*4+
         (sheath_loads[35]+sheath_loads[36])*4+
         (sheath_loads[43]+sheath_loads[43])*4+
         (sheath_loads[51]+sheath_loads[52])*4+
         (sheath_loads[59]+sheath_loads[59])*4+
         (sheath_loads[67]+sheath_loads[68])*4+
         (sheath_loads[75]+sheath_loads[75])*4+
         (sheath_loads[83]+sheath_loads[84])*4+
         (sheath_loads[91]+sheath_loads[91])*4)-bottom_14 

bottom_15 = ((sheath_loads[4]+sheath_loads[4])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[11]+sheath_loads[11])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[20]+sheath_loads[20])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[27]+sheath_loads[27])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[36]+sheath_loads[36])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[43]+sheath_loads[43])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[52]+sheath_loads[52])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[59]+sheath_loads[59])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[68]+sheath_loads[68])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[75]+sheath_loads[75])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[84]+sheath_loads[84])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[91]+sheath_loads[91])*(math.cos(math.radians(22.62))*46)*4)/44
top_15 = ((sheath_loads[4]+sheath_loads[4])*4+
         (sheath_loads[11]+sheath_loads[11])*4+
         (sheath_loads[20]+sheath_loads[20])*4+
         (sheath_loads[27]+sheath_loads[27])*4+
         (sheath_loads[36]+sheath_loads[36])*4+
         (sheath_loads[43]+sheath_loads[43])*4+
         (sheath_loads[52]+sheath_loads[52])*4+
         (sheath_loads[59]+sheath_loads[59])*4+
         (sheath_loads[68]+sheath_loads[68])*4+
         (sheath_loads[75]+sheath_loads[75])*4+
         (sheath_loads[84]+sheath_loads[84])*4+
         (sheath_loads[91]+sheath_loads[91])*4)-bottom_15 

bottom_16 = ((sheath_loads[4]+sheath_loads[4])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[11]+sheath_loads[12])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[20]+sheath_loads[20])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[27]+sheath_loads[28])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[36]+sheath_loads[36])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[43]+sheath_loads[44])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[52]+sheath_loads[52])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[59]+sheath_loads[60])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[68]+sheath_loads[68])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[75]+sheath_loads[76])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[84]+sheath_loads[84])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[91]+sheath_loads[92])*(math.cos(math.radians(22.62))*46)*4)/44
top_16 = ((sheath_loads[4]+sheath_loads[4])*4+
         (sheath_loads[11]+sheath_loads[12])*4+
         (sheath_loads[20]+sheath_loads[20])*4+
         (sheath_loads[27]+sheath_loads[28])*4+
         (sheath_loads[36]+sheath_loads[36])*4+
         (sheath_loads[43]+sheath_loads[44])*4+
         (sheath_loads[52]+sheath_loads[52])*4+
         (sheath_loads[59]+sheath_loads[60])*4+
         (sheath_loads[68]+sheath_loads[68])*4+
         (sheath_loads[75]+sheath_loads[76])*4+
         (sheath_loads[84]+sheath_loads[84])*4+
         (sheath_loads[91]+sheath_loads[92])*4)-bottom_16 

bottom_17 = ((sheath_loads[4]+sheath_loads[4])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[12]+sheath_loads[12])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[20]+sheath_loads[20])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[28]+sheath_loads[28])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[36]+sheath_loads[36])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[44]+sheath_loads[44])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[52]+sheath_loads[52])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[60]+sheath_loads[60])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[68]+sheath_loads[68])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[76]+sheath_loads[76])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[84]+sheath_loads[84])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[92]+sheath_loads[92])*(math.cos(math.radians(22.62))*46)*4)/44
top_17 = ((sheath_loads[4]+sheath_loads[4])*4+
         (sheath_loads[12]+sheath_loads[12])*4+
         (sheath_loads[20]+sheath_loads[20])*4+
         (sheath_loads[28]+sheath_loads[28])*4+
         (sheath_loads[36]+sheath_loads[36])*4+
         (sheath_loads[44]+sheath_loads[44])*4+
         (sheath_loads[52]+sheath_loads[52])*4+
         (sheath_loads[60]+sheath_loads[60])*4+
         (sheath_loads[68]+sheath_loads[68])*4+
         (sheath_loads[76]+sheath_loads[76])*4+
         (sheath_loads[84]+sheath_loads[84])*4+
         (sheath_loads[92]+sheath_loads[92])*4)-bottom_17 

bottom_18 = ((sheath_loads[4]+sheath_loads[5])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[12]+sheath_loads[12])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[20]+sheath_loads[21])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[28]+sheath_loads[28])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[36]+sheath_loads[37])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[44]+sheath_loads[44])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[52]+sheath_loads[53])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[60]+sheath_loads[60])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[68]+sheath_loads[69])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[76]+sheath_loads[76])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[84]+sheath_loads[85])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[92]+sheath_loads[92])*(math.cos(math.radians(22.62))*46)*4)/44
top_18 = ((sheath_loads[4]+sheath_loads[5])*4+
         (sheath_loads[12]+sheath_loads[12])*4+
         (sheath_loads[20]+sheath_loads[21])*4+
         (sheath_loads[28]+sheath_loads[28])*4+
         (sheath_loads[36]+sheath_loads[37])*4+
         (sheath_loads[44]+sheath_loads[44])*4+
         (sheath_loads[52]+sheath_loads[53])*4+
         (sheath_loads[60]+sheath_loads[60])*4+
         (sheath_loads[68]+sheath_loads[69])*4+
         (sheath_loads[76]+sheath_loads[76])*4+
         (sheath_loads[84]+sheath_loads[85])*4+
         (sheath_loads[92]+sheath_loads[92])*4)-bottom_18 

bottom_19 = ((sheath_loads[5]+sheath_loads[5])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[12]+sheath_loads[12])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[21]+sheath_loads[21])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[28]+sheath_loads[28])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[37]+sheath_loads[37])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[44]+sheath_loads[44])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[53]+sheath_loads[53])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[60]+sheath_loads[60])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[69]+sheath_loads[69])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[76]+sheath_loads[76])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[85]+sheath_loads[85])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[92]+sheath_loads[92])*(math.cos(math.radians(22.62))*46)*4)/44
top_19 = ((sheath_loads[5]+sheath_loads[5])*4+
         (sheath_loads[12]+sheath_loads[12])*4+
         (sheath_loads[21]+sheath_loads[21])*4+
         (sheath_loads[28]+sheath_loads[28])*4+
         (sheath_loads[37]+sheath_loads[37])*4+
         (sheath_loads[44]+sheath_loads[44])*4+
         (sheath_loads[53]+sheath_loads[53])*4+
         (sheath_loads[60]+sheath_loads[60])*4+
         (sheath_loads[69]+sheath_loads[69])*4+
         (sheath_loads[76]+sheath_loads[76])*4+
         (sheath_loads[85]+sheath_loads[85])*4+
         (sheath_loads[92]+sheath_loads[92])*4)-bottom_19 

bottom_20 = ((sheath_loads[5]+sheath_loads[5])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[12]+sheath_loads[13])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[21]+sheath_loads[21])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[28]+sheath_loads[29])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[37]+sheath_loads[37])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[44]+sheath_loads[45])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[53]+sheath_loads[53])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[60]+sheath_loads[61])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[69]+sheath_loads[69])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[76]+sheath_loads[77])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[85]+sheath_loads[85])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[92]+sheath_loads[93])*(math.cos(math.radians(22.62))*46)*4)/44
top_20 = ((sheath_loads[5]+sheath_loads[5])*4+
         (sheath_loads[12]+sheath_loads[13])*4+
         (sheath_loads[21]+sheath_loads[21])*4+
         (sheath_loads[28]+sheath_loads[29])*4+
         (sheath_loads[37]+sheath_loads[37])*4+
         (sheath_loads[44]+sheath_loads[45])*4+
         (sheath_loads[53]+sheath_loads[53])*4+
         (sheath_loads[60]+sheath_loads[61])*4+
         (sheath_loads[69]+sheath_loads[69])*4+
         (sheath_loads[76]+sheath_loads[77])*4+
         (sheath_loads[85]+sheath_loads[85])*4+
         (sheath_loads[92]+sheath_loads[93])*4)-bottom_20

bottom_21 = ((sheath_loads[5]+sheath_loads[5])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[13]+sheath_loads[13])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[21]+sheath_loads[21])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[29]+sheath_loads[29])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[37]+sheath_loads[37])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[45]+sheath_loads[45])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[53]+sheath_loads[53])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[61]+sheath_loads[61])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[69]+sheath_loads[69])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[77]+sheath_loads[77])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[85]+sheath_loads[85])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[93]+sheath_loads[93])*(math.cos(math.radians(22.62))*46)*4)/44
top_21 = ((sheath_loads[5]+sheath_loads[5])*4+
         (sheath_loads[13]+sheath_loads[13])*4+
         (sheath_loads[21]+sheath_loads[21])*4+
         (sheath_loads[29]+sheath_loads[29])*4+
         (sheath_loads[37]+sheath_loads[37])*4+
         (sheath_loads[45]+sheath_loads[45])*4+
         (sheath_loads[53]+sheath_loads[53])*4+
         (sheath_loads[61]+sheath_loads[61])*4+
         (sheath_loads[69]+sheath_loads[69])*4+
         (sheath_loads[77]+sheath_loads[77])*4+
         (sheath_loads[85]+sheath_loads[85])*4+
         (sheath_loads[93]+sheath_loads[93])*4)-bottom_21

bottom_22 = ((sheath_loads[5]+sheath_loads[6])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[13]+sheath_loads[13])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[21]+sheath_loads[22])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[29]+sheath_loads[29])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[37]+sheath_loads[38])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[45]+sheath_loads[45])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[53]+sheath_loads[54])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[61]+sheath_loads[61])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[69]+sheath_loads[70])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[77]+sheath_loads[77])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[85]+sheath_loads[86])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[93]+sheath_loads[93])*(math.cos(math.radians(22.62))*46)*4)/44
top_22 = ((sheath_loads[5]+sheath_loads[6])*4+
         (sheath_loads[13]+sheath_loads[13])*4+
         (sheath_loads[21]+sheath_loads[22])*4+
         (sheath_loads[29]+sheath_loads[29])*4+
         (sheath_loads[37]+sheath_loads[38])*4+
         (sheath_loads[45]+sheath_loads[45])*4+
         (sheath_loads[53]+sheath_loads[54])*4+
         (sheath_loads[61]+sheath_loads[61])*4+
         (sheath_loads[69]+sheath_loads[70])*4+
         (sheath_loads[77]+sheath_loads[77])*4+
         (sheath_loads[85]+sheath_loads[86])*4+
         (sheath_loads[93]+sheath_loads[93])*4)-bottom_22

bottom_23 = ((sheath_loads[6]+sheath_loads[6])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[13]+sheath_loads[13])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[22]+sheath_loads[22])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[29]+sheath_loads[29])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[38]+sheath_loads[38])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[45]+sheath_loads[45])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[54]+sheath_loads[54])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[61]+sheath_loads[61])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[70]+sheath_loads[70])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[77]+sheath_loads[77])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[86]+sheath_loads[86])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[93]+sheath_loads[93])*(math.cos(math.radians(22.62))*46)*4)/44
top_23 = ((sheath_loads[6]+sheath_loads[6])*4+
         (sheath_loads[13]+sheath_loads[13])*4+
         (sheath_loads[22]+sheath_loads[22])*4+
         (sheath_loads[29]+sheath_loads[29])*4+
         (sheath_loads[38]+sheath_loads[38])*4+
         (sheath_loads[45]+sheath_loads[45])*4+
         (sheath_loads[54]+sheath_loads[54])*4+
         (sheath_loads[61]+sheath_loads[61])*4+
         (sheath_loads[70]+sheath_loads[70])*4+
         (sheath_loads[77]+sheath_loads[77])*4+
         (sheath_loads[86]+sheath_loads[86])*4+
         (sheath_loads[93]+sheath_loads[93])*4)-bottom_23

bottom_24 = ((sheath_loads[6]+sheath_loads[6])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[13]+sheath_loads[14])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[22]+sheath_loads[22])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[29]+sheath_loads[30])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[38]+sheath_loads[38])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[45]+sheath_loads[46])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[54]+sheath_loads[54])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[61]+sheath_loads[62])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[70]+sheath_loads[70])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[77]+sheath_loads[78])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[86]+sheath_loads[86])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[93]+sheath_loads[94])*(math.cos(math.radians(22.62))*46)*4)/44
top_24 = ((sheath_loads[6]+sheath_loads[6])*4+
         (sheath_loads[13]+sheath_loads[14])*4+
         (sheath_loads[22]+sheath_loads[22])*4+
         (sheath_loads[29]+sheath_loads[30])*4+
         (sheath_loads[38]+sheath_loads[38])*4+
         (sheath_loads[45]+sheath_loads[46])*4+
         (sheath_loads[54]+sheath_loads[54])*4+
         (sheath_loads[61]+sheath_loads[62])*4+
         (sheath_loads[70]+sheath_loads[70])*4+
         (sheath_loads[77]+sheath_loads[78])*4+
         (sheath_loads[86]+sheath_loads[86])*4+
         (sheath_loads[93]+sheath_loads[94])*4)-bottom_24

bottom_25 = ((sheath_loads[6]+sheath_loads[6])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[14]+sheath_loads[14])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[22]+sheath_loads[22])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[30]+sheath_loads[30])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[38]+sheath_loads[38])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[46]+sheath_loads[46])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[54]+sheath_loads[54])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[62]+sheath_loads[62])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[70]+sheath_loads[70])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[78]+sheath_loads[78])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[86]+sheath_loads[86])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[94]+sheath_loads[94])*(math.cos(math.radians(22.62))*46)*4)/44
top_25 = ((sheath_loads[6]+sheath_loads[6])*4+
         (sheath_loads[14]+sheath_loads[14])*4+
         (sheath_loads[22]+sheath_loads[22])*4+
         (sheath_loads[30]+sheath_loads[30])*4+
         (sheath_loads[38]+sheath_loads[38])*4+
         (sheath_loads[46]+sheath_loads[46])*4+
         (sheath_loads[54]+sheath_loads[54])*4+
         (sheath_loads[62]+sheath_loads[62])*4+
         (sheath_loads[70]+sheath_loads[70])*4+
         (sheath_loads[78]+sheath_loads[78])*4+
         (sheath_loads[86]+sheath_loads[86])*4+
         (sheath_loads[94]+sheath_loads[94])*4)-bottom_25

bottom_26 = ((sheath_loads[6]+sheath_loads[7])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[14]+sheath_loads[14])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[22]+sheath_loads[23])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[30]+sheath_loads[30])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[38]+sheath_loads[39])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[46]+sheath_loads[46])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[54]+sheath_loads[55])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[62]+sheath_loads[62])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[70]+sheath_loads[71])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[78]+sheath_loads[78])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[86]+sheath_loads[87])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[94]+sheath_loads[94])*(math.cos(math.radians(22.62))*46)*4)/44
top_26 = ((sheath_loads[6]+sheath_loads[7])*4+
         (sheath_loads[14]+sheath_loads[14])*4+
         (sheath_loads[22]+sheath_loads[23])*4+
         (sheath_loads[30]+sheath_loads[30])*4+
         (sheath_loads[38]+sheath_loads[39])*4+
         (sheath_loads[46]+sheath_loads[46])*4+
         (sheath_loads[54]+sheath_loads[55])*4+
         (sheath_loads[62]+sheath_loads[62])*4+
         (sheath_loads[70]+sheath_loads[71])*4+
         (sheath_loads[78]+sheath_loads[78])*4+
         (sheath_loads[86]+sheath_loads[87])*4+
         (sheath_loads[94]+sheath_loads[94])*4)-bottom_26

bottom_27 = ((sheath_loads[7]+sheath_loads[7])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[14]+sheath_loads[14])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[23]+sheath_loads[23])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[30]+sheath_loads[30])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[39]+sheath_loads[39])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[46]+sheath_loads[46])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[55]+sheath_loads[55])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[62]+sheath_loads[62])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[71]+sheath_loads[71])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[78]+sheath_loads[78])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[87]+sheath_loads[87])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[94]+sheath_loads[94])*(math.cos(math.radians(22.62))*46)*4)/44
top_27 = ((sheath_loads[7]+sheath_loads[7])*4+
         (sheath_loads[14]+sheath_loads[14])*4+
         (sheath_loads[23]+sheath_loads[23])*4+
         (sheath_loads[30]+sheath_loads[30])*4+
         (sheath_loads[39]+sheath_loads[39])*4+
         (sheath_loads[46]+sheath_loads[46])*4+
         (sheath_loads[55]+sheath_loads[55])*4+
         (sheath_loads[62]+sheath_loads[62])*4+
         (sheath_loads[71]+sheath_loads[71])*4+
         (sheath_loads[78]+sheath_loads[78])*4+
         (sheath_loads[87]+sheath_loads[87])*4+
         (sheath_loads[94]+sheath_loads[94])*4)-bottom_27

bottom_28 = ((sheath_loads[7]+sheath_loads[7])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[14]+sheath_loads[15])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[23]+sheath_loads[23])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[30]+sheath_loads[31])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[39]+sheath_loads[39])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[46]+sheath_loads[47])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[55]+sheath_loads[55])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[62]+sheath_loads[63])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[71]+sheath_loads[71])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[78]+sheath_loads[79])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[87]+sheath_loads[87])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[94]+sheath_loads[95])*(math.cos(math.radians(22.62))*46)*4)/44
top_28 = ((sheath_loads[7]+sheath_loads[7])*4+
         (sheath_loads[14]+sheath_loads[15])*4+
         (sheath_loads[23]+sheath_loads[23])*4+
         (sheath_loads[30]+sheath_loads[31])*4+
         (sheath_loads[39]+sheath_loads[39])*4+
         (sheath_loads[46]+sheath_loads[47])*4+
         (sheath_loads[55]+sheath_loads[55])*4+
         (sheath_loads[62]+sheath_loads[63])*4+
         (sheath_loads[71]+sheath_loads[71])*4+
         (sheath_loads[78]+sheath_loads[79])*4+
         (sheath_loads[87]+sheath_loads[87])*4+
         (sheath_loads[94]+sheath_loads[95])*4)-bottom_28

bottom_29 = ((sheath_loads[7]+sheath_loads[7])*(math.cos(math.radians(22.62))*2)*4+
            (sheath_loads[15]+sheath_loads[15])*(math.cos(math.radians(22.62))*6)*4+
            (sheath_loads[23]+sheath_loads[23])*(math.cos(math.radians(22.62))*10)*4+
            (sheath_loads[32]+sheath_loads[31])*(math.cos(math.radians(22.62))*14)*4+
            (sheath_loads[39]+sheath_loads[39])*(math.cos(math.radians(22.62))*18)*4+
            (sheath_loads[47]+sheath_loads[47])*(math.cos(math.radians(22.62))*22)*4+
            (sheath_loads[55]+sheath_loads[55])*(math.cos(math.radians(22.62))*26)*4+
            (sheath_loads[63]+sheath_loads[63])*(math.cos(math.radians(22.62))*30)*4+
            (sheath_loads[71]+sheath_loads[71])*(math.cos(math.radians(22.62))*34)*4+
            (sheath_loads[79]+sheath_loads[79])*(math.cos(math.radians(22.62))*38)*4+
            (sheath_loads[87]+sheath_loads[87])*(math.cos(math.radians(22.62))*42)*4+
            (sheath_loads[95]+sheath_loads[95])*(math.cos(math.radians(22.62))*46)*4)/44
top_29 = ((sheath_loads[7]+sheath_loads[7])*4+
         (sheath_loads[15]+sheath_loads[15])*4+
         (sheath_loads[23]+sheath_loads[23])*4+
         (sheath_loads[31]+sheath_loads[31])*4+
         (sheath_loads[39]+sheath_loads[39])*4+
         (sheath_loads[47]+sheath_loads[47])*4+
         (sheath_loads[55]+sheath_loads[55])*4+
         (sheath_loads[63]+sheath_loads[63])*4+
         (sheath_loads[71]+sheath_loads[71])*4+
         (sheath_loads[79]+sheath_loads[79])*4+
         (sheath_loads[87]+sheath_loads[87])*4+
         (sheath_loads[95]+sheath_loads[95])*4)-bottom_29

connection_loads = [left_end_truss, top_1, top_2, top_3, top_4, top_5, top_6, top_7, top_8, top_9, top_10, top_11,
                    top_12, top_13, top_14, top_15, top_16, top_17, top_18, top_19, top_20, top_21, top_22, top_23,
                    top_24, top_25, top_26, top_27, top_28, top_29, right_end_truss, right_end_truss, right_end_truss,
                    right_end_truss, right_end_truss, right_end_truss, right_end_truss, right_end_truss, bottom_29,
                    bottom_28, bottom_27, bottom_26, bottom_25, bottom_24, bottom_23, bottom_22, bottom_21, bottom_20,
                    bottom_19, bottom_18, bottom_17, bottom_16, bottom_15, bottom_14, bottom_13, bottom_12, bottom_11,
                    bottom_10, bottom_9, bottom_8, bottom_7, bottom_6, bottom_5, bottom_4, bottom_3, bottom_2, 
                    bottom_1, left_end_truss, left_end_truss, left_end_truss, left_end_truss, left_end_truss,
                    left_end_truss, left_end_truss]

failed_connections = np.full(74,1)
for i in range(len(failed_connections)):
    if connection_loads[i] > connection_capacities[i]:
        failed_connections[i] = 0
        connection_loads[i-1] = connection_loads[i-1] + (connection_loads[i]/2)
        connection_loads[i+1] = connection_loads[i+1] + (connection_loads[i]/2)
        connection_loads[i] = 0
        
zz = np.count_nonzero(failed_connections==0)
if zz != 0:
    zz_old = zz + 1
    while zz > zz_old:
        zz_old = zz
        for i in range(len(failed_connections)):
            if connection_loads[i] > connection_capacities[i]:
                failed_connections[i] = 0
                connection_loads[i-1] = connection_loads[i-1] + (connection_loads[i]/2)
                connection_loads[i+1] = connection_loads[i+1] + (connection_loads[i]/2)
                connection_loads[i] = 0
        zz = np.count_nonzero(failed_connections==0)

back_wall_connections = [failed_connections[1],failed_connections[2],failed_connections[3],failed_connections[4],failed_connections[5],
                     failed_connections[6],failed_connections[7],failed_connections[8],failed_connections[9],failed_connections[10],
                     failed_connections[11],failed_connections[12],failed_connections[13],failed_connections[14],failed_connections[15],
                     failed_connections[16],failed_connections[17],failed_connections[18],failed_connections[19],failed_connections[20],
                     failed_connections[21],failed_connections[22],failed_connections[23],failed_connections[24],failed_connections[25],    
                     failed_connections[26],failed_connections[27],failed_connections[28]]; 
front_wall_connections = [failed_connections[37],failed_connections[38],failed_connections[39],failed_connections[40],failed_connections[41],
                    failed_connections[42],failed_connections[43],failed_connections[44],failed_connections[45],failed_connections[46],
                    failed_connections[47],failed_connections[48],failed_connections[49],failed_connections[50],failed_connections[51],
                    failed_connections[52],failed_connections[53],failed_connections[54],failed_connections[55],failed_connections[56],
                    failed_connections[57],failed_connections[58],failed_connections[59],failed_connections[60],failed_connections[61],
                    failed_connections[62],failed_connections[63],failed_connections[64]]; 
right_wall_connections = [failed_connections[29],failed_connections[30],failed_connections[31],failed_connections[32],failed_connections[33],
                    failed_connections[34],failed_connections[35],failed_connections[36]];
left_wall_connections = [failed_connections[65],failed_connections[66],failed_connections[67],failed_connections[68],failed_connections[69],
                    failed_connections[70],failed_connections[71],failed_connections[0]];
back_fail_conn_count = np.count_nonzero(back_wall_connections==0)
front_fail_conn_count = np.count_nonzero(front_wall_connections==0)
right_fail_conn_count = np.count_nonzero(right_wall_connections==0)
left_fail_conn_count = np.count_nonzero(left_wall_connections==0)

## wall uplift
back_wall_uplift = (connection_loads[1]+connection_loads[2]+connection_loads[3]+connection_loads[4]+connection_loads[5]+
                     connection_loads[6]+connection_loads[7]+connection_loads[8]+connection_loads[9]+connection_loads[10]+
                     connection_loads[11]+connection_loads[12]+connection_loads[13]+connection_loads[14]+connection_loads[15]+
                     connection_loads[16]+connection_loads[17]+connection_loads[18]+connection_loads[19]+connection_loads[20]+
                     connection_loads[21]+connection_loads[22]+connection_loads[23]+connection_loads[24]+connection_loads[25]+    
                     connection_loads[26]+connection_loads[27]+connection_loads[28])/60; 
front_wall_uplift = (connection_loads[37]+connection_loads[38]+connection_loads[39]+connection_loads[40]+connection_loads[41]+
                    connection_loads[42]+connection_loads[43]+connection_loads[44]+connection_loads[45]+connection_loads[46]+
                    connection_loads[47]+connection_loads[48]+connection_loads[49]+connection_loads[50]+connection_loads[51]+
                    connection_loads[52]+connection_loads[53]+connection_loads[54]+connection_loads[55]+connection_loads[56]+
                    connection_loads[57]+connection_loads[58]+connection_loads[59]+connection_loads[60]+connection_loads[61]+    
                    connection_loads[62]+connection_loads[63]+connection_loads[64])/60; 
right_wall_uplift = (connection_loads[29]+connection_loads[30]+connection_loads[31]+connection_loads[32]+connection_loads[33]+
                    connection_loads[34]+connection_loads[35]+connection_loads[36])/44
left_wall_uplift = (connection_loads[65]+connection_loads[66]+connection_loads[67]+connection_loads[68]+connection_loads[69]+
                    connection_loads[70]+connection_loads[71]+connection_loads[0])/44

uplift_loads = [front_wall_uplift,left_wall_uplift,back_wall_uplift,right_wall_uplift]

## wall bending
if direction == 1:
    front_wall_bending = abs((p_windward_CC*10**2)/8)
    back_wall_bending = abs((p_leeward_CC*10**2)/8)
    left_wall_bending1 = abs((p_side_CC*19.167**2)/8)
    left_wall_bending2 = abs((p_sideleading_CC*11.833**2)/8)
    left_wall_bending = max(left_wall_bending1, left_wall_bending2)
    right_wall_bending = left_wall_bending
if direction == 2:
    front_wall_bending = abs((p_windward_CC*10**2)/8)
    back_wall_bending1 = abs((p_side_CC*10**2)/8)
    back_wall_bending2 = abs((p_sideleading_CC*10**2)/8)
    back_wall_bending = max(back_wall_bending1, back_wall_bending2)
    left_wall_bending = abs((p_windward_CC*19.167**2)/8)
    right_wall_bending1 = abs((p_side_CC*19.167**2)/8)
    right_wall_bending2 = abs((p_sideleading_CC*11.833**2)/8)
    right_wall_bending = max(right_wall_bending1, right_wall_bending2)
if direction == 3:
    front_wall_bending1 = abs((p_side_CC*10**2)/8)
    front_wall_bending2 = abs((p_sideleading_CC*10**2)/8)
    front_wall_bending = max(front_wall_bending1, front_wall_bending2)
    back_wall_bending = front_wall_bending
    left_wall_bending = abs((p_windward_CC*19.167**2)/8)
    right_wall_bending = abs((p_leeward_CC*19.167**2)/8)
if direction == 4:
    back_wall_bending = abs((p_windward_CC*10**2)/8)
    front_wall_bending1 = abs((p_side_CC*10**2)/8)
    front_wall_bending2 = abs((p_sideleading_CC*10**2)/8)
    front_wall_bending = max(front_wall_bending1, front_wall_bending2)
    left_wall_bending = abs((p_windward_CC*19.167**2)/8)
    right_wall_bending1 = abs((p_side_CC*19.167**2)/8)
    right_wall_bending2 = abs((p_sideleading_CC*11.833**2)/8)
    right_wall_bending = max(right_wall_bending1, right_wall_bending2)    
if direction == 5:
    back_wall_bending = abs((p_windward_CC*10**2)/8)
    front_wall_bending = abs((p_leeward_CC*10**2)/8)
    left_wall_bending1 = abs((p_side_CC*19.167**2)/8)
    left_wall_bending2 = abs((p_sideleading_CC*11.833**2)/8)
    left_wall_bending = max(left_wall_bending1, left_wall_bending2)
    right_wall_bending = left_wall_bending   
if direction == 6:
    back_wall_bending = abs((p_windward_CC*10**2)/8)
    front_wall_bending1 = abs((p_side_CC*10**2)/8)
    front_wall_bending2 = abs((p_sideleading_CC*10**2)/8)
    front_wall_bending = max(front_wall_bending1, front_wall_bending2)
    right_wall_bending = abs((p_windward_CC*19.167**2)/8)
    left_wall_bending1 = abs((p_side_CC*19.167**2)/8)
    left_wall_bending2 = abs((p_sideleading_CC*11.833**2)/8)
    left_wall_bending = max(left_wall_bending1, left_wall_bending2)     
if direction == 7:
    front_wall_bending1 = abs((p_side_CC*10**2)/8)
    front_wall_bending2 = abs((p_sideleading_CC*10**2)/8)
    front_wall_bending = max(front_wall_bending1, front_wall_bending2)
    back_wall_bending = front_wall_bending
    right_wall_bending = abs((p_windward_CC*19.167**2)/8)
    left_wall_bending = abs((p_leeward_CC*19.167**2)/8)    
if direction == 8:
    front_wall_bending = abs((p_windward_CC*10**2)/8)
    back_wall_bending1 = abs((p_side_CC*10**2)/8)
    back_wall_bending2 = abs((p_sideleading_CC*10**2)/8)
    back_wall_bending = max(back_wall_bending1, back_wall_bending2)
    right_wall_bending = abs((p_windward_CC*19.167**2)/8)
    left_wall_bending1 = abs((p_side_CC*19.167**2)/8)
    left_wall_bending2 = abs((p_sideleading_CC*11.833**2)/8)
    left_wall_bending = max(left_wall_bending1, left_wall_bending2)       

if back_fail_conn_count > 14:
    back_wall_bending = back_wall_bending*2.8
if front_fail_conn_count > 14:
    front_wall_bending = front_wall_bending*2.8
if right_fail_conn_count > 4:
    right_wall_bending = right_wall_bending*2.8
if left_fail_conn_count > 4:
    left_wall_bending = left_wall_bending*2.8
    
bending_loads = [front_wall_bending,left_wall_bending,back_wall_bending,right_wall_bending]

## lateral loads
if direction == 1:
    if front_fail_conn_count <= 14:
        front_lateral = p_windward_CC*3*30*10/2
    elif front_fail_conn_count > 14:
        front_lateral = p_windward_CC*0.5*30*10
        
    if left_fail_conn_count <= 4:
        left_lateral = (p_side_CC*3*22*14.583/2)-(p_side_CC*0.5*4.4*5.83)+(p_sideleading_CC*0.5*4.4*5.83)
    elif left_fail_conn_count > 4:
        left_lateral = (p_side_CC*0.5*22*14.583)-(p_side_CC*0.5*4.4*5.83)+(p_sideleading_CC*0.5*4.4*5.83)
        
    if back_fail_conn_count <= 14:
        back_lateral = p_leeward_CC*3*30*10/2
    elif back_fail_conn_count > 14:
        back_lateral = p_leeward_CC*0.5*30*10
        
    if right_fail_conn_count <= 4:
        right_lateral = (p_side_CC*3*22*14.583/2)-(p_side_CC*0.5*4.4*5.83)+(p_sideleading_CC*0.5*4.4*5.83)
    elif right_fail_conn_count > 4:
        right_lateral = (p_side_CC*0.5*22*14.583)-(p_side_CC*0.5*4.4*5.83)+(p_sideleading_CC*0.5*4.4*5.83)
if direction == 2:
    if front_fail_conn_count <= 14:
        front_lateral = p_windward_CC*3*30*10/2
    elif front_fail_conn_count > 14:
        front_lateral = p_windward_CC*0.5*30*10
        
    if left_fail_conn_count <= 4:
        left_lateral = p_windward_CC*3*22*14.583/2
    elif left_fail_conn_count > 4:
        left_lateral = p_windward_CC*0.5*22*14.583
        
    if back_fail_conn_count <= 14:
        back_lateral = (p_side_CC*3*30*10/2)-(p_side_CC*0.5*4.4*2.93)+(p_sideleading_CC*0.5*4.4*2.93)
    elif back_fail_conn_count > 14:
        back_lateral = (p_side_CC*0.5*30*10)-(p_side_CC*0.5*4.4*2.93)+(p_sideleading_CC*0.5*4.4*2.93)
    
    if right_fail_conn_count <= 4:
        right_lateral = (p_side_CC*3*22*14.583/2)-(p_side_CC*0.5*4.4*5.83)+(p_sideleading_CC*0.5*4.4*5.83)
    elif right_fail_conn_count > 4:
        right_lateral = (p_side_CC*0.5*22*14.583)-(p_side_CC*0.5*4.4*5.83)+(p_sideleading_CC*0.5*4.4*5.83)
if direction == 3:
    if front_fail_conn_count <= 14:
        front_lateral = (p_side_CC*3*30*10/2)-(p_side_CC*0.5*4.4*2.93)+(p_sideleading_CC*0.5*4.4*2.93)
    elif front_fail_conn_count > 14:
        front_lateral = (p_side_CC*0.5*30*10)-(p_side_CC*0.5*4.4*2.93)+(p_sideleading_CC*0.5*4.4*2.93)
        
    if left_fail_conn_count <= 4:
        left_lateral = p_windward_CC*3*22*14.583/2
    elif left_fail_conn_count > 4:
        left_lateral = p_windward_CC*0.5*22*14.583      
        
    if back_fail_conn_count <= 14:
        back_lateral = (p_side_CC*3*30*10/2)-(p_side_CC*0.5*4.4*2.93)+(p_sideleading_CC*0.5*4.4*2.93)
    elif back_fail_conn_count > 14:
        back_lateral = (p_side_CC*0.5*30*10)-(p_side_CC*0.5*4.4*2.93)+(p_sideleading_CC*0.5*4.4*2.93)   
        
    if right_fail_conn_count <= 4:
        right_lateral = p_leeward_CC*3*22*14.583/2
    elif right_fail_conn_count > 4:
        right_lateral = p_leeward_CC*0.5*22*14.583
if direction == 4:
    if front_fail_conn_count <= 14:
        front_lateral = (p_side_CC*3*30*10/2)-(p_side_CC*0.5*4.4*2.93)+(p_sideleading_CC*0.5*4.4*2.93)
    elif front_fail_conn_count > 14:
        front_lateral = (p_side_CC*0.5*30*10)-(p_side_CC*0.5*4.4*2.93)+(p_sideleading_CC*0.5*4.4*2.93)
        
    if left_fail_conn_count <= 4:
        left_lateral = p_windward_CC*3*22*14.583/2
    elif left_fail_conn_count > 4:
        left_lateral = p_windward_CC*0.5*22*14.583      
        
    if back_fail_conn_count <= 14:
        back_lateral = p_windward_CC*3*30*10/2
    elif back_fail_conn_count > 14:
        back_lateral = p_windward_CC*0.5*30*10
        
    if right_fail_conn_count <= 4:
        right_lateral = (p_side_CC*3*22*14.583/2)-(p_side_CC*0.5*4.4*5.83)+(p_sideleading_CC*0.5*4.4*5.83)
    elif right_fail_conn_count > 4:
        right_lateral = (p_side_CC*0.5*22*14.583)-(p_side_CC*0.5*4.4*5.83)+(p_sideleading_CC*0.5*4.4*5.83)
if direction == 5:
    if front_fail_conn_count <= 14:
        front_lateral = p_leeward_CC*3*30*10/2
    elif front_fail_conn_count > 14:
        front_lateral = p_leeward_CC*0.5*30*10
        
    if left_fail_conn_count <= 4:
        left_lateral = (p_side_CC*3*22*14.583/2)-(p_side_CC*0.5*4.4*5.83)+(p_sideleading_CC*0.5*4.4*5.83)
    elif left_fail_conn_count > 4:
        left_lateral = (p_side_CC*0.5*22*14.583)-(p_side_CC*0.5*4.4*5.83)+(p_sideleading_CC*0.5*4.4*5.83)
        
    if back_fail_conn_count <= 14:
        back_lateral = p_windward_CC*3*30*10/2
    elif back_fail_conn_count > 14:
        back_lateral = p_windward_CC*0.5*30*10
        
    if right_fail_conn_count <= 4:
        right_lateral = (p_side_CC*3*22*14.583/2)-(p_side_CC*0.5*4.4*5.83)+(p_sideleading_CC*0.5*4.4*5.83)
    elif right_fail_conn_count > 4:
        right_lateral = (p_side_CC*0.5*22*14.583)-(p_side_CC*0.5*4.4*5.83)+(p_sideleading_CC*0.5*4.4*5.83)
if direction == 6:
    if front_fail_conn_count <= 14:
        front_lateral = (p_side_CC*3*30*10/2)-(p_side_CC*0.5*4.4*2.93)+(p_sideleading_CC*0.5*4.4*2.93)
    elif front_fail_conn_count > 14:
        front_lateral = (p_side_CC*0.5*30*10)-(p_side_CC*0.5*4.4*2.93)+(p_sideleading_CC*0.5*4.4*2.93)
        
    if left_fail_conn_count <= 4:
        left_lateral = (p_side_CC*3*22*14.583/2)-(p_side_CC*0.5*4.4*5.83)+(p_sideleading_CC*0.5*4.4*5.83)
    elif left_fail_conn_count > 4:
        left_lateral = (p_side_CC*0.5*22*14.583)-(p_side_CC*0.5*4.4*5.83)+(p_sideleading_CC*0.5*4.4*5.83)
        
    if back_fail_conn_count <= 14:
        back_lateral = p_windward_CC*3*30*10/2
    elif back_fail_conn_count > 14:
        back_lateral = p_windward_CC*0.5*30*10
        
    if right_fail_conn_count <= 4:
        right_lateral = p_windward_CC*3*22*14.583/2
    elif right_fail_conn_count > 4:
        right_lateral = p_windward_CC*0.5*22*14.583 
if direction == 7:
    if front_fail_conn_count <= 14:
        front_lateral = (p_side_CC*3*30*10/2)-(p_side_CC*0.5*4.4*2.93)+(p_sideleading_CC*0.5*4.4*2.93)
    elif front_fail_conn_count > 14:
        front_lateral = (p_side_CC*0.5*30*10)-(p_side_CC*0.5*4.4*2.93)+(p_sideleading_CC*0.5*4.4*2.93)

    if left_fail_conn_count <= 4:
        left_lateral = p_leeward_CC*3*22*14.583/2
    elif left_fail_conn_count > 4:
        left_lateral = p_leeward_CC*0.5*22*14.583
        
    if back_fail_conn_count <= 14:
        back_lateral = (p_side_CC*3*30*10/2)-(p_side_CC*0.5*4.4*2.93)+(p_sideleading_CC*0.5*4.4*2.93)
    elif back_fail_conn_count > 14:
        back_lateral = (p_side_CC*0.5*30*10)-(p_side_CC*0.5*4.4*2.93)+(p_sideleading_CC*0.5*4.4*2.93)   

    if right_fail_conn_count <= 4:
        right_lateral = p_windward_CC*3*22*14.583/2
    elif right_fail_conn_count > 4:
        right_lateral = p_windward_CC*0.5*22*14.583 
if direction == 8:
    if front_fail_conn_count <= 14:
        front_lateral = p_windward_CC*3*30*10/2
    elif front_fail_conn_count > 14:
        front_lateral = p_windward_CC*0.5*30*10
        
    if left_fail_conn_count <= 4:
        left_lateral = (p_side_CC*3*22*14.583/2)-(p_side_CC*0.5*4.4*5.83)+(p_sideleading_CC*0.5*4.4*5.83)
    elif left_fail_conn_count > 4:
        left_lateral = (p_side_CC*0.5*22*14.583)-(p_side_CC*0.5*4.4*5.83)+(p_sideleading_CC*0.5*4.4*5.83)
        
    if back_fail_conn_count <= 14:
        back_lateral = (p_side_CC*3*30*10/2)-(p_side_CC*0.5*4.4*2.93)+(p_sideleading_CC*0.5*4.4*2.93)
    elif back_fail_conn_count > 14:
        back_lateral = (p_side_CC*0.5*30*10)-(p_side_CC*0.5*4.4*2.93)+(p_sideleading_CC*0.5*4.4*2.93)   

    if right_fail_conn_count <= 4:
        right_lateral = p_windward_CC*3*22*14.583/2
    elif right_fail_conn_count > 4:
        right_lateral = p_windward_CC*0.5*22*14.583 

front_lateral = abs(front_lateral)/45
left_lateral = abs(left_lateral)/33
back_lateral = abs(back_lateral)/45
right_lateral = abs(right_lateral)/33
lateral_loads = [front_lateral,left_lateral,back_lateral,right_lateral]

## wall sheathing
if direction == 1:
    wall_sheath_loads = [p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC,
                         p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, 
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC,
                         p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC,
                         p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC,
                         p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC,
                         p_leeward_CC, p_leeward_CC, p_leeward_CC,
                         p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, 
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC]
if direction == 2:
    wall_sheath_loads = [p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, 
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, 
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC]
if direction == 3:
    wall_sheath_loads = [p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, 
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, 
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC,
                         p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC,
                         p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC,
                         p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC,
                         p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC]
if direction == 4:
    wall_sheath_loads = [p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, 
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC,
                         p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, 
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC]
if direction == 5:
    wall_sheath_loads = [p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC,
                         p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC,
                         p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC,
                         p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC,
                         p_leeward_CC, p_leeward_CC, p_leeward_CC, 
                         p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, 
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC,
                         p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, 
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC]
if direction == 6:
    wall_sheath_loads = [p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, 
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, 
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC]
if direction == 7:
    wall_sheath_loads = [p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, 
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC,
                         p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC,
                         p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC,
                         p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC,
                         p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC, p_leeward_CC,
                         p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, 
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC]
if direction == 8:
    wall_sheath_loads = [p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC,
                         p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, 
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_sideleading_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, 
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC, p_side_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC,
                         p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC, p_windward_CC]
   
wall_sheath_loads = np.absolute(wall_sheath_loads)

if walls ==1:
    for i in range(len(failed_walls_uplift)):
        if uplift_loads[i] > total_uplift_capacity[i]:
            failed_walls_uplift[i] = 0
    for i in range(len(failed_walls_lateral)):
        if lateral_loads[i] > total_lateral_capacity[i]:
            failed_walls_lateral[i] = 0
    failed_walls_sheath = np.full(118, 1)
    for i in range(len(failed_walls_sheath)):
        if wall_sheath_loads[i] > wall_sheath_capacity[i]:
            failed_walls_sheath[i] = 0

    for i in range(len(failed_walls)):
        if failed_walls_uplift[i] < 1:
            failed_walls[i] = 0
        if failed_walls_lateral[i] < 1:
            failed_walls[i] = 0   
        
elif walls == 2:
    u_front = (front_wall_bending/front_bending_capacity)+(front_wall_uplift/front_uplift_capacity)
    u_left = (left_wall_bending/left_bending_capacity)+(left_wall_uplift/left_uplift_capacity)
    u_back = (back_wall_bending/back_bending_capacity)+(back_wall_uplift/back_uplift_capacity)
    u_right = (right_wall_bending/right_bending_capacity)+(right_wall_uplift/right_uplift_capacity)
    u = [u_front, u_left, u_back, u_right]
    
    for i in range(len(failed_walls_u)):
        if u[i] > 1:
            failed_walls_u[i] = 0
            
    failed_walls = failed_walls_u
 

### percentages of exterior failure
failed_cover_count = len(np.where(failed_cover == 0)[0])
failed_cover_percentage = (failed_cover_count/(len(failed_cover)))*100
not_failed_cover_percentage = 100 - failed_cover_percentage
cover_array = np.array([failed_cover_percentage, not_failed_cover_percentage])

failed_sheath_count = len(np.where(failed_sheath == 0)[0])
failed_sheath_percentage = (failed_sheath_count/(len(failed_sheath)))*100
not_failed_sheath_percentage = 100 - failed_sheath_percentage
sheath_array = np.array([failed_sheath_percentage, not_failed_sheath_percentage])

failed_windows_total = np.concatenate((failed_leftwindows, failed_rightwindows, failed_frontwindows, failed_backwindows))
failed_window_count = len(np.where(failed_windows_total == 0)[0])
failed_window_percentage = (failed_window_count/(len(failed_windows_total)))*100

if garage_fail == 1:
    failed_garage_percentage = 0
elif garage_fail == 0:
    failed_garage_percentage = 100

failed_connections_count = len(np.where(failed_connections == 0)[0])
failed_connections_percentage = (failed_connections_count/(len(failed_connections)))*100

door_fail = [back_door_fail, front_door_fail]
failed_door_count = 2 - np.count_nonzero(door_fail)
failed_door_percentage = (failed_door_count/2)*100

failed_walls_count = 4 - np.count_nonzero(failed_walls)
failed_walls_percentage = (failed_walls_count/4)*100

### interior damages
fen_failures = [front_door_fail, back_door_fail, failed_frontwindows[0], failed_frontwindows[1],
                    failed_frontwindows[2], failed_leftwindows[0], failed_leftwindows[1], failed_leftwindows[2],
                    failed_leftwindows[3], failed_backwindows[0], failed_backwindows[1], failed_backwindows[2],
                    failed_backwindows[3], failed_rightwindows[0], failed_rightwindows[1], failed_rightwindows[2],
                    failed_rightwindows[3], garage_fail]
fen_failed_count = 18 - np.count_nonzero(fen_failures) 
fen_failed_percent = fen_failed_count/18*100

i_cover = failed_cover_percentage*0.5
i_sheath = failed_sheath_percentage*1.8
i_fen = fen_failed_percent*1.0

interior_damage = max(i_cover, i_sheath, i_fen)

### water loadings
failed_cover_water = np.full(96, 1, dtype = int)
if ds > 11.53:
    failed_cover_water = [0,0,0,0,0,0,0,0,
                          1,1,1,1,1,1,1,1,
                          1,1,1,1,1,1,1,1,
                          1,1,1,1,1,1,1,1,
                          1,1,1,1,1,1,1,1,
                          1,1,1,1,1,1,1,1,
                          1,1,1,1,1,1,1,1,
                          1,1,1,1,1,1,1,1,
                          1,1,1,1,1,1,1,1,
                          1,1,1,1,1,1,1,1,
                          1,1,1,1,1,1,1,1,
                          0,0,0,0,0,0,0,0]
if ds > 13.07:
    failed_cover_water = [0,0,0,0,0,0,0,0,
                          0,0,0,0,0,0,0,0,
                          1,1,1,1,1,1,1,1,
                          1,1,1,1,1,1,1,1,
                          1,1,1,1,1,1,1,1,
                          1,1,1,1,1,1,1,1,
                          1,1,1,1,1,1,1,1,
                          1,1,1,1,1,1,1,1,
                          1,1,1,1,1,1,1,1,
                          1,1,1,1,1,1,1,1,
                          0,0,0,0,0,0,0,0,
                          0,0,0,0,0,0,0,0]
if ds > 14.61:
    failed_cover_water = [0,0,0,0,0,0,0,0,
                          0,0,0,0,0,0,0,0,
                          0,0,0,0,0,0,0,0,
                          1,1,1,1,1,1,1,1,
                          1,1,1,1,1,1,1,1,
                          1,1,1,1,1,1,1,1,
                          1,1,1,1,1,1,1,1,
                          1,1,1,1,1,1,1,1,
                          1,1,1,1,1,1,1,1,
                          0,0,0,0,0,0,0,0,
                          0,0,0,0,0,0,0,0,
                          0,0,0,0,0,0,0,0]
if ds > 16.16:
    failed_cover_water = [0,0,0,0,0,0,0,0,
                          0,0,0,0,0,0,0,0,
                          0,0,0,0,0,0,0,0,
                          0,0,0,0,0,0,0,0,
                          1,1,1,1,1,1,1,1,
                          1,1,1,1,1,1,1,1,
                          1,1,1,1,1,1,1,1,
                          1,1,1,1,1,1,1,1,
                          0,0,0,0,0,0,0,0,
                          0,0,0,0,0,0,0,0,
                          0,0,0,0,0,0,0,0,
                          0,0,0,0,0,0,0,0]
if ds > 17.7:
    failed_cover_water = [0,0,0,0,0,0,0,0,
                          0,0,0,0,0,0,0,0,
                          0,0,0,0,0,0,0,0,
                          0,0,0,0,0,0,0,0,
                          0,0,0,0,0,0,0,0,
                          1,1,1,1,1,1,1,1,
                          1,1,1,1,1,1,1,1,
                          0,0,0,0,0,0,0,0,
                          0,0,0,0,0,0,0,0,
                          0,0,0,0,0,0,0,0,
                          0,0,0,0,0,0,0,0,
                          0,0,0,0,0,0,0,0]
if ds > 18.64:
    failed_cover_water = [0,0,0,0,0,0,0,0,
                          0,0,0,0,0,0,0,0,
                          0,0,0,0,0,0,0,0,
                          0,0,0,0,0,0,0,0,
                          0,0,0,0,0,0,0,0,
                          0,0,0,0,0,0,0,0,
                          0,0,0,0,0,0,0,0,
                          0,0,0,0,0,0,0,0,
                          0,0,0,0,0,0,0,0,
                          0,0,0,0,0,0,0,0,
                          0,0,0,0,0,0,0,0,
                          0,0,0,0,0,0,0,0] 

failed_leftwindows_water = np.full(4, 1)
failed_rightwindows_water = np.full(4, 1)
failed_backwindows_water = np.full(4, 1)
failed_frontwindows_water = np.full(3, 1)

if ds > 3:
    failed_frontwindows_water = [0,0,0]
    failed_backwindows_water = [0,0,0,0]
if ds > 4:
    failed_leftwindows_water = [0,0,0,0]
    failed_rightwindows_water = [0,0,0,0]

front_door_fail_water = 1
back_door_fail_water = 1
if ds > 1:
    front_door_fail_water = 0
if ds > 2:
    back_door_fail_water = 0    
    
ds_round = round(ds)
if ds_round > 16:
    ds_round = 16

y_no_base_structure = [0,0,0,0,0,0,0,2.5,13.4,23.3,32.1,40.1,47.1,53.2,58.6,63.2,67.2,70.5,73.2,75.4,77.2,78.5,79.5,80.2,80.7]
x_no_base_structure = [-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
y_no_base_content = [0,0,0,0,0,0,0,2.4,8.1,13.3,17.9,22,25.7,28.8,31.5,33.8,35.7,37.2,38.4,39.2,39.7,40,40,40,40]
x_no_base_content = [-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
y_base_structure = [0,0.7,0.8,2.4,5.2,9,13.8,19.4,25.5,32,38.7,45.5,52.2,58.6,64.5,69.8,74.2,77.7,80.1,81.1,81.1,81.1,81.1,81.1,81.1]
x_base_structure = [-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
y_base_content = [0,0,0,0,33,33,33,35.4,41.1,46.3,50.9,55,58.7,61.8,64.5,66.8,68.7,70.2,71.4,72.2,72.7,73,73,73,73]
x_base_content = [-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

std_structure_basement = [0,1.34,1.06,0.94,0.91,0.88,0.85,0.83,0.85,0.96,1.14,1.37,1.63,1.89,2.14,2.35,2.52,2.66,2.77,2.88,2.88,2.88,2.88,2.88,2.88]
std_contents_basement = [1.6,1.16,0.92,0.81,0.78,0.76,0.74,0.72,0.74,0.83,0.98,1.17,1.39,1.6,1.81,1.99,2.13,2.25,2.35,2.45,2.45,2.45,2.45,2.45,2.45]
std_structure_no_basement = [0,0,0,0,0,0,0,2.7,2,1.6,1.8,1.9,2,2.1,2.2,2.3,2.4,2.7,3,3.3,3.7,4.1,4.5,4.9]
std_contents_no_basement = [0,0,0,0,0,0,0,2.1,1.5,1.2,1.2,1.4,1.5,1.6,1.6,1.7,1.8,1.9,2.1,2.3,2.6,2.9,3.2,3.5,3.8]

x_position = x_no_base_structure.index(ds_round)
if basement == 1:
    std_structure = std_structure_basement
    std_contents = std_contents_basement
    y_structure = y_base_structure
    y_contents = y_base_content
elif basement == 2:
    std_structure = std_structure_no_basement
    std_contents = std_contents_no_basement  
    y_structure = y_no_base_structure
    y_contents = y_no_base_content

y_structure_modified = [i*0.516 for i in y_structure]
y_combined = np.zeros(25)
for i in range(25):
    y_combined[i] = y_structure_modified[i]+y_contents[i]

contents_mean = float(y_combined[x_position])
contents_std = std_contents[x_position]
upper_contents_limit = contents_mean + 2*contents_std
lower_contents_limit = contents_mean - 2*contents_std
contents_water_failure = np.random.normal(contents_mean, contents_std, size = (1))

too_high_indices = np.where(contents_water_failure > upper_contents_limit)
while np.any(too_high_indices):
    contents_water_failure[too_high_indices] = np.random.normal(
        contents_mean, contents_std, size=len(too_high_indices))
    too_high_indices = np.where(contents_water_failure > upper_contents_limit)

too_low_indices = np.where(contents_water_failure < lower_contents_limit)
while np.any(too_low_indices):
    contents_water_failure[too_low_indices] = np.random.normal(
        contents_mean, contents_std, size=len(too_low_indices))
    too_low_indices = np.where(contents_water_failure < lower_contents_limit)

contents_water_failure = float(contents_water_failure)

### combination of water and wind failures
interior_damage_combined = ((interior_damage/100) + (contents_water_failure/100) - ((interior_damage/100)*(contents_water_failure/100)))*100

failed_cover_combined = np.full(96,1, dtype = int)
for i in range(len(failed_cover_combined)):
    if failed_cover[i] == 0:
        failed_cover_combined[i] = 0
    if failed_cover_water[i] == 0:
        failed_cover_combined[i] = 0

failed_frontwindows_combined = np.full(3,1)
failed_backwindows_combined = np.full(4,1)
failed_leftwindows_combined = np.full(4,1)
failed_rightwindows_combined = np.full(4,1)
for i in range(len(failed_frontwindows_combined)):
    if failed_frontwindows[i] == 0:
        failed_frontwindows_combined[i] = 0
    if failed_frontwindows_water[i] == 0:
        failed_frontwindows_combined[i] = 0
for i in range(len(failed_backwindows_combined)):
    if failed_backwindows[i] == 0:
        failed_backwindows_combined[i] = 0
    if failed_backwindows_water[i] == 0:
        failed_backwindows_combined[i] = 0      
for i in range(len(failed_leftwindows_combined)):
    if failed_leftwindows[i] == 0:
        failed_leftwindows_combined[i] = 0
    if failed_leftwindows_water[i] == 0:
        failed_leftwindows_combined[i] = 0
for i in range(len(failed_rightwindows_combined)):
    if failed_rightwindows[i] == 0:
        failed_rightwindows_combined[i] = 0
    if failed_rightwindows_water[i] == 0:
        failed_rightwindows_combined[i] = 0

front_door_fail_combined = 1
back_door_fail_combined = 1
if front_door_fail == 0 or front_door_fail_water == 0:
    front_door_fail_combined = 0
if back_door_fail == 0 or back_door_fail_water == 0:
    back_door_fail_combined = 0

failed_cover_count = len(np.where(failed_cover_combined == 0)[0])
failed_cover_percentage = (failed_cover_count/(len(failed_cover_combined)))*100
not_failed_cover_percentage = 100 - failed_cover_percentage
cover_array = np.array([failed_cover_percentage, not_failed_cover_percentage])

failed_windows_total = np.concatenate((failed_leftwindows_combined, failed_rightwindows_combined, failed_frontwindows_combined, failed_backwindows_combined))
failed_window_count = len(np.where(failed_windows_total == 0)[0])
failed_window_percentage = (failed_window_count/(len(failed_windows_total)))*100

door_fail = [back_door_fail_combined, front_door_fail_combined]
failed_door_count = 2 - np.count_nonzero(door_fail)
failed_door_percentage = (failed_door_count/2)*100

### utilities damages
electrical_damage = interior_damage_combined*0.5
plumbing_damage = interior_damage_combined*0.35
mechanical_damage = interior_damage_combined*0.4

if electrical_damage > 100:
    electrical_damage = 100
if plumbing_damage > 100:
    plumbing_damage = 100
if mechanical_damage > 100:
    mechanical_damage = 100

### print failures
print("Cover:" , failed_cover_combined)
print("Sheathing:" , failed_sheath)
print("Front Door: ", front_door_fail_combined)
print("Back Door: ", back_door_fail_combined)
print("Garage Door: ", garage_fail)
print("Left side windows:", failed_leftwindows_combined)
print("Right side windows:", failed_rightwindows_combined)
print("Front Windows: ", failed_frontwindows_combined)
print("Back Windows: ", failed_backwindows_combined)
print("Connections:" , failed_connections)
print("Walls:" , failed_walls)
print("Percentage of failed cover: ", failed_cover_percentage, "%")
print("Percentage of failed sheathing: ", failed_sheath_percentage, "%")
print("Percentage of failed windows: ", failed_window_percentage, "%")
print("Percentage of failed connections: ", failed_connections_percentage, "%")
print("Percentage of failed doors: ", failed_door_percentage, "%")
print("Percentage of failed garage doors: ", failed_garage_percentage, "%")
print("Percentage of failed walls: ", failed_walls_percentage, "%")
print("Percentage of interior damage: ", interior_damage_combined, "%")
print("Percentage of failed utilities: \n Electrical damage: ", electrical_damage, "% \n Plumbing damage: ", plumbing_damage, "% \n Mechanical damage: ", mechanical_damage, "%")

percentages = [failed_cover_percentage, failed_sheath_percentage, failed_window_percentage, failed_door_percentage, failed_garage_percentage, failed_connections_percentage, failed_walls_percentage]
components = ['Roof Cover', 'Roof Sheathing', 'Windows', 'Exterior Doors', 'Garage Doors', 'Connections', 'Exterior Walls']

fen_failures_combined = [front_door_fail_combined, back_door_fail_combined, failed_frontwindows_combined[0], failed_frontwindows_combined[1],
                    failed_frontwindows_combined[2], failed_leftwindows_combined[0], failed_leftwindows_combined[1], failed_leftwindows_combined[2],
                    failed_leftwindows_combined[3], failed_backwindows_combined[0], failed_backwindows_combined[1], failed_backwindows_combined[2],
                    failed_backwindows_combined[3], failed_rightwindows_combined[0], failed_rightwindows_combined[1], failed_rightwindows_combined[2],
                    failed_rightwindows_combined[3], garage_fail]

## write text files
file = open("Roof_Cover_Failure","w")
failed_cover_string = np.array2string(failed_cover_combined, separator="\n")
failed_cover_string = str(failed_cover_string)[1:-1]
file.write(failed_cover_string)
file.flush()

file = open("Roof_Sheath_Failure","w")
failed_sheath_string = np.array2string(failed_sheath, separator="\n")
failed_sheath_string = str(failed_sheath_string)[1:-1]
file.write(failed_sheath_string)
file.flush()

file = open("Wall_Sheath_Failure","w")
failed_wallsheath_string = np.array2string(failed_walls_sheath, separator="\n")
failed_wallsheath_string = str(failed_wallsheath_string)[1:-1]
file.write(failed_wallsheath_string)
file.flush()

file = open("Open_Failure","w")
fen_failures_combined = np.array(fen_failures_combined, dtype = int)
failed_fen_string = np.array2string(fen_failures_combined, separator="\n")
failed_fen_string = str(failed_fen_string)[1:-1]
file.write(failed_fen_string)
file.flush()

user_input = [walls, roof, exposure, vegetation, category]
file = open("User_Input", "w")
user_input = np.array(user_input, dtype = int)
user_input_string = np.array2string(user_input, separator="\n")
user_input_string = str(user_input_string)[1:-1]
file.write(user_input_string)
file.flush()

utilities = [round(electrical_damage,1), round(plumbing_damage,1), round(mechanical_damage,1)]
file = open("Utility_Percentage", "w")
utilities = np.array(utilities)
utilities_string = np.array2string(utilities, separator="\n")
utilities_string = str(utilities_string)[1:-1]
file.write(utilities_string)
file.flush()

file = open("Water_Height", "w")
ds_string = str(ds)
file.write(ds_string)
file.flush()


# wait for participant to run virtual reality simulation
root5 = tk.Tk()
root5.title('Pause')
root5.geometry("400x400")

question15 = tk.Label(root5, text = "Please find research assistant to set up virtual reality model.\n Press continue to move onto the reflection section \n after completing the simulation.")
question15.pack()

response = requests.get('https://github.com/gfusco19/VR_V1/blob/main/wait.png?raw=true')
img = Image.open(BytesIO(response.content))
img = img.resize((250, 250))
tkimage = ImageTk.PhotoImage(img)
tk.Label(root5, image=tkimage).pack()

exit_button = tk.Button(root5, text = "Continue", command = root5.destroy)
exit_button.pack(side=BOTTOM)

root5.mainloop()



# collect information on virtual reality reflection
root6 = tk.Tk()
root6.title('Reflection')
root6.geometry("400x400")


clicked16 = tk.StringVar(root6)
clicked16.set("Choose Option")

clicked17 = tk.StringVar(root6)
clicked17.set("Choose Option")

clicked18 = tk.StringVar(root6)
clicked18.set("Choose Option")



question16 = tk.Label(root6, text = "How did you think your structure would perform in \n comparison to the virtual reality model?")
question16.pack()

drop16 = tk.OptionMenu(root6,clicked16,"I thought my home would perform better", "The virtual reality matched my perception", "I thought my home would perform worse")
drop16.pack()

question17 = tk.Label(root6, text = "Would you choose to evacuate or shelter in place?")
question17.pack()

drop17 = tk.OptionMenu(root6,clicked17, "Evacuate", "Shelter in place", "I don't know")
drop17.pack()

question18 = tk.Label(root6, text = "Did the virtual reality model impact your evacuation decision")
question18.pack()

drop18 = tk.OptionMenu(root6,clicked18, "Yes", "No")
drop18.pack()


exit_button = tk.Button(root6, text = "Submit", command = root6.destroy)
exit_button.pack(side=BOTTOM)


root6.mainloop()
