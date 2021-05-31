import pandas as pd

from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from tensorflow.python.keras.utils.vis_utils import plot_model
from sklearn.model_selection import train_test_split
import pydot
import graphviz
import pydotplus

class model_class():
    def __init__(self , mod_type , mod_lay, mod_layer_data,epochs):
        self.model_type = mod_type
        self.model_layers = mod_lay
        self.model_data = mod_layer_data
        self.epochs = epochs


    def model_create(self):
        model_self = Sequential()
        length = int(self.model_layers) - 1
        
        for i in range(length):
            print(self.model_data[i][0])
            act = str(self.model_data[i][2])
            if i == 0:
                model_self.add(Dense(int(self.model_data[i][0]),input_dim=int(self.model_data[i][1]),activation=act))
            else:
                model_self.add(Dense(int(self.model_data[i][0]),activation=act))

        model_self.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        return model_self

    def model_run(self,path,target_Y):
        pre_model = self.model_create()
        csv_file = pd.read_csv(path)
        X_data = csv_file.drop(target_Y,axis=1)
        Y_data = csv_file[target_Y]
        X_data = X_data.drop('Date' , axis=1)
        X_train,X_test,y_train,y_test = train_test_split(X_data,Y_data,test_size=0.2)
        pre_model.fit(X_train,y_train,epochs=int(self.epochs),batch_size=10)
        plot_model(pre_model,to_file="result.png",show_shapes=True,show_layer_names=True)



