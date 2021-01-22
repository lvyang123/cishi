#encoding=UTF-8
import numpy as np
import tensorflow
import matplotlib.pyplot as plt
from scipy.integrate import quad, dblquad
def qiujifen(xiaxian, shangxian):
    var, err = quad(lambda x: 2*np.exp(2)*np.sin(2*x)*np.cos(x),
    xiaxian,
    shangxian)
    print('积分结果：', var)


if __name__ == '__main__':
    qiujifen(-1, 2)
    x = np.linspace(0, 3, 200)
    e_x = np.exp(x)
    plt.plot(x, e_x)
    plt.show()