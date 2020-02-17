import numpy as np
import math

# impute missing entries
def impute_missing(X):
    for ls in X[0:2]:
        n = len(ls)
        sorted_ls = sorted(ls, key=lambda x: x if not math.isnan(x) else 0)
        
        if n % 2 == 0:
            median1 = sorted_ls[n//2]
            median2 = sorted_ls[n//2 - 1]
            median = (median1 + median2) / 2
        else:
            median = sorted_ls[n//2]

        for val in ls:
            if math.isnan(val):
                ls[ls.index(val)] = median
            
    return X


# discard missing entries
def discard_missing(X, y):
    X_copy = X.copy()
    
    for ls in X_copy:
        for val in ls:
            if math.isnan(val):
                y.pop(X.index(ls))
                X.remove(ls)
                break

    return X, y

        
