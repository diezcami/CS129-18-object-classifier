import cv2
import numpy as np
#from cv2 import NormalBayesClassifier

class DataPoint:
        feature_vector = []
        label = -1

        def __init__(self, vector, label):
                self.feature_vector = vector
                self.label = label

        def set_label(self,label):
                self.label = label

train_data = []
samples = []

def naivebayes_train(filename):
      file_object = open(filename)
      data = file_object.readlines()
      for line in data:
              line_vector = line.split(',')
              label = line_vector.pop(-1)
              temp_point = DataPoint(line_vector, label)
              train_data.append(temp_point)
      #cv2.NormalBayesClassifier.train(train_data)
      file_object.close();
        
def naivebayes_predict(filename):
        file_object = open(filename)
        data = file_object.readlines()
        for line in data:
                line_vector = line.split(',')
                line_vector.pop(-1)
                temp_point = DataPoint(line_vector, 0)
                samples.append(temp_point)
        file_object.close();
        
        for point in samples:
                label = cv2.NormalBayesClassifier.predict(samples)
                point.set_label(label)
                print label

naivebayes_train('output.csv')