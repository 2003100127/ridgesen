__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2021"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import numpy as np
import statsmodels.api as sm


class ridge(object):
    
    def customized(self, x, y, k):
        x_shape = np.array(x).shape
        x_mean = np.mean(x, axis=0)
        y_mean = np.mean(y, axis=0)
        x_std = np.std(x, axis=0, ddof=1)
        y_std = np.std(y, axis=0, ddof=1)
        X_mean = np.tile(x_mean, (x_shape[0], 1))
        X_std = np.tile(x_std, (x_shape[0], 1))
        Z = (x - X_mean) / X_std
        Y = (y - y_mean) / y_std
        alpha_init = np.eye(x_shape[1])
        pseudo_count = np.sqrt(k * (x_shape[0] - 1)) * alpha_init
        Zplus = np.concatenate((Z, pseudo_count), axis=0)
        Yplus = np.concatenate((Y, np.zeros(x_shape[1])), axis=0)
        model = sm.OLS(Yplus, Zplus)
        results = model.fit()
        r_square = results.rsquared
        f_stat = results.fvalue
        f_pvalue = results.f_pvalue
        err_var = results.mse_resid
        return results.params, r_square, f_stat, f_pvalue, err_var