
## Library Imports :: ---
import gym
import os
import time as t
import pybullet as p
import pybullet_workshop_23
import numpy as np
import cv2

CAR_LOCATION = [2,3,1.5]
# BALL_LOCATION = [4,5,1.5]
# HUMANOID_LOCATION = [-3,-4,1.3]
VISUAL_CAM_SETTINGS = dict({
    'cam_dist'       : 13,
    'cam_yaw'        : 0,
    'cam_pitch'      : -110,
    'cam_target_pos' : [0,4,0]
})

##########################################################
"""
Your task is to use env.move() and p.getKeyboardEvents() to control the husky using the arrow keys
of you keyboard and make the husky stop when the spacebar is pressed (like games :D

"""
##########################################################

os.chdir(os.path.dirname(os.getcwd()))

#Environment Setup ::---
env = gym.make('pybullet_workshop_23',
    arena = "arena1",
    car_location=CAR_LOCATION,
    visual_cam_settings=VISUAL_CAM_SETTINGS
)


###################### Write your code from here ###########################



def Findcontour(img, lowerRange, UpperRange):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lowerRange, UpperRange)
    res = cv2.bitwise_and(img, img, mask=mask)
    imgray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    contours, hierarchy = cv2.findContours(imgray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours

vel=[[0,0],
     [0,0]]

while True:
    # p.stepSimulation()
    keys = p.getKeyboardEvents()
    img = env.get_image(cam_height=0, dims=[600, 600])
    img = cv2.flip(img, 5)
    # range of RED color in HSV
    lower_color = np.array([0, 50, 50], dtype=np.uint8)
    upper_color = np.array([10, 255, 255], dtype=np.uint8)
    #####
    contours = Findcontour(img, lower_color, upper_color)
    cv2.drawContours(img,contours,-1,(0,0,255),2) ### uncomment to draw contours
    cv2.imshow('camera_feed', img)
    sorted(contours, key=cv2.contourArea)



    if p.B3G_UP_ARROW in keys and keys[p.B3G_UP_ARROW] & p.KEY_IS_DOWN:
        for a in vel:
            a[0] += 0.3
            a[1] += 0.3
        env.move(vels=vel)

    elif p.B3G_LEFT_ARROW in keys and keys[p.B3G_LEFT_ARROW] & p.KEY_IS_DOWN:
        for a in vel:
            a[0] -= 0.1
            a[1] += 0.1
        env.move(vels=vel)

    elif p.B3G_DOWN_ARROW in keys and keys[p.B3G_DOWN_ARROW] & p.KEY_IS_DOWN:
        for a in vel:
            a[0] -= 0.4
            a[1] -= 0.4
        env.move(vels=vel)

    elif p.B3G_RIGHT_ARROW in keys and keys[p.B3G_RIGHT_ARROW] & p.KEY_IS_DOWN:
        for a in vel:
            a[0] += 0.1
            a[1] -= 0.1
        env.move(vels=vel)

    elif 32 in keys and keys[32] & p.KEY_IS_DOWN:
        vel = [[0, 0],
               [0, 0]]
        env.move(vels=vel)
    else:
        pass

    k = cv2.waitKey(100)
    if k == ord('q'):
        break

    # t.sleep(0.1)


