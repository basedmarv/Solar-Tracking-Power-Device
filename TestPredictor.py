# Import required libraries:
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

# Read the CSV file :
data = pd.read_csv(r"C:\Users\quiam\Documents\EECS 159A\FakeDataSet.csv")
data.head()

# Let’s select some features to explore more:
data = data[["TIME", "POSITION"]]

# ENGINESIZE vs CO2EMISSIONS:
plt.scatter(data["TIME"], data["POSITION"], color = "blue")
plt.xlabel("TIME")
plt.ylabel("POSITION")
plt.show()

# Generating training and testing data from our data:
# We are using 80% data for training.
train = data[:(int((len(data) * 0.8)))]
test = data[(int((len(data) * 0.8))):]

# Modeling:
# Using sklearn package to model data:
regr = linear_model.LinearRegression()
train_x = np.array(train[["TIME"]])
train_y = np.array(train[["POSITION"]])
regr.fit(train_x, train_y)

# The coefficients:
print("coefficients:", regr.coef_)
print("intercept:", regr.intercept_)

# Plotting the regression line:
plt.scatter(data["TIME"], data["POSITION"], color = "blue")
plt.plot(train_x, regr.coef_ * train_x + regr.intercept_, '-r')
plt.xlabel("Time")
plt.ylabel("Position")

# Predicting values:
# Function for predicting future values:
def get_regression_predictions(input_features, intercept, slope):
    predicted_values = input_features * slope + intercept
    
    return predicted_values
 
# Predicting position of current time:
get_current_time = datetime.datetime.now().time()
t = get_current_time.strftime("%H:%M:%S")
print("Current time:", t)
(hour, minute, second) = t.split(':')
current_time = int(hour) + (int(minute)/60) + (int(second)/3600)
print("Current time as decimal:", current_time)

estimated_position = get_regression_predictions(current_time, regr.intercept_[0], regr.coef_[0][0])
print("Estimated position:", estimated_position)

# Checking various accuracy:
from sklearn.metrics import r2_score

test_x = np.array(test[['TIME']])
test_y = np.array(test[['POSITION']])
test_y_ = regr.predict(test_x)

print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_ - test_y)))
print("Mean sum of squares (MSE): %.2f" % np.mean((test_y_ - test_y) ** 2))
print("R2-score: %.2f" % r2_score(test_y_, test_y))
