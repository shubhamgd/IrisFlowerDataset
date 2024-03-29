from sklearn.datasets import load_iris
from sklearn import tree
import numpy as nu

iris = load_iris()

print("Feature names of iris data set")
print(iris.feature_names)

print("Target names of iris data set")
print(iris.target_names)

test_index = [1,51,101]

#training data with removed elements
train_target = np.delet(iris.target,test_index)
train_data = np.delete(iris.data,test_index,axis=0)

#testing data for testing on training data
test_target = iris.target[test_index]
test_data = iris.data[test_index]

#form a decision tree classifier
classifier = tree.DecisionTreeClassifier()

#apply training data to form tree
classifier.fit(train_data,train_target)

#for visualisation
from sklearn.externals.six import StringIO
import pydot

dot_data = StringIO()
tree.export_graphviz(classifier,out_file = dot_data,feature_names=iris.feature_names,
class_names=iris.target_names,filled=True,rounded=True,impurity=False)

graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph[0].write_pdf("Iris.pdf")