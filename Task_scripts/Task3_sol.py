## Library Imports :: ---

## Library Imports :: ---
import gym
import os
import time as t
import pybullet as p
import pybullet_workshop_23
import numpy as np
import cv2

CAR_LOCATION = [-0.7,8.5,1.5]
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
Your task is to make husky follow the red line autonomously using opencv and PID control.
This is BONUS TASK.
"""
##########################################################



os.chdir(os.path.dirname(os.getcwd()))
# Environment Setup ::---
env = gym.make('pybullet_workshop_23',
    arena = "arena1",
    car_location=CAR_LOCATION,
    visual_cam_settings=VISUAL_CAM_SETTINGS
)


###################### Write your code from here ###########################


def stop():
    env.move(vels=[[0, 0], [0, 0]])

def move(mode='f', speed=5):
    if mode.lower() == "f":
        mat = [[speed, speed], [speed, speed]]
    elif mode.lower() == "r":
        mat = [[speed, -speed], [speed, -speed]]
    else:
        print("Error Occurred , Unexpected mode in Move Function.")
        return "Error"
    env.move(vels=mat)

def MovePID(cnt):
    x, y, w, h = cv2.boundingRect(cnt)
    x = x + w / 2
    if x > 320:
        move('r', (320 - x) / 10)
    elif x < 280:
        move('r', (280 - x) / 10)
    else:
        move('f', 10)
        area = cv2.contourArea(cnt)

def Findcontour(img, lowerRange, UpperRange):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lowerRange, UpperRange)
    res = cv2.bitwise_and(img, img, mask=mask)
    imgray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    contours, hierarchy = cv2.findContours(imgray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours

vel=[[0,0],
     [0,0]]
# env.open_grip()
while True:
    # p.stepSimulation()
    keys = p.getKeyboardEvents()
    img = env.get_image(cam_height=0, dims=[600, 600])
    img = cv2.flip(img, 5)

    img = img[200:450, :]

    # range of RED color in HSV
    lower_color = np.array([50, 0, 0], dtype=np.uint8)
    upper_color = np.array([255, 255, 255], dtype=np.uint8)



    # hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # mask = cv2.inRange(hsv, lower_color, upper_color)
    # res = cv2.bitwise_and(img, img, mask=mask)
    # imgray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    # contours, hierarchy = cv2.findContours(imgray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)



    contours = Findcontour(img, lower_color, upper_color)
    cv2.drawContours(img,contours,-1,(0,255,0),2) ### uncomment to draw contours
    cv2.imshow('camera_feed', img)
    sorted(contours, key=cv2.contourArea)
    contours = list(contours)
    if len(contours) != 0:
        cnt = contours[-1]
        MovePID(cnt)
    else:
        move("r", -5)

    k = cv2.waitKey(100)
    if k == ord('q'):
        break

    # t.sleep(0.1)


