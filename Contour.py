import cv2
import numpy as np


def findContourProc(frame):
   # convert img to grey
   img_grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   # set a thresh
   thresh = 100
   # get threshold image
   ret, thresh_img = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)
   # find contours
   contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
   # print(contours)
   max1 = max2 = 0
   temp2 =[]
   temp1 = []
   for i in range(len(contours)):
       area = cv2.contourArea(contours[i])
       if int(area) > max1:
           max2 = max1
           max1 = area
           temp2 = temp1
           temp1 = []
           temp1.append(contours[i])
   cv2.drawContours(frame, temp2, -1, (0, 255, 0), 3)
   cv2.imshow("Contour",frame)
   cv2.waitKey(100000)
   cv2.destroyAllWindows()

