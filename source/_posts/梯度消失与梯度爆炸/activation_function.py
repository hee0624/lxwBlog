#!/usr/bin/env python3
# coding: utf-8
# File: activation_function.py
# Author: lxw
# Date: 3/21/18 3:47 PM

import matplotlib.pyplot as plt
import numpy as np
import math


def activation_function_and_derivative():
    def sigmoid(x):
        y = []
        for item in x:
            y.append(1 / (1 + math.exp(-item)))
        return y

    def sigmoid_derivative(x):
        y = []
        for item in x:
            e_x = math.exp(-item)
            y.append(e_x / ((1 + e_x) ** 2))
        return y


    x = np.arange(-10, 10, 0.1)    # arange(起点, 终点, 间隔). linspace(起点, 终点, 点个数)
    y = sigmoid(x)
    plt.subplot(321)
    plt.plot(x, y, label="sigmoid(x)")
    plt.legend()

    y = sigmoid_derivative(x)
    plt.subplot(322)
    plt.plot(x, y, label="sigmoid'(x)")
    plt.legend()

    def tanh(x):
        y = []
        for item in x:
            ex = math.exp(item)
            e_x = math.exp(-item)
            y.append((ex - e_x) / (ex + e_x))
        return y

    def tanh_derivative(x):
        y = []
        for item in x:
            ex = math.exp(item)
            e_x = math.exp(-item)
            # y.append(1 - ((ex - e_x) ** 2) / ((ex + e_x) ** 2))
            y.append(4 / ((ex + e_x) ** 2))
        return y

    y = tanh(x)
    plt.subplot(323)
    plt.plot(x, y, label="tanh(x)")
    plt.legend()

    y = tanh_derivative(x)
    plt.subplot(324)
    plt.plot(x, y, label="tanh'(x)")
    plt.legend()

    def relu(x):
        y = []
        for item in x:
            if item < 0:
                y.append(0)
            else:
                y.append(item)
        return y

    def relu_derivative(x):
        y = []
        for item in x:
            if item < 0:
                y.append(0)
            else:
                y.append(1)
        return y

    y = relu(x)
    plt.subplot(325)
    plt.plot(x, y, label="relu(x)")
    plt.legend()

    y = relu_derivative(x)
    plt.subplot(326)
    plt.plot(x, y, label="relu'(x)")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    activation_function_and_derivative()
