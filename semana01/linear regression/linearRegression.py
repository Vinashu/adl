#Linear Regression Quiz
#In this quiz, you'll be working with data on the average life expectancy at birth and the average the BMI for males across the world. The data comes from Gapminder.

#The data file can be found under the "bmi_and_life_expectancy.csv" tab in the quiz below. The data includes the country the person was born in. This data is under the "Country" column. The Life expectancy for a person in that country in the "Life expectancy" column. The media BMI of a child born in that country as "BMI". You'll predict the life expectancy using this BMI.

#You'll need to complete each of the following steps:
#1. Load the data

#The data is in the file called "bmi_and_life_expectancy.csv".
#Use pandas read_csv to load the data into a dataframe.
#Assign the dataframe to the variable bmi_life_data.
#2. Build a linear regression model

#Create a regression model using scikit-learn's LinearRegression and assign it to bmi_life_model.
#Fit the model to the data.
#3. Predict using the model

#Predict using a BMI of 21.07931 and assign it to the variable laos_life_exp.

# TODO: Add import statements
import pandas as pd
from sklearn.linear_model import LinearRegression

# Assign the dataframe to this variable.
# TODO: Load the data
bmi_life_data = pd.read_csv("bmi_and_life_expectancy.csv")

# Make and fit the linear regression model
#TODO: Fit the model and Assign it to bmi_life_model
bmi_life_model = LinearRegression()
bmi_life_model.fit(bmi_life_data[['BMI']], bmi_life_data[['Life expectancy']])

# Mak a prediction using the model
# TODO: Predict life expectancy for a BMI value of 21.07931
laos_life_exp = bmi_life_model.predict(21.07931)