import os
import cv2
import numpy as np

from config import *

def preprocess1(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("gray", gray)

    threshold = gray.copy()
    mask = (threshold < MIN_THRESHOLD) | (threshold > MAX_THRESHOLD)
    notMask = np.bitwise_not(mask)
    threshold[mask] = 0
    threshold[notMask] = 255
    # cv2.imshow("threshold", threshold)

    kernel = np.ones((11, 11), np.uint8)

    morphclose = cv2.morphologyEx(threshold, cv2.MORPH_CLOSE, kernel)
    # cv2.imshow("morphopen", morphclose)

    kernelErode = np.ones((5, 5), np.uint8)
    erode = cv2.morphologyEx(morphclose, cv2.MORPH_ERODE, kernelErode)
    # cv2.imshow("erode", erode)

    return erode

