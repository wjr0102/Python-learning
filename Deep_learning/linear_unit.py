#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2018-08-14 21:32:11
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2018-08-15 14:40:59

from perception import Perception
from matplotlib import pyplot as plt
import numpy as np

# Active function


#def f(x): return x
def f(x): return x


class LinearUnit(Perception):
    def __init__(self, input_num):
        Perception.__init__(self, input_num, f)


def get_training_dataset():
    input_vecs = [[5], [3], [8], [1.4], [10.1]]
    labels = [5500, 2300, 7600, 1800, 11400]
    return input_vecs, labels


def train_linear_unit():
    lu = LinearUnit(1)
    input_vecs, labels = get_training_dataset()
    lu.train(input_vecs, labels, 20, 0.01)
    return lu


if __name__ == '__main__':
    linearUnit = train_linear_unit()
    x = [5, 3, 8, 1.4, 10.1]
    y = [5500, 2300, 7600, 1800, 11400]
    plt.scatter(x, y)
    x = np.arange(0, 10, 0.1)
    # print type(x), type(linearUnit.weights[0]), type(linearUnit.bias)
    y = x * linearUnit.weights[0] + linearUnit.bias
    plt.plot(x, y)
    plt.show()
    print linearUnit
    print 'Work 3.4 years, monthly salary = %.2f' % linearUnit.predict([3.4])
    print 'Work 15 years, monthly salary = %.2f' % linearUnit.predict([15])
    print 'Work 1.5 years, monthly salary = %.2f' % linearUnit.predict([1.5])
    print 'Work 6.3 years, monthly salary = %.2f' % linearUnit.predict([6.3])
