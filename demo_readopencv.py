import cv2
import numpy as np
from cv_utils import *
from darkflow.net.build import TFNet

FILE_NAME = './data/mrinq-traffic-seq/DSC_0506.MOV'
cap = cv2.VideoCapture(FILE_NAME)

options = {"model": "cfg/yolo.cfg", "load": "bin/yolo.weights", "threshold": 0.2}
tfnet = TFNet(options)

frame_count = 0
while True:
    ret, frame = cap.read()
    frame_resized = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)

    result = tfnet.return_predict(frame_resized)
    print(result)
    result_im = draw_bounding_box( frame_resized, result )

    # cv2.imshow( 'frame', frame_resized )
    # cv2.imshow( 'frame_provc', result_im )
    # if cv2.waitKey(10) & 0xFF == ord('q'):
        # break

    # cv2.imwrite( 'file.png', cv2.resize(frame, (0,0), fx=0.3, fy=0.3) )
    print 'Write : ', FILE_NAME+'%d.jpg' %(frame_count)
    cv2.imwrite( FILE_NAME+'%d.jpg' %(frame_count), result_im)
    frame_count += 1

cap.release()
