from point import P3
import math
import matplotlib.pyplot as plt
import numpy as np


class LogisticRegression:

    @staticmethod
    def z(w0, w1, w2, x, y):
        return w0 + w1 * x + w2 * y

    def minimization_function(self, parameters):
        sum1 = 0
        sum2 = 0

        w0 = parameters.x
        w1 = parameters.y
        w2 = parameters.z

        for p in self.points:
            if p.class_number == 0:
                sum1 += math.log(1 + math.e ** (-self.z(w0, w1, w2, p.x, p.y)))
            else:
                sum2 += math.log(1 + math.e ** (self.z(w0, w1, w2, p.x, p.y)))

        return sum1 + sum2

    def gradient_next_step(self, current_step):
        next_step = P3()
        for p in self.points:
            if p.class_number == 0:
                next_step.x += -math.e ** (-self.z(current_step.x, current_step.y, current_step.z, p.x, p.y)) / \
                               (1 + math.e ** (-self.z(current_step.x, current_step.y, current_step.z, p.x, p.y)))
                next_step.y += (-p.x * math.e ** (-self.z(current_step.x, current_step.y, current_step.z, p.x, p.y))) / \
                               (1 + math.e ** (-self.z(current_step.x, current_step.y, current_step.z, p.x, p.y)))

                next_step.z += (-p.y * math.e ** (-self.z(current_step.x, current_step.y, current_step.z, p.x, p.y))) / \
                               (1 + math.e ** (-self.z(current_step.x, current_step.y, current_step.z, p.x, p.y)))

            else:
                next_step.x += math.e ** (self.z(current_step.x, current_step.y, current_step.z, p.x, p.y)) / \
                               (1 + math.e ** (self.z(current_step.x, current_step.y, current_step.z, p.x, p.y)))

                next_step.y += (p.x * math.e ** (self.z(current_step.x, current_step.y, current_step.z, p.x, p.y))) / \
                               (1 + math.e ** (self.z(current_step.x, current_step.y, current_step.z, p.x, p.y)))

                next_step.z += (p.y * math.e ** (self.z(current_step.x, current_step.y, current_step.z, p.x, p.y))) / \
                               (1 + math.e ** (self.z(current_step.x, current_step.y, current_step.z, p.x, p.y)))

        return next_step

    def __init__(self, points):
        self.points = points
        self.w0 = 0
        self.w1 = 0
        self.w2 = 0

    def calculate(self, debug=False):

        gradient_current_step = P3(-2, -2, -2)

        while True:

            gradient_last_step = gradient_current_step.__copy__()

            multiplier = 0.001
            gradient_current_step = gradient_current_step - self.gradient_next_step(gradient_last_step).multiply(multiplier)

            if debug:
                print("Current step: " + str(gradient_current_step))
                print("Last step: " + str(gradient_last_step))
                print("Gradient distance: " + str(
                    math.fabs(gradient_current_step.calculate_distance_to_point(gradient_last_step))))
                print("Function distance: " + str(math.fabs(
                    self.minimization_function(gradient_current_step) - self.minimization_function(gradient_last_step))))
                print("Minimization function value: " + str(self.minimization_function(gradient_current_step)))
                print('\n')

            if math.fabs(gradient_current_step.calculate_distance_to_point(gradient_last_step)) < 0.0001 or \
                    math.fabs(self.minimization_function(gradient_current_step) - self.minimization_function(
                        gradient_last_step)) < 0.0001:
                self.w0 = gradient_current_step.x
                self.w1 = gradient_current_step.y
                self.w2 = gradient_current_step.z

                x = np.arange(-0.25, 1.25, 0.005)
                plt.plot(x, (-self.w1 * x - self.w0) / self.w2, c='r')

                return

    def p(self, point, class_number):
        if class_number == 0:
            return 1 / (1 + math.e ** -self.z(self.w0, self.w1, self.w2, point.x, point.y))
        else:
            return 1 - self.p(point, 0)
