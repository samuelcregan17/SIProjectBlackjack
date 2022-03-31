#Main class for project, this is where the camera feed loop will exist
import cv2
import numpy as np

#main method is where camera loop exists
def main():

    #setup video feed
    cap = cv2.VideoCapture(0)
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

        #create mask and display original feed and the mask
        _, img = cap.read()
        imgHLS = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
        cv2.imshow("Original", img)
        lower = np.array([h_min, l_min, s_min])
        upper = np.array([h_max, l_max, s_max])
        mask = cv2.inRange(imgHLS, lower, upper)
        imgResults = cv2.bitwise_and(img, img, mask=mask)
        cv2.imshow("Results", imgResults) #may delete this from final code, don't think we need the mask displayed, good for debugging

        if cv2.waitKey(1) & 0xFF ==ord('q'):
            cv2.destroyAllWindows()

main()