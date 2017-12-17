import cv2
import numpy as np

def draw_bounding_box( imgcv, result ):
    img = imgcv.copy()
    for r in result:
        pt_topleft = ( r['topleft']['x'], r['topleft']['y']   )
        pt_bottomright = ( r['bottomright']['x'], r['bottomright']['y'])
        confidence = r['confidence']
        label = r['label']

        print '---'
        print pt_topleft, pt_bottomright
        print '%s: %4.2f' %(label, confidence )

        cv2.rectangle(img, pt_topleft, pt_bottomright, (255,0,0), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,'%4.2f: %s' %(confidence, label),pt_topleft, font, 0.5, (0,0,255),1)

    return img
