import cv2
import numpy as np

img = cv2.imread('./img.png')

while True:
    cv2.imshow('patric',img)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()