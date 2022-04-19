#Main class for project, this is where the camera feed loop will exist
import cv2
import numpy as np

#main method is where camera loop exists
import detectCard
import identifyCard


def main():

    #setup video feed
    cap = cv2.VideoCapture(1)
    cap.set(3, 640) #set width
    cap.set(4, 480) #set height

    #while loop for camera feed
    while True:
        #preset color values for detecting white
        h_min = 0
        h_max = 179
        l_min = 233
        l_max = 255
        s_min = 0
        s_max = 255

        #read video feed and create mask
        _, img = cap.read()
        imgHLS = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

        #prompt user to scan cards
        scanUserCardsTxt1 = "To scan your cards, focus your cards"
        scanUserCardsTxt2 = "and press \'q\' to scan."
        cv2.putText(img, scanUserCardsTxt1, (10, 420), cv2.FONT_HERSHEY_COMPLEX, .75, (0, 0, 0), 2)
        cv2.putText(img, scanUserCardsTxt2, (10, 450), cv2.FONT_HERSHEY_COMPLEX, .75, (0, 0, 0), 2)

        #display original image, create mask and display mask
        cv2.imshow("Original", img)
        lower = np.array([h_min, l_min, s_min])
        upper = np.array([h_max, l_max, s_max])
        mask = cv2.inRange(imgHLS, lower, upper)
        imgResults = cv2.bitwise_and(img, img, mask=mask)
        cv2.imshow("Results", imgResults) #may delete this from final code, don't think we need the mask displayed, good for debugging


        #how we exit the loop to capture and identify cards
        if cv2.waitKey(1) & 0xFF ==ord('q'):
            # call function to create the array of card images
            cardArray = detectCard.getContours(imgResults, img)

            # call function to identify each card detected, store name and value of card in arrays
            cardNames, cardValues = identifyCard.matchCards(cardArray)
            print(cardNames) # testing
            print(cardValues) # testing

            numCards = 1
            # to show the cards we detected (for debugging, may not need in final code)
            for card in cardArray:
                winName = "Card " + str(numCards)
                cv2.imshow(winName, card)
                numCards += 1

            #cv2.destroyAllWindows()

main()