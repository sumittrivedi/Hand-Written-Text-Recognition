#!C:/Users/vivek/PycharmProjects/untitled1/venv/Scripts/python.exe

import cgitb
cgitb.enable()
print("Content-Type: text/html;charset=utf-8")
print() 
import numpy as np
import matplotlib.pyplot as pt
import pandas as pd
from sklearn.tree import svm

data =pd.read_csv("train.csv").values
clf=svm()

#trianing dataset
xtrain =data[0:40000,1:]
train_lebel=data[0:40000,0]
clf.fit(xtrain,train_lebel)

#test dataset
xtest=data[40000:,1:]
actual_lebel=data[40000:,0]

#Accuracy
p=clf.predict(xtest)
count=0
for i in range(0,1000):
	count+=1 if p[i]==actual_lebel[i] else 0
print("Accuracy = ", (count/1000)*100)
	
d=xtest[20]
d.shape=(28,28)
pt.imshow(255-d,cmap='gray')
print("\n Predition = ",clf.predict([xtest[20]]))
pt.show()


