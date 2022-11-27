import math

import pandas


class ErrorCounter:
    def __init__(self, json_data):
        self.w11 = float(json_data['w11']),
        self.w12 = float(json_data['w12']),
        self.w21 = float(json_data['w21']),
        self.w22 = float(json_data['w22']),
        self.v11 = float(json_data['v11']),
        self.v12 = float(json_data['v12']),
        self.v13 = float(json_data['v13']),
        self.v21 = float(json_data['v21']),
        self.v22 = float(json_data['v22']),
        self.v23 = float(json_data['v23']),
        self.w1 = float(json_data['w1']),
        self.w2 = float(json_data['w2']),
        self.w3 = float(json_data['w3']),
        data = pandas.read_csv('csv/test_data_100.csv', delimiter=';').to_numpy()
        self.x1 = list(data[:, 0])
        self.x2 = list(data[:, 1])
        self.y = list(data[:, 2])

    @staticmethod
    def f(x):
        return 1 / (1 + math.exp(-x))

    def g(self, x1, x2):
        h11 = self.f(x1 * self.w11[0] + x2 * self.w21[0])
        h12 = self.f(x1 * self.w12[0] + x2 * self.w22[0])
        return self.f(self.f(h11 * self.v11[0] + h12 * self.v21[0]) * self.w1[0] + self.f(
            h11 * self.v12[0] + h12 * self.v22[0]) * self.w2[0] + self.f(h11 * self.v13[0] + h12 * self.v23[0]))

    def e(self):
        res = 0
        for i in range(0, 99):
            yt = self.g(self.x1[i], self.x2[i])
            res += (yt - self.y[i]) * (yt - self.y[i])
        return res
