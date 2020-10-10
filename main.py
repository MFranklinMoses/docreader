import sys
import cv2
import wrap
import numpy as np
import requests
# from matplotlib import pyplot as plt
from auto import autoprocess

pnts=[]
count = 0
def click_event(event, x, y, flags, param):
    pnt=[]
    global count
    if event == cv2.EVENT_LBUTTONDOWN:
        # print(x,', ' s,y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', '+ str(y)
        image = cv2.circle(img, (x,y), 5, (0,0, 255), 5)
        # cv2.putText(img, strXY, (x, y), font, .5, (255, 255, 0), 2)
        cv2.imshow('image', img)
        
        count+=1
        save(x,y,count)
        
        print(count)
            
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ', '+ str(green)+ ', '+ str(red)
        cv2.putText(img, strBGR, (x, y), font, .5, (0, 255, 255), 2)
        cv2.imshow('image', img)
    
def save(x,y, count):
    global pnts
    if count >3:
        cv2.setMouseCallback('image', click_event, param=None)
        
    pnts.append([x,y])
    print(pnts)


def captureImage():
    cap = cv2.VideoCapture(0)

    if cap.isOpened() == False: 
        print("Error opening video stream or file")

    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:

            cv2.imshow('Frame',frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                proc_frame = frame.copy()
                # cv2.imwrite("proc.jpg", proc_frame)
                break

        else: 
            break

    cap.release()
    cv2.destroyAllWindows()

    return proc_frame

def captureImageIpCamera(url, src):
    cap = cv2.VideoCapture(url)
    autoprocess(cap, src)




if __name__ == "__main__":
    choice = int(input("auto [1] \n manual [2] \n Quit [3]"))
    if choice == 1:
        c = int(input("Default cam 1, IPcam 2"))
        if c == 1:
            url=0
            captureImageIpCamera(url,c)
        elif c == 2:
            url = input("Enter your IpWebcam URL")
            captureImageIpCamera(url,c)

        # auto(proc_image)

    elif choice == 2:
        proc_image = captureImage()
        img = proc_image.copy()
        #img = np.zeros((512, 512, 3), np.uint8)
        cv2.imshow('image', img)
        # four_point_transform(img, [[232,89],[546,85],[174,372],[600,372]])
        cv2.setMouseCallback('image', click_event)
        # print(pnts)
        # image = cv2.imread("")
        # 2
        # p.Wrap(proc_image)
        if cv2.waitKey(0) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
        wrap.Wrap(proc_image, pnts)
        # wrap.Wrap(proc_image)

    elif choice == 3:
        sys.exit("Thank You!")
    else:
        print("Invalid User choice")


