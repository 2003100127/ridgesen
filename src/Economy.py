__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2021"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Ridge import ridge


class economy(object):

    def sensitivity(self, file_path, industry, step=0.005):
        data = pd.read_csv(
            file_path,
            sep='\s+',
            header=None,
        )
        x = data.loc[:, :5].values.tolist()
        y = data.loc[:, 6].values.tolist()
        coefs = []
        ridge_k = np.arange(0.1, 1, step)
        for k in ridge_k:
            params, _, _, _, _ = ridge().customized(x, y, k)
            coefs.append(params)
        ax = plt.gca()
        ax.plot(ridge_k, coefs)
        plt.xlabel('k choice')
        plt.ylabel(r'$\beta$ weight')
        plt.title(industry)
        plt.axis('tight')
        plt.show()
        return coefs

    def general(self, file_path, k=0.4):
        data = pd.read_csv(
            file_path,
            sep='\s+',
            header=None,
        )
        x = data.loc[:, :5].values.tolist()
        y = data.loc[:, 6].values.tolist()
        params, _, _, _, _ = ridge().customized(x, y, k)
        d = self.transform(x, y, params)
        return d

    def transform(self, x, y, params):
        ax = []
        x_shape = np.array(x).shape
        for i in range(x_shape[1]):
            s = 0
            for j in range(x_shape[0]):
                s = s + x[j][i]
            ax.append(s / x_shape[0])
        qx = []
        for i in range(x_shape[1]):
            qs = 0
            for j in range(x_shape[0]):
                qs = qs + pow((x[j][i] - ax[i]), 2)
            qx.append(pow(qs, 1 / 2))
        general = []
        for i in range(x_shape[1]):
            general.append(params[i] / qx[i])
        incept = np.mean(y) - np.dot(ax, general)
        return [incept] + general