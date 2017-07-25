import argparse
import cv2

refPt = []
refPtt = []
cropping = False
 
def click_and_crop(event, x, y, flags, param):

    global refPt, cropping, refptt

    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True
 
    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        refPt.append((x, y))
        cropping = False

        # for making the rectangle starting from any palce and ending at any place. 
        refPtt.append((min(refPt[0][0],refPt[1][0]), max(refPt[0][1],refPt[1][1])))
        refPtt.append((max(refPt[0][0],refPt[1][0]), min(refPt[0][1],refPt[1][1])))

        # draw a rectangle around the region of interest
        cv2.rectangle(image, refPtt[0], refPtt[1], (0, 255, 0), 2)
        cv2.imshow("image", image)

if __name__ == '__main__':
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the image")
    args = vars(ap.parse_args())
     
    # load the image, clone it, and setup the mouse callback function
    image = cv2.imread(args["image"])
    clone = image.copy()
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", click_and_crop)
    quitter = False
    while True: 
        # keep looping until the 'q' key is pressed
        while True:
            # display the image and wait for a keypress
            cv2.imshow("image", image)
            key = cv2.waitKey(1) & 0xFF
         
            # if the 'r' key is pressed, reset the cropping region
            if key == ord("r"):
                image = clone.copy()
         
            # if the 'c' key is pressed, break from the loop
            elif key == ord("c"):
                break
            # if 'w' is pressed program quits.
            if key == ord("w"):
                quitter = True
                break
         
        if quitter==True:
           break

        # if there are two reference points, then crop the region of interest
        # from teh image and display it
        if len(refPtt) == 2:
            roi = clone[min(refPtt[0][1],refPtt[1][1]):max(refPtt[0][1],refPtt[1][1]), min(refPtt[0][0],refPtt[1][0]):max(refPtt[0][0],refPtt[1][0])]
            cv2.imshow("ROI", roi)
            cv2.waitKey(0)
            refPtt = []
        else:
            print("No region selected!Please select region of interest.")
             

    cv2.destroyAllWindows()
