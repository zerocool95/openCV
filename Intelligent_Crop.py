import cv2
import numpy as np

def get_otsu_threshold(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.bitwise_not(gray)
    thresh = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    return thresh

def crop(image, weight = 0.5):
    '''
    Remove irrelevant white padding from the images from the top, bottom, left and right 
    by checking the percentage(specified by the weight param) of activated pixels in every row from top, bottom , left and right.
    '''
    image = get_otsu_threshold(image)
    h,w = image.shape
    xmin = 0
    xmax = w-1
    ymin = 0 
    ymax = h-1
    for i in range(w):
        if np.sum(image[:,i]) > image.shape[1] * weight:
            xmin = i
            break
            
    for i in range(w-1, 0, -1):
        if np.sum(image[:,i]) > image.shape[1] * weight:
            xmax = i
            break
            
    for i in range(h-1, 0, -1):
        if np.sum(image[i]) > image.shape[0] * weight:
            ymax = i
            break
            
    for i in range(h):
        if np.sum(image[i]) > image.shape[0] * weight:
            ymin = i
            break

    crop_image = image[ymin:ymax , xmin:xmax]
    return crop_image

if __name__ == '__main__':

    img = cv2.imread(<FILE_PATH>)
    cropped_img = crop(img)