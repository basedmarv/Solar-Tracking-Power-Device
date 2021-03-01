import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import datetime

def getAngle(angle):
    # Importing the dataset
    data = pd.read_csv(r"FakeDataSet.csv")
    data.head()
    
    data = data[["Time", angle]]
    
    x = np.array(data[["Time"]])
    y = np.array(data[[angle]])
    
    poly_reg = PolynomialFeatures(degree=3)
    x_poly = poly_reg.fit_transform(x)
    pol_reg = LinearRegression()
    pol_reg.fit(x_poly, y)
    
    plt.scatter(x, y, color='red')
    plt.plot(x, pol_reg.predict(poly_reg.fit_transform(x)), color='blue')
    plt.title('Latitude Angle vs Time')
    plt.xlabel('Time')
    plt.ylabel('Latitude Angle')
    plt.show()
    
    getCurrentTime = datetime.datetime.now().time()
    currentTime = getCurrentTime.strftime("%H:%M:%S")
    print("Current time:", currentTime)
    (hour, minute, second) = currentTime.split(':')
    currentTimeDecimal = int(hour) + (int(minute)/60) + (int(second)/3600)
    print("Current time as decimal:", currentTimeDecimal)
    
    estimatedAngle = float(pol_reg.predict(poly_reg.fit_transform([[currentTimeDecimal]])))
    print("Estimated angle:", estimatedAngle)
    
    return estimatedAngle

#getAngle("latitude")
