# Loading required module
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

# load iris
iris = datasets.load_iris()
# This is the label or class
# Iris-Setosa[0]
# Iris-Versicolour[1]
# Iris-Virginica[2]

# print(iris.DESCR)
# split featurs and label
featurs = iris.data
label = iris.target

# print(featurs[0],label[0])

# Traing the classifier
model = KNeighborsClassifier()
model.fit(featurs,label)
# predict the value
predict_class = model.predict([[1.5,1,5,1]])

if predict_class == [0]:
    print("Iris-Setosa")
elif predict_class == [1]:
    print("Iris-Versicolour")
elif predict_class == [2]:
    print("Iris-Virginica")