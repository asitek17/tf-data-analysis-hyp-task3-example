import pandas as pd 
import numpy as np 
from scipy.stats import ks_2samp
 
 
chat_id = 694905952 # Ваш chat ID, не меняйте название переменной
 
def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия 
    alpha = 0.03 
    pvalue = ks_2samp(x, y, alternative='less').pvalue 
     
    return pvalue < alpha
