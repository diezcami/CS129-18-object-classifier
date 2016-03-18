# cs129.18-lab-2
A program that uses Naive Bayes classification and OpenCV functionalities to solve a computer visualisation problem.

## Directory Structure
```
├── input/ - Input for image processing
│   ├── 01.jpg, 02.jpg, 03.jpg ...
├── output/ - Output of image processing
│   ├── 01.jpg, 02.jpg, 03.jpg ...
├── data/
│   ├── input/ - Input for training set image processing
│   │   ├── 01.jpg, 02.jpg, 03.jpg ...
│   ├── output/ - Output of training set image processing
│   │   ├── 01.jpg, 02.jpg, 03.jpg ...
│   ├── positives/ - Ground truth: objects
│   │   ├── 01.jpg, 02.jpg, 03.jpg ...
│   ├── negatives/ - Ground truth: non-objects
│   │   ├── 01.jpg, 02.jpg, 03.jpg ...
│   ├── training_data/ - Generated data from the training set
│   │   ├── output.csv
│   │   ├── negative_mean.txt
│   │   ├── positive_mean.txt
│   │   ├── variance.txt
├── generate_training_csv.py
├── process.py - Main driver file
├── process_training_images.py
```

## Files
* **process_training_images.py**
  * Processes images in the *input* folder by cropping them according to contours. The cropped results will manually be classified into objects and non-objects.
* **generate_training_csv.py**
  * Creates a CSV file containing the feature vectors of the cropped images. This serves as the training model to be used when processing new images.
* **process.py** (Driver Class)
  * Processes a new object by drawing blue rectangles over objects and rectangles over non-objects. The information used to process this image is retrieved from performing the Naive Bayes algorithm using the collected information in the training set.
  * **Input**: All images in the input/ directory
  * **Output**: Processed images to be found in the output/ directory