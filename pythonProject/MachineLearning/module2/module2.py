import pandas
import numpy as np


def logistic(x):
    return 1.0 / (1 + np.exp(-x))


def logistic_deriv(x):
    return logistic(x) * (1 - logistic(x))


LR = 1

I_dim = 2
H_dim = 2
T_dim = 3

epoch_count = 100

weights_ItoH = np.random.uniform(-1, 1, (I_dim, H_dim))
weights_HtoT = np.random.uniform(-1, 1, (H_dim, T_dim))
weights_TtoO = np.random.uniform(-1, 1, T_dim)

preActivation_H = np.zeros(H_dim)
postActivation_H = np.zeros(H_dim)

preActivation_T = np.zeros(T_dim)
postActivation_T = np.zeros(T_dim)

training_data = pandas.read_csv('xdata.csv', delimiter=';')
target_output = pandas.read_csv('ydata03.csv')
training_data = np.asarray(training_data)
target_output = np.array(target_output).ravel()
training_count = training_data.shape[0]

for epoch in range(epoch_count):
    for sample in range(training_count):

        for node in range(H_dim):
            preActivation_H[node] = np.dot(training_data[sample, :], weights_ItoH[:, node])
            postActivation_H[node] = logistic(preActivation_H[node])

        for node in range(T_dim):
            preActivation_T[node] = np.dot(postActivation_H, weights_HtoT[:, node])
            postActivation_T[node] = logistic(preActivation_T[node])

        preActivation_O = np.dot(postActivation_T, weights_TtoO)
        postActivation_O = logistic(preActivation_O)
        FE = postActivation_O - target_output[sample]

        for T_node in range(T_dim):
            S_error = FE * logistic_deriv(preActivation_O)
            gradient_TtoO = S_error * postActivation_T[T_node]

            for H_node in range(H_dim):
                value = postActivation_H[H_node]
                gradient_HtoT = S_error * weights_TtoO[T_node] * logistic_deriv(preActivation_T[T_node]) * value

                for I_node in range(I_dim):
                    input_value = training_data[sample, I_node]
                    gradient_ItoH = S_error * weights_HtoT[H_node, T_node] * logistic_deriv(
                        preActivation_H[H_node]) * input_value

                    weights_ItoH[I_node, H_node] -= LR * gradient_ItoH

                weights_HtoT[H_node, T_node] -= LR * gradient_HtoT

            weights_TtoO[T_node] -= LR * gradient_TtoO

error = 0
ss_tot = 0
avg = target_output.mean()

for sample in range(training_count):
    for node in range(H_dim):
        preActivation_H[node] = np.dot(training_data[sample, :], weights_ItoH[:, node])
        postActivation_H[node] = logistic(preActivation_H[node])

    for node in range(T_dim):
        preActivation_T[node] = np.dot(postActivation_H, weights_HtoT[:, node])
        postActivation_T[node] = logistic(preActivation_T[node])

    preActivation_O = np.dot(postActivation_T, weights_TtoO)
    postActivation_O = logistic(preActivation_O)
    error += (postActivation_O - target_output[sample]) ** 2
    ss_tot += (avg - target_output[sample]) ** 2

print('Error:')
print(error)
print('R^2:')
print(1 - error / ss_tot)
