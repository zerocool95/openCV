import cv2
import numpy as np
'''
Tag image by simple mouse clicks using openCV
'''

img = cv2.imread('watch.jpg',0) #insert image name in place of "watch.jpg"

def draw_text(event, x,y, flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
    	#gg = raw_input()
        cv2.putText(img,"tag", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,0), 1)
        #print nameTextField.get()

def paint_canvas():
    winname="Press ESC to exit; Double Click to TAG"
    cv2.namedWindow(winname)
    cv2.setMouseCallback(winname,draw_text)
    while(1):
        cv2.imshow(winname,img)
        if cv2.waitKey(2) & 0xFF ==27:
            break
            
    cv2.destroyAllWindows()

if __name__ == '__main__':
    paint_canvas()
