import sklearn
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
import graphviz
import pydot

class modeld_class():
    def __init__(self):
        self.max_depth = None
        self.max_features =  None
        self.max_leaf_nodes =  None
        

    def model_create(self):
        model_self = DecisionTreeClassifier(max_depth=self.max_depth, max_features=self.max_features,max_leaf_nodes=self.max_leaf_nodes)
        return model_self

    def model_run(self, path, target_Y):
        model = self.model_create()
        csv_file = pd.read_csv(path)
        X_data = csv_file.drop(target_Y, axis=1)
        Y_data = csv_file[csv_file.columns[-1]]
        X_data = X_data.drop('Date', axis=1)
        try:
            X_train, X_test, y_train, y_test = train_test_split(
                X_data, Y_data, test_size=0.2)
            model.fit(X_train,y_train)
            tree.export_graphviz(model,out_file="tree.dot")
            (graph, ) = pydot.graph_from_dot_file("tree.dot")
            graph.write_png("tree.png")
        
        except Exception as e:
            print(e)

        
