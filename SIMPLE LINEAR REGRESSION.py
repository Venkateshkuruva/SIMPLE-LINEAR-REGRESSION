
import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

dataset = pd.read_csv(r"C:\Users\Asus.LAPTOP-EMBE8J7O\Downloads\Salary_Data\Salary_Data.csv")


x = dataset.iloc[:,:-1]

y = dataset.iloc[:,-1]

from sklearn.model_selection import train_test_split

x_train, x_test,y_train,y_test = train_test_split(x, y, test_size=0.20, random_state=0)

x_train = x_train.values.reshape(-1,1)

x_test = x_test.values.reshape(-1, 1)

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test) 

plt.scatter(x_test, y_test, color = 'red')  

plt.plot(x_train, regressor.predict(x_train), color = 'blue')  

plt.title('Salary vs Experience (Test set)')

plt.xlabel('Years of Experience')

plt.ylabel('Salary')

plt.show()
