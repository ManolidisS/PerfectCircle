import ctypes
user32 = ctypes.windll.user32
from math import cos, sin, radians
from mouse import *
from time import sleep
from keyboard import wait

radius = int(input("Radius: "))
sectors = int(input("Sectors: "))

print("Hotkey is \\")

screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
midpoint_x = round(screensize[0]/2)
midpoint_y = round(screensize[1]/2)

def x_pos(theta,r,j):
    return r*cos(radians(theta))+j

def y_pos(theta,r,k):
    return r*sin(radians(theta))+k

def y_transformation(y):
    return -1*(y - screensize[1])

while True:
    wait("\\")

    for i in range(sectors+1):
        angle = (360/sectors)*i
        move(x_pos(angle,radius,midpoint_x),y_transformation(y_pos(angle,radius,midpoint_y)))
        press()
        sleep(2/sectors)

    release()