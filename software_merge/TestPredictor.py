# Import required libraries:
import datetime
import warnings
import pandas as pd
import numpy as np
warnings.filterwarnings("ignore",category=DeprecationWarning)
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import r2_score
from dbms_connection import * 

def createModel(angle):
    # Read the CSV file:
    filename = extract_data()
    data = pd.read_csv(r"%s" % filename)
    #data = pd.read_csv(r"FakeDataSet.csv")
    data.head()
    
    data = data[["time", angle]]
    print(data)
    
    # Generating training and testing data from our data:
    # We are using 80% data for training.
    train = data[:(int((len(data) * 0.8)))]
    test = data[(int((len(data) * 0.8))):]
    
    # Modeling:
    # Using sklearn package to model data:
    regr = linear_model.LinearRegression()
    train_x = np.array(train[["time"]])
    train_y = np.array(train[[angle]])
    regr.fit(train_x, train_y)
    
    # The slope and intercept:
    print("slope: %.2f" % regr.coef_[0][0])
    print("intercept: %.2f" % regr.intercept_[0])
    
    # Plotting the regression line:
#    plt.scatter(data["Time"], data[angle], color = "blue")
#    plt.plot(train_x, regr.coef_ * train_x + regr.intercept_, '-r')
#    plt.xlabel("Time")
#    plt.ylabel(angle)
#    plt.show()
    
    # Checking various accuracy:
    actual_test_x = np.array(test[['time']])
    actual_test_y = np.array(test[[angle]])
    predicted_test_y = regr.predict(actual_test_x)
    
    print("Mean absolute error: %.2f" % np.mean(np.absolute(predicted_test_y - actual_test_y)))
    print("Mean sum of squares (MSE): %.2f" % np.mean((predicted_test_y - actual_test_y) ** 2))
    print("R2-score: %.2f" % r2_score(predicted_test_y, actual_test_y))
    
    return regr.coef_, regr.intercept_

# Predicting position of current time:
def getEstimatedAngle(slope, intercept):
    getCurrentTime = datetime.datetime.now().time()
    currentTime = getCurrentTime.strftime("%H:%M:%S")
    print("Current time:", currentTime)
    (hour, minute, second) = currentTime.split(':')
    currentTimeDecimal = float(hour) + (float(minute)/60) + (float(second)/3600)
    print("Current time as decimal: %.2f" % currentTimeDecimal)
    
    estimatedAngle = currentTimeDecimal * slope[0][0] + intercept[0]
    print("Estimated angle: %.2f" % estimatedAngle)
    
    return estimatedAngle

# Function calls
#print("Time vs Latitude Angle:")
#slope1, intercept1 = createModel("latitude")
#getEstimatedAngle(slope1, intercept1)
#print(" ")
#print("Time vs Longitude Angle:")
#slope2, intercept2 = createModel("Longitude Angle")
#getEstimatedAngle(slope2, intercept2)
