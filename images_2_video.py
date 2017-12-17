import cv2

FILE_NAME = './data/mrinq-traffic-seq/DSC_0506.MOV'
for i in range(900):
    fname = FILE_NAME+'%d.jpg' %i
    print 'Open : ', fname
    im = cv2.imread( fname )
    cv2.imshow( 'im', im )
    cv2.waitKey(40)
