import cv2
import numpy as np

font =cv2.FONT_HERSHEY_SIMPLEX
for index in xrange(33,127):
	img=np.zeros((64,64,3))
	letter_int=index
	letter_str=chr(letter_int)
	print letter_int,letter_str
	cv2.putText(img,letter_str,(0,0),font,8,(255,255,255),2,cv2.LINE_AA)
	img_saving_name='./letter_img/'+letter_str+'.jpg'
	cv2.imwrite(img_saving_name,img)
	cv2.imshow(letter_str,img)
	cv2.waitKey(500)
