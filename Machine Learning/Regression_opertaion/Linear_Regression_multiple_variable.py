#%%
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

#%%
df = pd.read_excel("Linear_Regression_multiple_variable.xlsx")
#df = pd.read_excel("D:\\MACHINE LEARNING\\Machine Learning\\CSV FILE\\Linear_Regression_multiple_variable.xlsx")
print(df)
#%%
print(df.isnull().sum())
#%%
# handling the null value
fill_value = df.experience.mean()
df.experience = df.experience.fillna(fill_value)
#%%
model = LinearRegression()
model.fit(df[['speed','car_age','experience']],df.risk)
#%%
print(model.coef_)
print(model.intercept_)
#%%
value = np.array(list(map(float,input("enter speed,car_age,experience: ").split())),ndmin=2)
predict_value = model.predict(value)
print("Predict risk is: ",*predict_value)