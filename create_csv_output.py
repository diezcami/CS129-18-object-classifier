import cv2
import csv
import os
import numpy as np

POSITIVE_DIR = 'positives'
NEGATIVE_DIR = 'negatives'

def create_csv_output():
	positive_images = load_images_from_folder (POSITIVE_DIR)
	negative_images = load_images_from_folder (NEGATIVE_DIR)
	positive_feature_vectors = get_all_image_feature_vectors (positive_images, True)
	negative_feature_vectors = get_all_image_feature_vectors (negative_images, False)

	with open ("output.csv", "wb") as f:
		writer = csv.writer(f)
		writer.writerows(positive_feature_vectors)
		writer.writerows(negative_feature_vectors)
  	cv2.waitKey(0);

def get_all_image_feature_vectors(images, positive):
	feature_vector = []
	for src in images:
		src = cv2.GaussianBlur( src, (3,3), 0 );	
		# Convert it to gray
  		src_gray = cv2.cvtColor(src ,cv2.COLOR_BGR2GRAY);

  		# Gradient X
  		#Scharr( src_gray, grad_x, ddepth, 1, 0, scale, delta, BORDER_DEFAULT );
  		grad_x = cv2.Sobel( src_gray, cv2.CV_16S, 1, 0, 3 );
  		abs_grad_x = cv2.convertScaleAbs( grad_x );

  		# Gradient Y
  		# Scharr( src_gray, grad_y, ddepth, 0, 1, scale, delta, BORDER_DEFAULT );
  		grad_y = cv2.Sobel( src_gray, cv2.CV_16S, 0, 1, 3 );
  		abs_grad_y = cv2.convertScaleAbs( grad_y );

		# Total Gradient (approximate)
  		grad = cv2.addWeighted( abs_grad_x, 0.5, abs_grad_y, 0.5, 0 );
  		resized = cv2.resize(grad, (8,8))
		# cv2.imshow('Sobel Image', resized)

		val_list = get_feature_vector (resized, positive)
		feature_vector.append(val_list)

	return feature_vector

def get_feature_vector (img, positive):
	val_list = []
	for x in range(0,8):
		for y in range(0,8):
			val = img[x][y]
			val_list.append(val)

	if positive:
		val_list.append(1)
	else:
		val_list.append(0)

	return val_list

def load_images_from_folder (folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images	

create_csv_output();