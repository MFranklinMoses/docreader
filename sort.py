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
# if __name__ == "__main__":
#     # pnts = [[190, 142], [288, 122], [261, 38], [160, 57]]
#     sort(pnts)