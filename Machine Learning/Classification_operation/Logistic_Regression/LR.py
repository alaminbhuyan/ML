from sklearn import datasets
from sklearn.linear_model import LogisticRegression

iris = datasets.load_iris()

featurs = iris.data
label = iris.target

model = LogisticRegression()
model.fit(featurs,label)
predicted_value = model.predict([[1,1,1,1]])
print(predicted_value)
