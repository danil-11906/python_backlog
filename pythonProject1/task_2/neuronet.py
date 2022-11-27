import pandas
from keras.callbacks import LambdaCallback
from keras.models import Sequential
from keras.layers import Dense
from keras import activations


class NeuroNetwork:
    def __init__(self):
        self.__epochs = 1
        self.__weights = []
        self.__min_loss = 1000000.0
        self.__x = pandas.read_csv('csv/xdata.csv', delimiter=';').to_numpy()
        self.__y = pandas.read_csv('csv/ydata04.csv', delimiter=';').to_numpy()

        self.__model = Sequential()
        self.__model.add(Dense(2, input_shape=(2,), activation=activations.sigmoid, name='first'))
        self.__model.add(Dense(3, activation=activations.sigmoid, name='second'))
        self.__model.add(Dense(1, activation=activations.sigmoid, name='last'))

        self.__model.compile(loss='mse', optimizer='adam')

    def __compare_data(self, epoch, logs):
        loss = logs['loss']
        if loss < self.__min_loss:
            self.__min_loss = loss
            self.__weights = [
                self.__model.layers[0].get_weights()[0],
                self.__model.layers[1].get_weights()[0],
                self.__model.layers[2].get_weights()[0],
            ]

    def solve_task(self):
        callback = LambdaCallback(
            on_epoch_end=lambda epoch, logs: self.__compare_data(epoch, logs)
        )
        self.__model.fit(self.__x, self.__y, epochs=self.__epochs, batch_size=1, callbacks=[callback])

        return self.__min_loss, self.__weights
