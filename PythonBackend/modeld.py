from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pydot


class modeld_class():
    def __init__(self):
        self.max_depth = None
        self.max_features = None
        self.max_leaf_nodes = None

    def model_create(self):
        model_self = DecisionTreeClassifier(
            max_depth=self.max_depth, max_features=self.max_features, max_leaf_nodes=self.max_leaf_nodes)
        return model_self

    def model_run(self, path):
        model = self.model_create()
        csv_file = pd.read_csv(path + 'DATASET.csv')
        Y_data = csv_file[csv_file.columns[-1]]
        X_data = csv_file.iloc[:, :-1]

        #X_data = X_data.drop('Date', axis=1)

        X_train, X_test, y_train, y_test = train_test_split(
            X_data, Y_data, test_size=0.2)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        print("Accuracy: ", metrics.accuracy_score(y_test, y_pred))
        tree.export_graphviz(model, out_file=path + "result.dot")
        (graph, ) = pydot.graph_from_dot_file(path + "result.dot")
        graph.write_png(path + "result.png")
