#Main class for project, this is where the camera feed loop will exist
import cv2
import numpy as np

#main method is where camera loop exists
import algorithm
import detectCard
import identifyCard


def main():

    # set up text prompts
    userPrompt = "To scan your cards, focus your cards"
    dealerPrompt = "To scan dealer's card, focus the card"
    playAgainPrompt = "To play again, press e'w'. To quit, press 'e'"

    #setup video feed
    cap = cv2.VideoCapture(1)
    cap.set(3, 640) #set width
    cap.set(4, 480) #set height
    while True:
        # call method to prompt the user to scan the players cards
        playerCardNames, playerCardValues = scanCards(cap, userPrompt)

        # call method to prompt the user to scan the dealers cards
        dealerCardNames, dealerCardValues = scanCards(cap, dealerPrompt)

        ### call to algorithm here using "userCardValues" and "dealerCardValues"
        suggestedMove = algorithm.determineMove(playerCardValues, dealerCardValues, False)
        print(suggestedMove)

        playAgain = displayMove(cap, playAgainPrompt, suggestedMove)

        if playAgain:
            pass
        else:
            break



# this method is how we prompt the user to scan the correct cards
def scanCards(cap, prompt1):
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
        prompt2 = "and press \'q\' to scan."
        cv2.putText(img, prompt1, (10, 420), cv2.FONT_HERSHEY_COMPLEX, .75, (0, 0, 0), 2)
        cv2.putText(img, prompt2, (10, 450), cv2.FONT_HERSHEY_COMPLEX, .75, (0, 0, 0), 2)

        #display original image, create mask and display mask
        cv2.imshow("Original", img)
        lower = np.array([h_min, l_min, s_min])
        upper = np.array([h_max, l_max, s_max])
        mask = cv2.inRange(imgHLS, lower, upper)
        imgResults = cv2.bitwise_and(img, img, mask=mask)
        cv2.imshow("Results", imgResults) #may delete this from final code, don't think we need the mask displayed, good for debugging

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cardArray2 = detectCard.getContours(imgResults, img)
            cardNames, cardValues = identifyCard.matchCards(cardArray2)
            print(cardNames)  # testing
            print(cardValues)  # testing
            return cardNames, cardValues

def displayMove(cap, prompt, move):
    move = move + "!"
    while True:
        _, img = cap.read()

        cv2.putText(img, move, (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
        cv2.putText(img, prompt, (10, 450), cv2.FONT_HERSHEY_COMPLEX, .75, (0, 0, 0), 2)

        cv2.imshow("Original", img)

        if cv2.waitKey(1) & 0xFF == ord('w'):
            return True
        elif cv2.waitKey(1) & 0xFF == ord('e'):
            return False


main()