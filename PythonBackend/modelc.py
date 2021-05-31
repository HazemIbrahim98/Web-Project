import pandas as pd

from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from tensorflow.python.keras.utils.vis_utils import plot_model
from sklearn.model_selection import train_test_split


class model_class():
    def __init__(self, mod_type, mod_lay, mod_layer_data, epochs):
        self.model_type = mod_type
        self.model_layers = mod_lay
        self.model_data = mod_layer_data
        self.epochs = epochs

    def model_create(self, dimension):
        model_self = Sequential()
        length = int(self.model_layers) - 1

        for i in range(length):
            print(self.model_data[i][0])
            print("                                     ")

            act = str(self.model_data[i][1])
            if i == 0:
                model_self.add(
                    Dense(int(self.model_data[i][0]), input_dim=dimension, activation=act))
            else:
                model_self.add(
                    Dense(int(self.model_data[i][0]), activation=act))

        model_self.compile(loss='binary_crossentropy',
                           optimizer='adam', metrics=['accuracy'])
        return model_self

    def model_run(self, path, outputPATH, target_Y):
        csv_file = pd.read_csv(path)
        X_data = csv_file.drop(target_Y, axis=1)
        Y_data = csv_file[csv_file.columns[-1]]
        X_data = X_data.drop('Date', axis=1)

        print(len(X_data.columns))
        print("<br>")

        pre_model = self.model_create(len(X_data.columns))
        X_train, X_test, y_train, y_test = train_test_split(
            X_data, Y_data, test_size=0.2)

        pre_model.fit(X_train, y_train, epochs=int(
            self.epochs), batch_size=10, verbose=0)
        plot_model(pre_model, to_file=outputPATH,
                   show_shapes=True, show_layer_names=True)
