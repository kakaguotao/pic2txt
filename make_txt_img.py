import cv2
import numpy as np

font =cv2.FONT_HERSHEY_SIMPLEX
for index in xrange(33,127):
	img=np.zeros((16,16,3))
	letter_int=index
	letter_str=chr(letter_int)
	print letter_int,letter_str
	cv2.putText(img,letter_str,(2,12),font,0.5,(255,255,255),1)
	img_saving_name='./letter_img/'+letter_str+'.jpg'
	cv2.imwrite(img_saving_name,img)
	cv2.imshow('letter',img)
	cv2.waitKey(500)
