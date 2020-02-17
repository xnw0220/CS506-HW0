# 5. Dataset split

# (a) Write a function that gets as input the fraction of the dataset that
# will be used as the test set and randomly splits the dataset into
# train and test sets.
import numpy as np
def train_test_split(X, y, t_f):
    X_shuffle = []
    y_shuffle = []
    
    indices = list(range(len(X)))
    np.random.shuffle(indices)
    for i in indices:
        X_shuffle.append(X[i])
        y_shuffle.append(y[i])

    num_of_rows = int(len(X) * (1 - t_f))
    X_train = X_shuffle[:num_of_rows]
    y_train = y_shuffle[:num_of_rows]
    X_test = X_shuffle[num_of_rows:]
    y_test = y_shuffle[num_of_rows:]

    return X_train, y_train, X_test, y_test


# (b) Write a function which divides the data set into three sections,
# including test, train, and cross validation sets.
def train_test_CV_split(X, y, t_f, cv_f):
    X_shuffle = []
    y_shuffle = []
    
    indices = list(range(len(X)))
    np.random.shuffle(indices)
    for i in indices:
        X_shuffle.append(X[i])
        y_shuffle.append(y[i])

    num_of_rows_t = int(len(X) * (1 - t_f - cv_f))
    num_of_rows_cv = int(len(X) * (1 - t_f))
    X_train = X_shuffle[:num_of_rows_t]
    y_train = y_shuffle[:num_of_rows_t]
    X_cv = X_shuffle[num_of_rows_t:num_of_rows_cv]
    y_cv = y_shuffle[num_of_rows_t:num_of_rows_cv]
    X_test = X_shuffle[num_of_rows_cv:]
    y_test = y_shuffle[num_of_rows_cv:]
    
    return X_train, y_train, X_test, y_test, X_cv, y_cv
