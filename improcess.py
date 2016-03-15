import cv2
import numpy as np

INPUT_DIR = 'data/input/'
OUTPUT_DIR = 'data/output/'

def improcess(filename):
	# Load image
	orig = cv2.imread(INPUT_DIR + filename)
	img = orig.copy()
	imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	#Perform canny
	edges = cv2.Canny(imgray,100,200)

	#Find contours
	ret,thresh = cv2.threshold(edges,100,200,0)
	image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	#Draw contours
	for i in range(len(contours)):
		image = cv2.drawContours(img, contours, i, (0,255,0), 1)
		x,y,w,h = cv2.boundingRect(contours[i])
		cv2.rectangle(image, (x, y), (x+w, y+h), (255,0,0), 2)
		
		# Arbitrary threshold height and width is 10, 10:
		if h>20 and w>20: 
			cropimg = orig[y:y+h, x:x+w]
			output_name = OUTPUT_DIR + filename[:-4] + str(i) + '.jpg'
			cv2.imwrite(output_name, cropimg)
			
			# To show individual images in a window:
			# cv2.imshow('Cropped Image ' + str(i), cropimg)
		
	cv2.imshow('Canny Image', edges)
	cv2.imshow('Original Image', orig)
	cv2.imshow('Annotated Image', image)
	cv2.waitKey(0)

improcess('test6.jpg')
