#!/usr/bin/env python
# coding: utf-8

# ## Generate dataset from video
# #### In this step, the inout video is read frame by frame.
# ####  For each frame, the red channel is filtered and the top, bottom and center coordinate of the red ball are stored in a csv file

# In[3]:


import cv2
import numpy as np
import  csv
import imutils

# print('Enter name of csv:')
# path = input()
# print('Enter name of video:')
# video = input()
# if not (path):
path = "output1.csv"
# if not (video):
video = "ball_video1.mp4"

# Variables to write data in csv file
oFile = open(path,"w")
writer = csv.writer(oFile, delimiter = ',', dialect = 'excel', lineterminator = '\n')

# create video capture object
video_ = cv2.VideoCapture(video)

# wait till video is playing
while not video_.isOpened():
    print("Loading Video")
    video_ = cv2.VideoCapture("ball_video1.mp4")
    cv2.waitKey(1000)

# variables to store ball x-y coordinates
ball_x =[]
ball_y =[]


# ###### Read video and store data

# In[4]:



# read video frame by frame
pos_frame = video_.get(cv2.CAP_PROP_POS_FRAMES)
while True:
    flag, frame = video_.read()
    if flag:
        cv2.imshow('video', frame)
        pos_frame = video_.get(cv2.CAP_PROP_POS_FRAMES)
        print(str(pos_frame)+" frames")
        
        img_hsv = cv2.cvtColor(cv2.rotate(frame, cv2.ROTATE_180), cv2.COLOR_BGR2HSV)
        mask_lb = cv2.inRange(img_hsv, (0,90,50), (5,255,255)) # lower bound for red color hsv value
        mask_ub = cv2.inRange(img_hsv, (175,90,50), (180,255,255)) # upper bound for red color hsv value
        mask = cv2.bitwise_or(mask_lb, mask_ub )
        contours= cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(contours)
        if contours:
            contours_ = max(contours, key=cv2.contourArea)
            ball_top = tuple(contours_[contours_[:, :, 1].argmin()][0])
            ball_bottom = tuple(contours_[contours_[:, :, 1].argmax()][0])
            max_contour = contours[0]
            for contour in contours:
                if cv2.contourArea(contour)>cv2.contourArea(max_contour):
                    max_contour=contour
            contour=max_contour
            M=cv2.moments(contours_)
            if M['m00']!=0: # Midpoint coordinate of ball
                x=int(M['m10']//M['m00'])
                y=int(M['m01']//M['m00'])
                # print("x: %d"%x)
                # print("y: %d"%y)
                # ball_x.append(x)
                # ball_y.append(y)
                writer.writerow([x, y])
            #print(ball_top)
            #print(ball_bottom)
            #writer.writerow([ball_top[0], ball_top[1]])
            #writer.writerow([ball_bottom[0], ball_bottom[1]])
    else:   # wait for next frame        
        video_.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, pos_frame-1)
        cv2.waitKey(1000)
    if cv2.waitKey(10) == 27:
        break
    if video_.get(cv2.CAP_PROP_POS_FRAMES) == video_.get(cv2.CAP_PROP_FRAME_COUNT): 
        # traversed all frames
        break

