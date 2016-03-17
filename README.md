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
├── improcess.py
```

## Training Set Structure
1[n]: Positive Mean of the *nth* dimension
2[n]: Negative Mean of the *nth* dimension
3[n]: Variance/Standard Deviation of the *nth* dimension
4[0]: Probability of a Positive Object
4[1]: Probability of a Negative Object