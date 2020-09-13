import cv2
import numpy as np
import glob
from pathlib import Path
# Step 2 : Here we fetch data or we can say snapshots of documents from local storage by giving path.
# path=Path("/home/veronica/docreader")
# # Step 3 : Now we start a loop to fetch snaps one by one
# image=[]
# count=0
# for imagepath in path.glob(“*.jpeg”):
# count=count+1
image=cv2.imread("/home/veronica/docreader/paper.jpeg")
#here path of the image is taken, we can take different image by giving another.

#here image is get resized for easy processing and a feasible dimension is taken
image = cv2.resize(image, (1500, 880))
original = image.copy()
#image converted into grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#blurred the image for clear processing
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
#here edge detection is done by “canny edge detection technique. By this image can be easily segmented.
edged_image = cv2.Canny(blurred_image, 0, 50)
original_edged = edged_image.copy()
# file_name_path = ‘file path to save image’ + str(count) + ‘.png’
# cv2.imwrite(file_name_path, original_edged)
#findContours is used to find contours around the images.
(contours, _) = cv2.findContours(edged_image, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)
#a function named rectify is created to to reshape or rectify the image.
def rectify(h):
    h = h.reshape((4,2))
    hnew = np.zeros((4,2),dtype = np.float32)
    add = h.sum(1)
    hnew[0] = h[np.argmin(add)]
    hnew[2] = h[np.argmax(add)]
    diff = np.diff(h,axis = 1)
    hnew[1] = h[np.argmin(diff)]
    hnew[3] = h[np.argmax(diff)]
    return hnew
#It is obvious that if any image is clicked at a random angle it will definately have background and some other pictures and
#images also but we need to specify that detection should be done for the paper or document only. So the vertix size 4 is chosen
#of contour points.
for c in contours:
    p = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * p, True)
    #gives vertices size 4 means if vertices are 4 of any contour take that
    if len(approx) == 4:
        target = approx
        break
# mapping target points to 800x800 quadrilateral
approx = rectify(target)
pts2 = np.float32([[0,0],[800,0],[800,800],[0,800]])
M = cv2.getPerspectiveTransform(approx,pts2)
final_image = cv2.warpPerspective(original,M,(800,800))
cv2.drawContours(image, [target], -1, (0, 255, 0), 2)
final_image = cv2.cvtColor(final_image, cv2.COLOR_BGR2GRAY)
cv2.imshow("test", final_image)
# file_name_path = ‘file path to save image’ + str(count) + ‘.png’
# cv2.imwrite(file_name_path, final_image)

cv2.waitKey(0)
cv2.destroyAllWindows()