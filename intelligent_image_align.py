import numpy as np
import cv2

def align_image(image):
    '''
    Aligns image horizontally by checking the regression line that fits the pixels points and then rotating it for with the
    horizontal.
    '''
    thresh = get_otsu_threshold(image)
    shape = thresh.shape
    zeros = np.zeros((thresh.shape[0], 500))
    thresh = np.hstack([zeros,thresh,zeros])
    shape = thresh.shape
    zeros = np.zeros((500, thresh.shape[1]))
    thresh = np.vstack([zeros,thresh,zeros])
    coords = np.column_stack(np.where(thresh.T > 0))
    rows,cols = thresh.shape[:2]
    [vx,vy,x,y] = cv2.fitLine(coords, cv2.DIST_WELSCH,0,0.01,0.1)
    lefty = int((-x*vy/vx) + y)
    righty = int(((cols-x)*vy/vx)+y)
    angle = (vy/vx)*180/3.14
    (h, w) = thresh.shape
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(thresh, M, (w, h),flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated


if __name__ == '__main__':

    img = cv2.imread(<FILE_PATH>)
    aligned_img = align_image(img)