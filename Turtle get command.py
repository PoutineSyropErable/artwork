# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 18:13:41 2022

@author: Francois
"""

import numpy as np
import os
import sys
import matplotlib.pyplot as plt
import math
from scipy.optimize import curve_fit
import matplotlib
matplotlib.rcParams["figure.dpi"]=250 #Increasing the Graphs Resolution.

print("-------")
print("This is the current path")
print(os.getcwd())
print(sys.path[0])
os.chdir(sys.path[0] + "/Data_CSV")


# OM ({DOOM}/{DO}) and contour of Eternal. 
OE = np.loadtxt("OE.csv",delimiter=",")
OI = np.loadtxt("OI.csv",delimiter=",")
M = np.loadtxt("M.csv",delimiter=",")
EC = np.loadtxt("Eternal Contour.csv",delimiter=",")
#end of OM

def GetCode(Name,data,colorMode): #Could have used an array to identify but fuck that

    Fill = True

    print("---------------------------")
    print("This is the code for ",Name+ ":")
    print("")
    
    
    z = "def draw_" + str(Name)+"():" + "\n" + "    "
    z += str(Name) +"= turtle.Turtle()" + "\n" + "    "
    z +=  str(Name) +".penup()" +"\n" + "    "
    
    if Fill:
        z +=  str(Name) +".begin_fill()" +"\n    "
        z +=  str(Name) +".pensize(1.3)" +"\n    "
        z +=  str(Name) +".color(0,0,0)" +"\n    "
        
    
    
    
    if colorMode == "White":
        z +=  str(Name) +".fillcolor(255,255,255)" +"\n    "
    if colorMode == "Black":
        z +=  str(Name) +".fillcolor(0,0,0)" +"\n    "
    if colorMode == "Red":
        z +=  str(Name) +".fillcolor(222,42,42)" +"\n    "
        
    if colorMode == "Dark_Grey":
        z +=  str(Name) +".fillcolor(97,97,97)" +"\n    "
        
    if colorMode == "Light_Grey":
        z +=  str(Name) +".fillcolor(146,146,146)" +"\n    "
        
        
    if colorMode == "Shit_Brown":
        z +=  str(Name) +".fillcolor(142,91,38)" +"\n    "
        
    if colorMode == "Light_Brown":
        z +=  str(Name) +".fillcolor(194,155,106)" +"\n    "
        
    if colorMode == "Mid_Brown":
        z +=  str(Name) +".fillcolor(155,118,68)" +"\n    "
    
    if colorMode == "Dark_Brown":
        z +=  str(Name) +".fillcolor(112,86,53)" +"\n    "
    
    if colorMode == "Lightest_Brown":
        z +=  str(Name) +".fillcolor(220,177,119)" +"\n    "
        
    if colorMode == "Shit_Brown_Darker":
        z +=  str(Name) +".fillcolor(104,74,42)" +"\n    "
        
    if colorMode == "Orange":
        z +=  str(Name) +".fillcolor(255,69,22)" +"\n    "
        
    if colorMode == "Mid_Grey":
        z +=  str(Name) +".fillcolor(79,89,100)" +"\n    "


    z +=  str(Name) + ".goto(" + str(data[0][0]) + "," + str(data[0][1]) + ")" +"\n    "
    z +=  str(Name) +".pendown()" +"\n    "
    

    
    for i in range(1,len(data)):
        z +=  str(Name) + ".goto(" + str(data[i][0]) + "," + str(data[i][1]) + ")" +"\n    "
    
    z +=  str(Name) + ".goto(" + str(data[0][0]) + "," + str(data[0][1]) + ")" +"\n    "
    
    if Fill:
        z +=  str(Name) +".end_fill()  \n    "
    
    
    z +=  str(Name) + ".hideturtle()"
    print(z)
    print("")
    print("_______")
    print("")
    
def GetLetter(Name,ColorMode):
    data2 = np.loadtxt(str(Name)+".csv",delimiter=",")
    GetCode(str(Name),data2,ColorMode)
    
    
    
    
def GetStuff1():

    GetCode("O",OE,"Black")
    GetCode("O",OI,"White")
    
    GetCode("M",M,"Black")
    
    GetCode("EC",EC,"Red")
    
    
    T = np.loadtxt("T.csv",delimiter=",")
    GetCode("T",T,"White")
    
    
        
    
    GetLetter("E1","White")
    
    GetLetter("T","White")
    GetLetter("E2","White")
    
    GetLetter("R","White")
    
    GetLetter("RI","Red")
    
    GetLetter("N","White")
    
    GetLetter("A","White")
    GetLetter("Ai","Red")
    
    GetLetter("L","White")


def GetStuff2():
    os.chdir(sys.path[0] + "/Data_CSV")
    os.chdir("./Crucible")
    print("-------")
    print("This is the current path")
    print(os.getcwd())

    
    #---------------Start of crucible
    
    GetLetter("CC","White")
    
    GetLetter("handle","Black")
    
    GetLetter("pommel","Red")
    GetLetter("CP","Dark_Grey")
    GetLetter("CB","Dark_Grey")
    
    GetLetter("Blade","Red")
    GetLetter("connection","Dark_Grey")
    
    GetLetter("Lhlg","Light_Grey")
    GetLetter("lhlg2","Light_Grey")
    
    GetLetter("rhlg1","Light_Grey")
    GetLetter("rhlg2","Light_Grey")
    
    GetLetter("rslg1","Light_Grey")
    GetLetter("rslg2","Light_Grey")
    GetLetter("Triangle_Middle","Light_Grey")
    GetLetter("shape_middle","Light_Grey")
    
    
    
    
    #--------------------GET THE SHAPE OF THE HANDLE----------------------
    
    handleshape = np.loadtxt("handle.csv",delimiter=",")
    print(handleshape[:0],np.shape(handleshape))
    plt.plot(handleshape[:,0],handleshape[:,1],".")
    plt.plot(handleshape[0,0],handleshape[0,1],".")
    #plt.plot(handleshape[1,0],handleshape[1,1],".")
    #plt.plot(handleshape[3:10,0],handleshape[3:10,1],".")
    plt.plot(handleshape[10:,0],handleshape[10:,1],".")
    plt.show
    
    Xdown , Ydown = handleshape[3:10,0],handleshape[3:10,1]
    
    Xup,Yup = handleshape[10:,0],handleshape[10:,1]
    Xup = list(Xup)
    Xup.append(handleshape[0,0])
    
    
    Yup = list(Yup)
    Yup.append(handleshape[0,1])
    
    #plt.plot(Xup,Yup)
    #plt.plot(Xdown,Ydown)
                     
    
    MatDown = np.polyfit(Xdown,Ydown,3)
    func_down = np.poly1d(MatDown)


    plt.plot(Xdown,func_down(Xdown))

    MatUp = np.polyfit(Xup,Yup,3)
    func_up = np.poly1d(MatUp)
    

    
    plt.plot(Xup,func_up(Xup))
    

    
    print("Matdown=",MatDown)
    print("Matup=",MatUp)
    
    H = MatUp-MatDown
    
    print("H=",H)
    
    #-------------------- END OF GET THE SHAPE OF THE HANDLE----------------------

def GetCurve(Name,Color_Name):

    data = np.loadtxt(str(Name)+".csv",delimiter=",")
    t = np.linspace(0,1,len(data))
    print("lenght =",len(t),len(data[:,0]))
    
    
    N = min(7,len(data))
    
    x_of_t_coeff = np.polyfit(t,data[:,0],N)
    y_of_t_coeff = np.polyfit(t,data[:,1],N)
    
    x_func = np.poly1d(x_of_t_coeff)
    y_func = np.poly1d(y_of_t_coeff)
    
    t_arr = np.linspace(0,1,4*len(data))
    
    
    #plt.figure()
    #plt.plot(t,data[:,0],".b",ms=4)
    #plt.plot(t_arr,x_func(t_arr),"-",color="tab:orange",label="the x line")
    #plt.legend()
    #plt.show()
    
    
    #plt.figure()
    #plt.plot(t,data[:,1],".b",ms=4)
    #plt.plot(t_arr,y_func(t_arr),"-",color="tab:orange",label="the y line")
    #plt.legend()
    #plt.show()
    
    
    
  #  plt.figure()
   # plt.plot(data[:,0],data[:,1])
   # plt.plot(x_func(t_arr),y_func(t_arr),".",label="the line")
    #plt.show()    
    
    x_rev,y_rev = np.flip(x_of_t_coeff),np.flip(y_of_t_coeff)
    
    print(x_rev)
    
    x_dot_coeff,y_dot_coeff = [],[]
    for i in range(N-1):
        x_dot_coeff.append(x_rev[i+1])
        y_dot_coeff.append(y_rev[i+1]*(i+1))
    
    print(x_dot_coeff)
        
    x_dot_coeff = np.flip(np.array(x_dot_coeff))
    y_dot_coeff = np.flip(np.array(y_dot_coeff))
        
    x_dot_func = np.poly1d(x_dot_coeff) 
    y_dot_func = np.poly1d(y_dot_coeff)
    
    slope_func = lambda t: -x_dot_func(t)/y_dot_func(t)
    norm_func = lambda t: np.sqrt(1+ (slope_func(t))**2)
    
    r = 0.2
    
    
    
    x_r = lambda t: x_func(t) + r/norm_func(t)
    y_r = lambda t: y_func(t) + abs(slope_func(t)*r/norm_func(t))
    
    x_r2 = lambda t: x_func(t) - r/norm_func(t)
    y_r2 = lambda t: y_func(t) - abs(slope_func(t)*r/norm_func(t))
    
    
    
    X1,Y1 = [], []
    X2,Y2 = [] ,[]
    
    if 1==0:
        
        for i in range(len(t_arr)):
            if y_r(t_arr[i]) <= np.max(data[:,1]) and y_r(t_arr[i]) >= np.min(data[:,1]):
                X1.append(x_r(t_arr[i]))
                Y1.append( y_r(t_arr[i]) )
            if y_r2(t_arr[i]) <= np.max(data[:,1]) and y_r2(t_arr[i]) >= np.min(data[:,1]):
                X2.append(x_r2(t_arr[i]))
                Y2.append(y_r2(t_arr[i]))
    else:
        X1 = list(x_r(t_arr))
        Y1 = list(y_r(t_arr))
        
        X2 = list(x_r2(t_arr))
        Y2 = list(y_r2(t_arr))
    
    """
    plt.figure()
    plt.plot(x_func(t_arr),y_func(t_arr),".",label="the line")
    plt.plot(x_r(t_arr),y_r(t_arr),".",label="Side 1")
    plt.plot(x_r2(t_arr),y_r2(t_arr),".",label="Side 2")
    plt.legend()
    plt.show()
    
    plt.figure()
    plt.plot(x_func(t_arr),y_func(t_arr),".",label="the line")
    plt.plot(X1,Y1,".",label="Side 1")
    plt.plot(X2,Y2,".",label="Side 2")
    plt.legend()
    plt.show()
    """
    
    
  # X2_rev = X1.append(X2.reverse())
    
    print("____________________")
    print("")
    print("This is the Xs")
    print(X1)
    print("")
    print("x2")
    #print(X2[::-1])
    
    print("____________________")
    print("")
    print("This is the Ys")
    print(Y1)
    print("")
    print("Y2")
    print(Y2[::-1])
    
    
    X_string = X1
    X_string.extend(X2[::-1])
    Y_string = Y1
    Y_string.extend(Y2[::-1])
    
    print("-----")
    print("This is the string")
    print(X_string)
    print("")
    print(Y_string)
    
    DATA = np.transpose(np.array([X_string,Y_string]))
    
    print("This is the data")
    print(np.shape(DATA))
    print(DATA)
    GetCode(Name,DATA,Color_Name)
    
 
    
 
#-----------------------------rUNNING THE FUCTION THAT GET THE STUFF   


 


#--------------------------------GETTING THE STRING ON THE HANDLE





def Get_Curves():
    os.chdir(sys.path[0] + "/Data_CSV/Crucible/Handle line")
    print("-------")
    print("This is the current path")
    print(os.getcwd())

    GetCurve("l1","Shit_Brown")
    GetCurve("l2","Shit_Brown")
    GetCurve("l3","Shit_Brown")
    GetCurve("l4","Shit_Brown")
    GetCurve("l5","Light_Brown")
    GetCurve("l6","Mid_Brown")
    GetCurve("l7","Mid_Brown")
    GetCurve("l8","Dark_Brown")
    GetCurve("l9","Mid_Brown")
    GetCurve("l10","Lightest_Brown")
    GetCurve("l11","Mid_Brown")
    GetCurve("l12","Shit_Brown")
    GetCurve("l13","Shit_Brown_Darker")

    GetCurve("symbol_p1","Orange")
    GetCurve("symbol_p2","Orange")
    GetCurve("symbol_p3","Orange")
    GetCurve("symbol_p4","Orange")
    GetCurve("symbol_p5","Orange")
    GetCurve("symbol_p6","Orange")




def get_pommel_detail():
    os.chdir(sys.path[0] + "/Data_CSV")
    os.chdir("./Crucible")
    os.chdir("./pommel")
    print("-------")
    print("This is the current path")
    print(os.getcwd())

    GetLetter("p_c1","Mid_Grey")
    GetLetter("p_c2","Mid_Grey")

    GetLetter("s1","Mid_Grey")
    GetLetter("s2","Mid_Grey")
    GetLetter("trident","Mid_Grey")

    GetLetter("m1","Mid_Grey")
    GetLetter("m2","Mid_Grey")
    GetLetter("m3","Mid_Grey")
    GetLetter("m4","Mid_Grey")
    GetLetter("m5","Mid_Grey")
    GetLetter("m6","Mid_Grey")

    GetLetter("llg","Mid_Grey")
    GetLetter("ulg","Mid_Grey")
    GetLetter("dlg","Mid_Grey")



#GetStuff1() #DOOM and Eternal
#GetLetter("f_name","Orange")
#GetStuff2() #The crucible
Get_Curves() #The string on the handle
get_pommel_detail() #self obvious




    
    

    
    
    

