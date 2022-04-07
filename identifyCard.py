import cv2
import numpy as np
import os

path1 = 'Cards' #baseline image directory
path2 = 'CardsTest' #test image directory
orb = cv2.ORB_create(nfeatures=2000)

images = []
images2 = []
classNames = []
classNames2 = []
myList = os.listdir(path1)  # creates list of all baseline image names
testList = os.listdir(path2)  # creates list of all test image names

# adds baseline images to an array
for cl in myList:
    imgCur = cv2.imread(f'{path1}/{cl}', 0)
    images.append(imgCur)
    classNames.append(os.path.splitext(cl)[0])  # store without file extension

# adds test images to an array
for cl in testList:
    imgCur = cv2.imread(f'{path2}/{cl}', 0)
    images2.append(imgCur)
    classNames2.append(cl)  # store with file extension


# finds descriptive points of all baseline images and stores in descriptionList
def findDescription(images):
    descriptionList = []
    # loops through baseline images and creates descriptions
    for img in images:
        kp, des = orb.detectAndCompute(img, None)
        descriptionList.append(des)
    return descriptionList

# determines the best match for an image from the baseline images
def findID(img, desList):
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

###TESTING
desList = findDescription(images)
print(classNames)
print("")
for img in classNames2:
    print(img)
    img3 = cv2.imread(path2 + '/' + img, 0)
    id = findID(img3, desList)
    print(id)
    print(classNames[id] + "\n")
