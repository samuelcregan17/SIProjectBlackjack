import cv2
import numpy as np
import os

path2 = 'CardsTest' #test image directory


images2 = [] #array to store test images

classNames2 = [] #array to store names of test images

testList = os.listdir(path2)  # creates list of all test image names


# create the baseline images that we will compare the detected cards to (using bicycle card set)
def createBaselineImgs():
    path1 = 'Final Images'
    images = []
    classNames = []
    myList = os.listdir(path1)
    for cl in myList:
        imgCur = cv2.imread(f'{path1}/{cl}', 0)
        images.append(imgCur)
        classNames.append(os.path.splitext(cl)[0])  # store without file extension

    return images, classNames


# finds descriptive points of all baseline images and stores in descriptionList
def findDescription(images):
    orb = cv2.ORB_create(nfeatures=2000)
    descriptionList = []
    # loops through baseline images and creates descriptions
    for img in images:
        kp, des = orb.detectAndCompute(img, None)
        descriptionList.append(des)
    return descriptionList

# determines the best match for an image from the baseline images
def findID(img, desList):
    orb = cv2.ORB_create(nfeatures=2000)
    kp2, des2 = orb.detectAndCompute(img, None)
    bf = cv2.BFMatcher()
    matchList = []
    finalVal = -1
    try:
        #checks all descriptions to find best match
        for des in desList:
            matches = bf.knnMatch(des, des2, k=2)
            good = []
            for m, n in matches:
                if m.distance < 0.75 * n.distance:
                    good.append([m])
            matchList.append(len(good))
    except:
        pass

    # print(matchList)
    if len(matchList) != 0:
        finalVal = matchList.index(max(matchList))
    return finalVal

# determines the number value of the card based on the card description
def determineCardVal(cardName):
    cardVal = 10 # set initial value to ten, if the card is not 1 - 9, then it is 10 or face card
    firstLetter = cardName[0]
    if firstLetter == 'T' or firstLetter == 'J' or firstLetter == 'Q' or firstLetter == 'K':
        cardVal = 10
    elif firstLetter == 'A':
        cardVal = 1
    else:
        cardVal = int(firstLetter)

    return cardVal

# takes in the detected card array from main and returns arrays of the card descriptions and number values
def matchCards(cardArray):
    cardNames = [] # array to hold the names of each card in order once they are identified
    cardValues = [] # array to hold the value of each card once identified
    images, classNames = createBaselineImgs()
    descriptionList = findDescription(images)

    for card in cardArray:
        id = findID(card, descriptionList)
        cardName = classNames[id]
        cardValue = determineCardVal(cardName)
        cardNames.append(cardName)
        cardValues.append(cardValue)

    return cardNames, cardValues
