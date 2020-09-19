import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#%%
df = pd.read_csv("D:\\MACHINE LEARNING\\Machine Learning\\CSV FILE\\data.csv")
print(df)
# split the area and price
x = df[['area']]
y = df['price']
# make test and train data
#%%
xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.3,random_state=1)
print(xtrain.head())
# make the regression obj
reg = LinearRegression()
reg.fit(xtrain,ytrain)
print(reg.score(xtest,ytest))

value = np.array(float(input("Enter a value: ")),ndmin=2)
predict_value = reg.predict(value)
print("Predicted value is: ",*predict_value)

plt.scatter(df['area'],df['price'],color="red")
plt.plot(df.area,reg.predict(df[['area']]))
plt.xlabel("Area")
plt.ylabel("Price")
plt.title("Regression Line")
plt.show()

