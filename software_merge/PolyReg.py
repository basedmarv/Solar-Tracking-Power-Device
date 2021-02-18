import datetime
import warnings
import pandas as pd
import numpy as np
warnings.filterwarnings("ignore",category=DeprecationWarning) 
import matplotlib.pyplot as plt
from dbms_connection import *

def createPolyModel(angle):
    # Read the CSV file:
    filename = extract_data()
    data = pd.read_csv(r"%s" % filename)
    data.head()
    
    data = data[["time", angle]]
    
    plt.scatter(data["time"], data[angle], color = "blue")
    plt.xlabel("time")
    plt.ylabel(angle)
    plt.show()
    
    x = np.array(data["time"])
    y = np.array(data[angle])
    
    n = len(x)
    
    # Make polynomial data:
    x1 = x
    x2 = np.power(x1,2)
    x3 = np.power(x1,3)
    
    # Reshaping data:
    x1_new = np.reshape(x1,(n,1))
    x2_new = np.reshape(x2,(n,1))
    x3_new = np.reshape(x3,(n,1))
    
    # First column of matrix X:
    x_bias = np.ones((n,1))
    
    # Form the complete x matrix:
    x_new = np.append(x_bias,x1_new,axis=1)
    x_new = np.append(x_new,x2_new,axis=1)
    x_new = np.append(x_new,x3_new,axis=1)
    
    # Finding transpose:
    x_new_transpose = np.transpose(x_new)
    
    # Finding dot product of original and transposed matrix :
    x_new_transpose_dot_x_new = x_new_transpose.dot(x_new)
    
    # Finding Inverse:
    temp_1 = np.linalg.inv(x_new_transpose_dot_x_new)# Finding the dot product of transposed x and y :
    temp_2 = x_new_transpose.dot(y)
    
    # Finding coefficients:
    theta = temp_1.dot(temp_2)
    
    # Store coefficient values in different variables:
    beta_0 = theta[0]
    beta_1 = theta[1]
    beta_2 = theta[2]
    beta_3 = theta[3]
    
    # Prediction function:
    y_pred = beta_0 + beta_1*x1 + beta_2*x2 + beta_3*x3
    #print("Prediction:", y_pred)
    
    # Calculate accuracy of model:
    var = (y - y_pred)
    var = var*var
    n = len(var)
    MSE = var.sum()
    MSE = MSE/n
    #print("Error:", MSE)
    
    # Plot the polynomial curve:
    plt.scatter(x,y)
    plt.plot(x, y_pred, c="red")
    
    return y_pred, len(x)
    
def getPolyEstimatedAngle(model, length):
    now = datetime.datetime.now()
    hour = now.hour
    
    if(now.minute > 15 and now.minute <= 30):
        minute = 0.25
    elif(now.minute > 30 and now.minute <= 45):
        minute = 0.50
    elif(now.minute > 45 and now.minute <= 60):
        minute = 0.75
    else:
        minute = 0
    
    currentTimeDecimal = hour + minute
    print("Current time as decimal:", currentTimeDecimal)
    
    if(currentTimeDecimal < 8):
        estimatedAngle = model[0]
    elif(currentTimeDecimal > 17):
        estimatedAngle = model[length - 1]
    else:
        index = currentTimeDecimal * 4 - 32
        estimatedAngle = model[index]
    
    print("Estimated angle:", estimatedAngle)
    
    return estimatedAngle

#model, length = createPolyModel("latitude")
#getPolyEstimatedAngle(model, length)
