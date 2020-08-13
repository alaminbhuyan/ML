import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
#%%
df = pd.read_csv("UCI_Credit_Card.csv")
print(df.head(10))
print(df.shape)
df.iloc[[2,3],[5]] = np.nan

# handle the null value
#%%
print(df.isnull().sum())
fillnan = df.AGE.mean()
print(fillnan)
#%%
df.AGE = df.AGE.fillna(fillnan)
#%%
# divide features and label
featurs = df.drop(columns="target")
print(featurs)
label = df['target']
print(label)
#%%
xtrain,xtest,ytrain,ytest = train_test_split(featurs,label,test_size=.25,random_state=1)
#%%
# make svm model
model = SVC(gamma='auto')
model.fit(xtrain,ytrain)
print(model.score(xtest,ytest))
#%%
rand_cls = RandomForestClassifier()
rand_cls.fit(xtrain,ytrain)
print(rand_cls.score(xtest,ytest))
#%%
desicion_cls = DecisionTreeClassifier()
desicion_cls.fit(xtrain,ytrain)
print(desicion_cls.score(xtest,ytest))