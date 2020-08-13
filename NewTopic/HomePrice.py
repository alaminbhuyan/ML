import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


df = pd.read_csv('CSV_FILES/homeprice.csv')
# print(df)
# print(df.head(3))

plt.scatter(df['area'],df['price'],marker='o',color='red')
plt.xlabel("Area",color='red')
plt.ylabel("Price",color='green')
# plt.show()

# divide the data into two parts

x = df[['area']]
y = df['price']

# Now make the test and train model
xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.3)
# print(xtrain)
# print()
# print(ytrain)
# print()
# print(xtest)
# print()
# print(ytest)

# Now train the data using LinearRegssion
reg = LinearRegression()
reg.fit(xtrain,ytrain)

# Now test the data
accuracy = reg.score(xtest,ytest)
print(accuracy)

plt.plot(df.area,reg.predict(df[['area']]))
plt.show()