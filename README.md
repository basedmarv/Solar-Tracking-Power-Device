# Solar Tracking Power Device

This repository is a compilation of the software used for our senior design project for the 2020-2021 school year. Our project is a Solar Tracking Power Device that uses machine learning to predict the optimal position/angle for the device to absorb the most solar energy. 

The high demand for renewable energy around the world is currently propelling the global Solar Tracker Market. What the Solar Tracking Power Device aims to accomplish is maximizing the solar energy input using machine learning, motors, and photovoltaic resistors to accurately align the solar panel of the device towards the sun regardless of the season.

## Methodology 

### Software 
* Incorporate Machine Learning by using gathered data to automatically predict the most optimal position and range of the tracker
* Properly implement methods that allows for accurate solar energy readings and utilize the gathered data to optimize the functionality of the solar tracker
### Hardware 
* Fabricate structural design of tracker similar to figure on the left
* Design and Solder circuit to read analog values on Raspberry Pi


## Built With

* [MCRP3008](https://github.com/Freenove/Freenove_Ultimate_Starter_Kit_for_Raspberry_Pi) - ADC Communication
* [Pandas](https://pandas.pydata.org/docs/user_guide/index.html) - Data Management for Machine Learning
* [dotenv](https://pypi.org/project/python-dotenv/) - Database Management System Data Encryption
* [Rpio.GPIO](https://pypi.org/project/RPi.GPIO/) - Raspberry Pi Software and Hardware Integration
* [MariaDB](https://mariadb.org/) - Data Storage

## Future Goals

* Replace photoresistors on each corner with Solar Panels so that the device can track unconcentrated light
* Develop a web application for the user
* Adjust the machine learning model for a more accurate representation of the sun’s location

## Authors:

### Software Team
* **Jayrell Quiambao** 
* **Roy Matthew Ramos**

### Hardware Team
* **Marvin Neil Sabas**
* **Michael Sanchez-Hernandez**

## Acknowledgments 
* [Professor Nader Bagherzadeh](https://engineering.uci.edu/users/nader-bagherzadeh)
* [Amber from Kookeye.com](https://kookye.com)
