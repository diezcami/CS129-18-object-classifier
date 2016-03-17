# cs129.18-lab-2
A program that uses Naive Bayes classification and OpenCV functionalities to solve a computer visualisation problem.

## Directory Structure
Tentative dir structure:
```
├── data/
│   ├── input/ - Input for image processing
│   ├── output/ - Output of image processing
│   ├── positives/ - Ground truth: objects
│   │   ├── 01.jpg, 02.jpg, 03.jpg ...
│   │   ├── 01.bing, 02.bing, 03.bing ...
│   │   ├── features.csv
│   ├── negatives/ - Ground truth: non-objects
│   │   ├── 01.jpg, 02.jpg, 03.jpg ...
│   │   ├── 01.bing, 02.bing, 03.bing ...
│   │   ├── features.csv
├── generate_training_csv.py
├── process_image.py
├── process_training_images.py
```

## Files
* **process_training_images.py**
  * Processes images in the *input* folder by cropping them according to contours. The cropped results will manually be classified into objects and non-objects.
* **generate_training_csv.py**
  * Creates a CSV file containing the feature vectors of the cropped images. This serves as the training model to be used when processing new images.
* **process_image.py**
  * Processes a new object by drawing blue rectangles over objects and rectangles over non-objects. The information used to process this image is retrieved from performing the Naive Bayes algorithm using the collected information in the training set.