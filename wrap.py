import cv2
import numpy as np
# from matplotlib import pyplt as plt
def sort(pnts):
    pt1 = pt2 = pt3 = pt4 = []
    swap = []
    if pnts[0][1] > pnts[2][1] or pnts[0][1] > pnts[3][1] or pnts[1][1] > pnts[2][1] or pnts[1][1] > pnts[3][1]:
        if pnts[2][0] > pnts[3][0]:
            pt1 = pnts[3]
            pt2 = pnts[2]
            if pnts[0][0] > pnts[1][0]:
                pt3 = pnts[1]
                pt4 = pnts[0]
            else:
                pt4 = pnts[1]
                pt3 = pnts[0]

    if pnts[2][0] < pnts[3][0]:
        swap = pnts[2][0]
        pnts[2][0] = pnts[3][0]
        pnts[3][0] = swap

    pnts = [pt1,pt2,pt3,pt4]

    return pnts
        

def Wrap(img, pnts):
    pntsi = pnts
    # pnts = sort(pnts)
    print("final", pnts)
    pts1 = np.float32(pnts)
    pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
    M = cv2.getPerspectiveTransform(pts1,pts2)
    dst = cv2.warpPerspective(img,M,(300,300))
    cv2.imshow(str(pntsi), dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # plt.subplot(121),plt.imshow(img),plt.title('Input')
    # plt.subplot(122),plt.imshow(dst),plt.title('Output')
    # plt.show()

# import cv2
# import numpy as np
# import sys
# # from matplotlib import pyplt as plt

# def Wrap(img, pnts):
#     rows,cols,ch = img.shape
#     pts1 = np.float32(pnts)
#     pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
#     M = cv2.getPerspectiveTransform(pts1,pts2)
#     dst = cv2.warpPerspective(img,M,(300,300))
#     cv2.waitKey(0)
#     cv2.imshow("wrap", dst)
#     save = input("Save the Image? [Y/n]: ")
#     if "y" in save.lower():
#         cv2.imwrite("Scan.jpg",dst)
#     cv2.destroyAllWindows()
#     sys.exit(0)
#     # plt.subplot(121),plt.imshow(img),plt.title('Input')
#     # plt.subplot(122),plt.imshow(dst),plt.title('Output')
#     # plt.show()
