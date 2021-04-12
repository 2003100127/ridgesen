# RidgeSen
![](https://img.shields.io/badge/RidgeSen-executable-519dd9.svg)
![](https://img.shields.io/badge/last_released_date-April._2021-green.svg)

###### tags: `Ridge regression` `Sensitivity analysis` `Econometric modeling` `Sensitive industries`

## Overview
RidgeSen is a repository for the methodological analysis of the Beijing economy sensitivity of nine industries to the changes of meteorological factors based on the ridge regression method that was proposed [here](https://www.tandfonline.com/doi/abs/10.1080/00401706.1970.10488634) to estimate the parameters of a regression analysis problem from observations in which independent variables are highly correlated (Please refer to [wiki Ridge regression](https://en.wikipedia.org/wiki/Ridge_regression)). 

I implemented this ridge regression method by estimating parameters of the ridge regression estimator (RRE) ([Yazid M, 2010](https://www.sciencedirect.com/science/article/pii/S1815385210000076)) using the least squares estimator (LSE). Based on Beijing meteorological and economic observations from 2002-2013, we then used this method to analyze the economy sensitivity of Beijing nine industries to the changes of meteorological factors. According to the sensitivity values, among 9 industries the economy of the construction industry was found to be most sensitive to the changes of meteorological factors. This is in accordance with specific circumstances of Beijing's industries. In our paper (please see below), we specifically analyzed how and why some industry economies are very sensitive while some are not. The sensitivity analysis is helpful to decision-making departments w.r.t. industrial shake-up and resource allocation and etc.

## Install
```    
pip install -r requirements.txt
```

## Usage
Please run our program in `./example/ridge_regression_analysis.ipynb`. 

## Cite our work
For Chinese version,
孙鉴锋, 王冀, 何桂梅, 陈志泊, 王建新. 北京市行业经济产出对气象变化的敏感性分析. ***资源科学***，2017，39(6):1212-1223. DOI: [https://doi.org/10.18402/resci.2017.06.20](http://www.resci.cn/EN/10.18402/resci.2017.06.20)

For English version,
**Jianfeng Sun**, Ji Wang, Guimei He, Zhibo Chen, and Jianxin Wang. Sensitivity analyses of industrial economic output to weather variability in Beijing. ***Resources Science***, 39(6):1212-1223, 2017. DOI: [http://www.resci.cn/EN/10.18402/resci.2017.06.20](http://www.resci.cn/EN/10.18402/resci.2017.06.20).

or

```c=
@article{sun2017,
    title={北京市行业经济产出对气象变化的敏感性分析},
    author={孙鉴锋，王冀，何桂梅，陈志泊，王建新},
    journal={资源科学},
    year={2017},
    volume={39},
    number={6},
    eid={1212},
    numpages={11},
    pages={1212},
    url={http://www.resci.cn/CN/abstract/article_41276.shtml},
    doi={10.18402/resci.2017.06.20},
}

or

@article{sun2017,
    title={Sensitivity analyses of industrial economic output to weather variability in \uppercase{B}eijing},
    author={Jianfeng Sun and Ji Wang and Guimei He and Zhibo Chen and Jianxin Wang},
    journal={Resources Science},
    year={2017},
    volume={39},
    number={6},
    eid={1212},
    numpages={11},
    pages={1212},
    url={http://www.resci.cn/EN/10.18402/resci.2017.06.20},
    doi={10.18402/resci.2017.06.20},
}
```

## Contact
If you have any question, please contact [Jianfeng Sun](mailto:jianfeng.sunmt@gmail.com/jianfeng.sun@tum.de). We highly recommend creating [issue](https://github.com/2003100127/deeptminter/issues) pages when you have problems. Your issues will subsequently be responded.  