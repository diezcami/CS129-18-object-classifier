import cv2
import numpy as np

POSITIVE_PROBABILITY = 0.398809524
NEGATIVE_PROBABILITY = 0.601190476
INPUT_DIR = 'data/input/'
OUTPUT_DIR = 'data/output/'        

def process_image(filename):
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

            # HI SEAN DO YOUR STUFF HERE
            # result = process_image_part (output of whatever goes here)
            # if result = 0 = red, else blue
            
    cv2.waitKey(0)

# Returns a list with 64 elements/dimensions
def process_image_part(src):
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

    val_list = get_feature_vector (image)

    return val_list

def get_feature_vector(src):
    val_list = []
    for x in range(0,8):
        for y in range(0,8):
            val = img[x][y]
            val_list.append(val)

    return val_list

# Retrieves mean and variance information required for the NB algorithm
def process_training_data (file_name):
    file_address = "data/training_data/" + file_name
    training_data = open(file_address,'r')
    dimension_data = []
    for dimension in training_data:
        dimension_data.append(dimension)

    return dimension_data

# Actual NB algorithm. Returns 1 if the image is an object and 0 otherwise.
def check_objectivity():
    positive_mean = process_training_data("positive_mean")
    negative_mean = process_training_data("negative_mean")
    variance = process_training_data("variance")
    feature_vector = process_image_part(src)
    sum_positive = 0
    sum_negative = 0
    for i in range(len(feature_vector)):
        base = 1/math.sqrt(2*math.pi*variance[i])
        positive_mult = math.e * (-1 * (feature_vector[i] - positive_mean[i]) ** 2)) / (2 * variance[i])
        negative_mult = math.e * (-1 * (feature_vector[i] - negative_mean[i]) ** 2)) / (2 * variance[i])

        sum_positive = sum_positive + (base * positive_mult)
        sum_negative = sum_positive + (base * positive_mult)

    if sum_positive > sum_negative:
        return 1
    else
        return 0

process_image ('test6.jpg')