import cv2
import numpy as np


#get letter set
letter_set=[]
for index in xrange(33,127):
	letter_int=index
	letter_str=chr(letter_int)
	img_saving_name='./letter_img/'+letter_str+'.jpg'
	letter_img=cv2.imread(img_saving_name)
	letter_img=cv2.resize(letter_img,(8,8))
	letter_set.append(letter_img)


img=cv2.imread('')
img_w=np.shape[1]
img_h=np.shape[0]
img = cv2.GaussianBlur(img,(3,3),0)
img_canny = cv2.Canny(img, 50, 150)
cv2.imshow('img_canny',img_canny)
letter_position=np.zeros((img_h//8,img_w//8))
img_letter=np.zeros((img_h,img_w))
for w_index in xrange(img_w//8):
	for h_index in xrange(img_h//8):
		sub_img=img[h_index*8:(h_index+1)*8,w_index*8:(w_index+1)*8]
		if max(sub_img)>0:
			for letter_index in xrange(letter_num):
				dis.append(np.sum(abs(sub_img-letter_set(letter_index))))
			letter_sel=np.argmin(dis)+33
			letter_position[h_index,w_index]=letter_sel
			img_letter[h_index*8:(h_index+1)*8,w_index*8:(w_index+1)*8]=letter_set(letter_index)

print letter_position
cv2.imshow('img_letter',img_letter)
cv2.imwrite('./img_letter.jpg',img_letter)

if cv2.waitKey(0) == 27:  
    cv2.destroyAllWindows()

