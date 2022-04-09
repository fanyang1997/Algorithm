
# gradient decent using numpy
# w_theta_{t+1} = w_theta_t - gradient_decent_rate * gradient_t
# gradient_t = (1/m) * sum(h(x_i) - y_i) * x_i
# h(x) = theta_0 * x_0 + theta_1 * x_1 + theta_2 * x_2 + ... + theta_n * x_n

import numpy as np

def linear_model(x, theta):
    return np.dot(x, theta)

def gradient_decent(x, y, theta, gradient_decent_rate, iterations):
    m = len(y)
    for i in range(iterations):
        gradient = (1/m) * np.dot(x.T, linear_model(x, theta) - y)
        theta = theta - gradient_decent_rate * gradient
    return theta
