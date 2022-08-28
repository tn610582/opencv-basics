"""
Opencv read videostream, show stream and write to file
"""
import cv2
import numpy as np

capture = cv2.VideoCapture(0)
# capture = cv2.VideoCapture('<your video file>')

fourcc = cv2.VideoWriter_fourcc(*'X264')
fps = 20
width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
vid_writer = cv2.VideoWriter('./test.mp4', fourcc, fps, (width, height))

while True:
    rec,frame = capture.read()
    
    frame = cv2.flip(frame,1)

    frame = cv2.line(frame,pt1=(100, 100), pt2=(200,200), color=(255,0,0), thickness=10)

    vid_writer.write(frame)
    cv2.imshow("Test", frame)

    # exit condiction
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break


vid_writer.release()
cv2.release()
cv2.destroyAllWindows()