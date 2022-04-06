import math

import cv2
import numpy as np

def getContours(imgResults, img):
    #create image arrays for card detection
    imgGray = cv2.cvtColor(imgResults, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
    imgCanny = cv2.Canny(imgBlur, 50, 100)

    #for debugging
    cv2.imshow("Canny", imgCanny)

    #opencv method for finding contours
    contours, hierarchy = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    #initialize card array
    cardArray = []

    #iterate through detected contours and add them to the card array
    for cnt in contours:
        area = cv2.contourArea(cnt)
        peri = cv2.arcLength(cnt, True)
        corners = cv2.approxPolyDP(cnt, 0.02 * peri, True)
        if (len(corners) == 4) & (area > 50):   #if the shape has four corners, assume its a card, unless diamond, then need area
            cardArray.append(createCardImg(img, corners))

    return cardArray

#overlay detected contours from canny image to the original image to get snapshot of the card that is being detected
def createCardImg(img, corners):
    width, height = 250, 350

    #math to determine how the contour function oriented the card based on the distance of the sides
    #used to resolve bug where the cards are flipped sideways
    side1 = np.sqrt(np.sum(np.square(corners[0] - corners[1])))
    side2 = np.sqrt(np.sum(np.square(corners[1] - corners[2])))
    if (side1 > side2):
        pts1 = np.float32([corners[0], corners[3], corners[1], corners[2]])
    else:
        pts1 = np.float32([corners[1], corners[0], corners[2], corners[3]])

    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgCard = cv2.warpPerspective(img, matrix, (width, height))
    return imgCard