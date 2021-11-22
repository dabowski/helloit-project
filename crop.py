import cv2
import numpy as np
import sys

img = cv2.imread(sys.argv[1])

if img is None:
    sys.exit("Nie mozna wczytac obrazu")


cropped_image = img[int(sys.argv[2]):int(sys.argv[4]), int(sys.argv[3]):int(sys.argv[5])]

try:
    cv2.imwrite("cropped_" + sys.argv[1], cropped_image)
except:
    print("\nWystapil blad\n")
