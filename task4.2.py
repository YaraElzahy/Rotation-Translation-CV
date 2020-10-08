#______________________________________________    Author: Yara Elzahy    _____________________________________________#
#______________________________________________     Date: 6/10/2020       _____________________________________________#
#______________________________________________     Version: 1.0.0        _____________________________________________#
#______________________________________________     Title: Task 4.2       _____________________________________________#
# _____________________________________________    ~  Description  ~      _____________________________________________#
#_________________________ This code rotates and translates a video dynamically using trackbars _______________________#

import cv2
import numpy as np


# This function will be called whenever the value of the trackbar changes
def trackbarCallBack(x):
    print(x)   # prints the current trackbar value


def setup():
    # set initial position of trackbars
    cv2.setTrackbarPos('x-shift', 'Trackbars', 127)
    cv2.setTrackbarPos('y-shift', 'Trackbars', 127)
    cv2.setTrackbarPos('angle', 'Trackbars', 180)


def translate_with_trackbar():
    # triggers the current position of the trackbar
    x = cv2.getTrackbarPos('x-shift', 'Trackbars')
    y = cv2.getTrackbarPos('y-shift', 'Trackbars')
    # (trackbar name, window name)

    rows, cols = frame.shape[0], frame.shape[1]
    # matrix of transformation
    # M = [ 1 0 x_shift; 0 1 y_shift]

    # set to initial position with shift in x and y of zero at (127, 127)
    M = np.float32([[1, 0, x - 127], [0, 1, y - 127]])

    # # 3rd argument :(width, height) Remember width = number of columns, and height = number of rows.
    dst = cv2.warpAffine(frame, M, (cols, rows))
    return dst


def rotate_with_trackbar():
    # triggers the current position of the trackbar
    angle = cv2.getTrackbarPos('angle', 'Trackbars')
    # (trackbar name, window name)

    rows, cols = res.shape[0], res.shape[1]
    #     # matrix of transformation
    # (center of rotation, degree in anti CLK-wise, scale factor)
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle - 180, 1)
    dst = cv2.warpAffine(res, M, (cols, rows))
    return dst


if __name__ == "__main__":

    cap = cv2.VideoCapture(0)

    # create a new window
    cv2.namedWindow('Trackbars')

    # resize your window
    cv2.resizeWindow('Trackbars', 500, 100)

    # create a black background image for the trackbars
    img = np.ones((38, 512, 3), np.uint8)

    # callbackfn that will be called when u move the trackbar
    # lazem yeb2a fih callback fn even if we don't need it

    cv2.createTrackbar('x-shift', 'Trackbars', 0, 255, trackbarCallBack)
    cv2.createTrackbar('y-shift', 'Trackbars', 0, 255, trackbarCallBack)
    cv2.createTrackbar('angle', 'Trackbars', 0, 360, trackbarCallBack)

    setup()   # set initial trackbars' state

    while True:
        # read frame
        _, frame = cap.read()
        cv2.imshow("Trackbars", img)

        # wait for keystroke
        k = cv2.waitKey(1) & 0xFF

        # if 'esc' or 'q' is pressed, exit and close window
        if (k == 27) or (k == ord('q')):
            break
        # if 'r' is pressed, return to initial state
        if k == ord('r'):
            setup()

        res = translate_with_trackbar()
        res = rotate_with_trackbar()
        cv2.imshow('output', res)

    cap.release()
    cv2.destroyAllWindows()
