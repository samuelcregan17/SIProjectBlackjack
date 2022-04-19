import cv2
import numpy as np
import os

####DELETE?
#path1 = 'Cards' #baseline image directory
path2 = 'CardsTest' #test image directory

####DELETE?
#images = [] #array to store baseline images
images2 = [] #array to store test images
#classNames = [] #array to store names of baseline images
classNames2 = [] #array to store names of test images
#myList = os.listdir(path1)  # creates list of all baseline image names
testList = os.listdir(path2)  # creates list of all test image names

####DELETE?
# adds baseline images to 'images' array
# for cl in myList:
#     imgCur = cv2.imread(f'{path1}/{cl}', 0)
#     images.append(imgCur)
#     classNames.append(os.path.splitext(cl)[0])  # store without file extension

####DELETE?
# adds test images to an array to 'images2' array
# for cl in testList:
#     imgCur = cv2.imread(f'{path2}/{cl}', 0)
#     images2.append(imgCur)
#     classNames2.append(cl)  # store with file extension

# create the baseline images that we will compare the detected cards to (using bicycle card set)
def createBaselineImgs():
    path1 = 'Cards'
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

    print(matchList)
    if len(matchList) != 0:
        finalVal = matchList.index(max(matchList))
    return finalVal

# determines the number value of the card based on the card description
def determineCardVal(cardName):
    cardVal = 10 # set initial value to ten, if the card is not 1 - 9, then it is 10 or face card
    cardName = cardName.split()
    firstWord = cardName[0]
    if firstWord == 'Ace':
        cardVal = 1
    elif firstWord == 'Two':
        cardVal = 2
    elif firstWord == 'Three':
        cardVal = 3
    elif firstWord == 'Four':
        cardVal = 4
    elif firstWord == 'Five':
        cardVal = 5
    elif firstWord == 'Six':
        cardVal = 6
    elif firstWord == 'Seven':
        cardVal = 7
    elif firstWord == 'Eight':
        cardVal = 8
    elif firstWord == 'Nine':
        cardVal = 9

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

####DELETE?
###TESTING
# desList = findDescription(images)
# print(classNames)
# print("")
# for img in classNames2:
#     print(img)
#     img3 = cv2.imread(path2 + '/' + img, 0)
#     id = findID(img3, desList)
#     print(id)
#     print(classNames[id] + "\n")

####DELETE?
#create cropped image array for more accurate indentification
def cropImgs(cardArray):
    croppedCardArray = []
    for card in cardArray:
        croppedCardArray.append(card[0:55, 0:35])

    return croppedCardArray
