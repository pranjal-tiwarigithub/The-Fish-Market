# -*- coding: utf-8 -*-
"""ML_Training.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_K0tsvicenE9RQ32Htu7PmaF6lfLgqgD

CS50
"""

#I have selected a Fish market dataset.
#So, using this dataset I’ll build simple linear regression model as well as multiple-linear regression model.
#So, in simple linear regression I’ll take Length as the predictor value and predict the weight of the fish.
#Whereas in multiple linear regression I’ll take length, width & height as the predictor values and predict the weight of the fish.

# Importing Libraries

import pandas as pd
import matplotlib.pyplot as plt

# Creating a object called fish and storng the dataset into that object.
# Using read_csv to load tha dataset.

fish = pd.read_csv("/workspaces/79278298/project/Fish.csv")

# Using head function to display the first 10 rows of the dataset.

fish[fish["Species"] == "Roach"]

fish["Species"].unique()

# Using the corr() method to find the correlation between each column present in the dataset.

print(fish.corr())

# As we got the correlation between the columns and i can see Length3 is more precise then Lenght1 and Lenght2.
# So I'll take Length3 as the predictor value and will predict the Weight.

"""# Simple Linear Regression"""

# Here x is the independent variable and y is the dependent variable.

x = fish[["Length3"]]
y = fish[["Weight"]]

#sklearn is the library
#linear_model & model selection is the package
#LinearRegression & train_test_split is the function

from sklearn.linear_model import LinearRegression

# So, here i'm spliting the dataset into two subsets.
# First subset is known as Training dataset - Training data is the initial dataset i'm using to teach a machine learning algo to recognise patterns.
# Second subset is known as Testing dataset - Testing data is used to evaluate the accuracy of your model.

# So, here i have take train_size=0.75 that means 75% of my data is training dataset and remaining 25% we can use it for testing.

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=0.75,random_state= 2)

# shape is a tuple that always gives dimensions of the array.

x_train.shape

y_train.shape

# So, here finally i've created a model of linear regression.
# fit_intercept is the parameter used to calculate intercept for the model.

model = LinearRegression(fit_intercept = True)

# I've inserted the training data successfully in the model.

model.fit(x_train, y_train)

# Now i'll predict the weight using the text dataset to check the accuracy of the model.

y_pred = model.predict(x_test)

# Classification metrics. metrics module implements several loss, score, and utility functions to measure classification performance.

from sklearn import metrics

# The coefficient of determination (R2) is a measure that provides information about the goodness of fit of a model.
# The Best possible r2 score is 1, my models r2 score is 0.72 so it means it's almost 72% accurate.
# Most reliable r2 score for a model is 0.9 and i'm not even nearby. It menas my model is not very accurate.

metrics.r2_score(y_test, y_pred)

# coef_ gives the coefficient value.

model.coef_

# intercept_ gives the intercept value.

model.intercept_

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline

plt.scatter(x_test, y_test)

plt.plot(x_test, y_pred, color = "orange")

plt.show()



"""# Multiple Linear Regression"""

from sklearn.preprocessing import LabelEncoder

#create instance of label encoder
lab = LabelEncoder()

#perform label encoding on 'team' column
fish['Species'] = lab.fit_transform(fish['Species'])

fish

# Here, i'm taking three variables to predict the weight.
# So this time our model can become more accurate.

x = fish[["Length3","Height", "Width","Species"]]
y = fish[["Weight"]]

x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=0.75,random_state= 2)

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

# So, here we can see that the r2 value is 0.798 that means my model became more accurate when i provided some more details.
# In simple linear regression when i gave single variable as input i got 0.72 accuracy model and here i can see that value gone to 0.79.
# Model became more accurate using multiple lineae regression.

metrics.r2_score(y_test, y_pred)

model.coef_

model.intercept_

import pickle

pickle.dump(model,open("/workspaces/79278298/project/weight.pk","wb"))

model = pickle.load(open("weight.pk","rb"))