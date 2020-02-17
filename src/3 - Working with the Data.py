# 3. Working with the data

# Assume the input to all functions is reoresented as a matrix.

# (a) Create a function which shuffles the order of data entries.
import numpy as np
def shuffle_order(X):
    np.random.shuffle(X)
    return X


# (b) Create a function which calculates the standard deviation of each feature.
def stdev(X):
    all_std = []
    
    transpose = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]
    for ls in transpose:
        mean = sum(ls) / len(ls) 
        var = sum((x - mean)**2 for x in ls) / (len(ls) - 1)
        std = var**(1/2)
        all_std.append(std)
    
    return all_std


# (c) Create a function which removes all entries that contain a value which is
# more than two standard deviations away from the mean.
def remove_more_than_two_std(X):
    X_copy = X.copy()
    for ls in X_copy:
        for val in ls:
            if val < mean - 2*stdev(ls) or val > mean + 2*stdev(ls):
                X.remove(ls)
                break
            
    return X


# (d) Create a function which standardizes all the data points.
def standardize(X):
    all_mean = []
    std = stdev(X)
    
    transpose = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]
    for ls in transpose:
        mean = sum(ls) / len(ls)
        all_mean.append(mean)
        print(all_mean)

    for i in range(len(X)):
        for j in range(len(X[0])):
            X[i][j] = (X[i][j] - all_mean[j]) / std[j]

    return X
        
        
    

    
