#Programming Quiz: Multiple Linear Regression
#In this quiz, you'll be using the Boston house-prices dataset. The dataset consists of 13 features of 506 houses and their median value in $1000's. You'll fit a model on the 13 features to predict on the value of houses.

#You'll need to complete each of the following steps:

#1. Build a linear regression model

#Create a regression model using scikit-learn's LinearRegression and assign it to model.
#Fit the model to the data.
#2. Predict using the model

#Predict the value of sample_house.

from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston

# Load the data from the the boston house-prices dataset 
boston_data = load_boston()
x = boston_data['data']
y = boston_data['target']

# Make and fit the linear regression model
# TODO: Fit the model and Assign it to the model variable
model = LinearRegression()
model.fit(x, y)

# Mak a prediction using the model
sample_house = [[2.29690000e-01, 0.00000000e+00, 1.05900000e+01, 0.00000000e+00, 4.89000000e-01,
                6.32600000e+00, 5.25000000e+01, 4.35490000e+00, 4.00000000e+00, 2.77000000e+02,
                1.86000000e+01, 3.94870000e+02, 1.09700000e+01]]
# TODO: Predict housing price for the sample_house
prediction = model.predict(sample_house)