import numpy as np
import cv2
import os

'''
Purpose:
1. Face detection using haar cascades and save headshots on loacl disk.
2. Corner Detection 
3. Draw some shapes on images
'''
start_xy = False
end_xy = False
rect = (0,0,0,0)

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(frame,(x,y),100,(255,0,0),-1)

def on_mouse(event,x,y,flag,params):
	global rect, start_xy, end_xy

	if start_xy == True and end_xy == True :
		start_xy = False
		end_xy = False
		rect = (0,0,0,0)

	if event == cv2.EVENT_LBUTTONDBLCLK and start_xy == False :
		rect = (x,y,0,0)
		start_xy = True
	elif event == cv2.EVENT_LBUTTONDBLCLK and end_xy == False :
		rect = (rect[0], rect[1], x, y)
		end_xy = True

if __name__ == '__main__':
	cap = cv2.VideoCapture("Megamind.avi")	#Put the name of the video here. 0 for your own primary webcam.

	face_cascade = cv2.CascadeClassifier('../../opencv/data/haarcascades/haarcascade_frontalface_default.xml')
	profile_face_cascade = cv2.CascadeClassifier('../../opencv/data/haarcascades/haarcascade_profileface.xml')
	upper_body = cv2.CascadeClassifier('../../opencv/data/haarcascades/haarcascade_upperbody.xml')
	i=0
	while(True):
	    ret, frame = cap.read()
	    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	    faces = face_cascade.detectMultiScale(frame,2,5)
	    p_faces = profile_face_cascade.detectMultiScale(frame,2,5) 
	    u_body = upper_body.detectMultiScale(frame,5,10)
	    for (x,y,w,h) in p_faces:
	        cv2.rectangle(frame,(x,y),(x+w,y+h),(200,255,0),2)
	    
	    for (x,y,w,h) in faces:
	        cv2.rectangle(frame,(x,y),(x+w,y+h),(200,255,0),2)

		for (x,y,w,h) in u_body:
			cv2.rectangle(frame,(x,y),(x+w,y+h),(200,255,0),2)
	        crop_img = frame[y: y + h, x: x + w]
	        if i%5 == 0:
	            cv2.imwrite("face" + str(i)+ ".jpg", crop_img)
	        i=i+1
	   
		#uncomment for corner detection
	    # gray = np.float32(gray)  #corner detection code
	    # dst = cv2.cornerHarris(gray,2,3,0.05)
	    # dst = cv2.dilate(dst,None)
	    # frame[dst > 0.01*dst.max()] = [0,0,255]
	    cv2.imshow('frame',frame)

	    cv2.setMouseCallback('frame', draw_text)     

	    #drawing rectangle
	    if start_xy == True and end_xy == True:
	        cv2.rectangle(frame, (rect[0], rect[1]), (rect[2], rect[3]), (0, 0, 0), 3)

	    #if cv2.waitKey(1) & 0xFF == ord('c'):

	    if cv2.waitKey(20) & 0xFF == ord('q'):
	        break	


	cap.release()
	cv2.destroyAllWindows()
