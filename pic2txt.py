import cv2
import numpy as np


#get letter set
letter_set=[]
for index in xrange(65,91):
	letter_int=index
	letter_str=chr(letter_int)
	img_saving_name='./letter_img/'+letter_str+'.jpg'
	letter_img=cv2.imread(img_saving_name,0)
	letter_img=cv2.resize(letter_img,(16,16))
	letter_img=cv2.threshold(letter_img, 128, 255, cv2.THRESH_BINARY)[1]
	letter_set.append(letter_img)
letter_num=len(letter_set)

img=cv2.imread('./lena.bmp')
img=cv2.resize(img,(1024,1024))
img_w=img.shape[1]
img_h=img.shape[0]
print img_w
print img_h
img = cv2.GaussianBlur(img,(5,5),0)
img_canny = cv2.Canny(img, 50, 150)
cv2.imshow('img_canny',img_canny)
cv2.waitKey(500)
letter_position=np.zeros((img_h//16,img_w//16))
img_letter=np.zeros((img_h,img_w))
for w_index in xrange(img_w//16):
	for h_index in xrange(img_h//16):
		sub_img=img_canny[h_index*16:(h_index+1)*16,w_index*16:(w_index+1)*16]
		sub_img=cv2.threshold(sub_img, 128, 255, cv2.THRESH_BINARY)[1]
		if np.max(sub_img)>128:
			dis=[]
			for letter_index in xrange(letter_num):
				dis.append(np.sum(np.abs(np.int32(sub_img)-letter_set[letter_index])))
			letter_sel=np.argmin(dis)
			#print letter_sel
			letter_position[h_index,w_index]=letter_sel+65
			img_letter[h_index*16:(h_index+1)*16,w_index*16:(w_index+1)*16]=letter_set[letter_sel]

print letter_position

cv2.imshow('img_letter',img_letter)
cv2.imwrite('./img_letter.jpg',img_letter)
cv2.imwrite('./img_letter_canny.jpg',(img_letter+img_canny)//2)

cv2.waitKey(5000) 

