import pandas as pd 
import numpy as np 
from scipy.stats import wilcoxon 
 
chat_id = 694905952 # Ваш chat ID, не меняйте название переменной
 
def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия 
    alpha = 0.03 
    pvalue = wilcoxon(x, y, alternative="less", method='exact', zero_method = 'zsplit').pvalue 
     
    return pvalue < alpha
