from darkflow.net.build import TFNet
import cv2
from cv_utils import *

INPUT_IMAGE = "./data/real_car.png"

options = {"model": "cfg/yolo.cfg", "load": "bin/yolo.weights", "threshold": 0.2}
tfnet = TFNet(options)

imgcv = cv2.imread(INPUT_IMAGE)

result = tfnet.return_predict(imgcv)
print(result)

result_im = draw_bounding_box( imgcv, result )

cv2.imwrite( 'img.png', result_im )
# cv2.waitKey(0)
