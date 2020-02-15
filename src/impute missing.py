import numpy as np
import math

def import_data(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        X = [[] for _ in range(len(lines))]
        y = [[] for _ in range(len(lines))]
        
        for i in range(0, 2):
            replace = lines[i].replace("?", str(np.nan))
            line = replace.strip().split(",")
            
            for item in line[:279]:
                if item == str(np.nan):
                    X[i].append(float(item))
                else:
                    X[i].append(eval(item))
                    
            y[i].append(eval(line[279]))

    return X,y

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
        
