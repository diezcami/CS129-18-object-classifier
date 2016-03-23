import cv2
import numpy as np
import math
import os

# Some constant declarations
POSITIVE_PROBABILITY = 0.398809524
NEGATIVE_PROBABILITY = 0.601190476
INPUT_DIR = 'input/'
OUTPUT_DIR = 'output/'

# Retrieved from process_training_images.py
def process_image(image, id):
    # Load image
    img = image.copy()
    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # Perform canny
    edges = cv2.Canny(imgray,100,200)

    # Find contours
    ret,thresh = cv2.threshold(edges,100,200,0)
    image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours
    for i in range(len(contours)):
        image = cv2.drawContours(img, contours, i, (0,255,0), 1)
        x,y,w,h = cv2.boundingRect(contours[i])
        
        # Arbitrary threshold height and width is 20, 20:
        if h>20 and w>20: 
            feature_vector = process_image_component(image[y:y+h, x:x+w])
            is_object = check_objectivity(feature_vector)
            # if is_object==1: blue rectangle, else red
            if is_object == 1:
                cv2.rectangle(image, (x, y), (x+w, y+h), (255,0,0), 2)
            else:
                cv2.rectangle(image, (x, y), (x+w, y+h), (0,0,255), 2)

    cv2.imshow('Annotated Image', image)
    output_name = OUTPUT_DIR + str(id) + '.jpg'
    cv2.imwrite(output_name, image)
    cv2.waitKey(0)

# Adjusts a cropped component of an image, and retrieves/returns its feature vector
# Retrieved from generate_training_csv.py
def process_image_component(src):
    src = cv2.GaussianBlur( src, (3,3), 0 );    
    src_gray = cv2.cvtColor(src ,cv2.COLOR_BGR2GRAY);

    # Retrieve X Gradient
    grad_x = cv2.Sobel( src_gray, cv2.CV_16S, 1, 0, 3 );
    abs_grad_x = cv2.convertScaleAbs( grad_x );

    # Retrieve Y Gradient
    grad_y = cv2.Sobel( src_gray, cv2.CV_16S, 0, 1, 3 );
    abs_grad_y = cv2.convertScaleAbs( grad_y );

    # Retrieve Approximate Total Gradient
    grad = cv2.addWeighted( abs_grad_x, 0.5, abs_grad_y, 0.5, 0 );
    resized = cv2.resize(grad, (8,8))

    val_list = get_feature_vector (resized)
    
    return val_list
    

# Returns a feature vector of an image in form of a list with 64 elements/dimensions
# To be called in the process_image_component method
# Retrieved from generate_training_csv.py
def get_feature_vector(src):
    val_list = []
    for x in range(0,8):
        for y in range(0,8):
            val = src[x][y]
            val_list.append(val)

    return val_list

# Actual NB algorithm. Returns 1 if the image is an object and 0 otherwise.
def check_objectivity(feature_vector):
    positive_mean = process_training_data('positive_mean')
    negative_mean = process_training_data('negative_mean')
    variance = process_training_data('variance')
    sum_positive = 0
    sum_negative = 0
    for i in range(len(feature_vector)):
        base = 1 / math.sqrt(2 * math.pi * float(variance[i]))
        positive_mult = math.e * ((-1 * (float(feature_vector[i]) - float(positive_mean[i])) ** 2) / (2 * float(variance[i])))
        negative_mult = math.e * ((-1 * (float(feature_vector[i]) - float(negative_mean[i])) ** 2) / (2 * float(variance[i])))

        sum_positive = sum_positive + (base * positive_mult)
        sum_negative = sum_negative + (base * negative_mult)

    if sum_positive > sum_negative:
        return 1
    else:
        return 0

# Retrieves mean and variance information
# Called in the check_objectivity method
def process_training_data (file_name):
    file_address = 'data/training_data/' + file_name + '.txt'
    training_data = open(file_address,'r')
    dimension_data = []
    for dimension in training_data:
        dimension_data.append(dimension)

    return dimension_data

# Returns a list of images found in a directory
def load_images_from_folder (folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images

images = load_images_from_folder (INPUT_DIR)
for i, image in enumerate(images):
    process_image(image, i)
