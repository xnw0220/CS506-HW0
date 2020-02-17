# 4. Working with non-numerical data

import numpy as np

def import_non_num_data(dataset):
    included_col = [0, 1, 2, 5, 6, 7, 8, 10, 12]
    
    with open(dataset, "r") as f:
        f.readline()
        lines = f.readlines()
        X = [[] for _ in range(len(lines))]
        y = [[] for _ in range(len(lines))]

        for i in range(len(lines)):
            line = lines[i].strip().split(",")
            line = [line[z] for z in included_col]

            if line[3] == 'male':
                line[3] = '1'
            else:
                line[3] = '0'

            if line[-1] == 'C':
                line[-1] = '0'
            elif line[-1] == 'Q':
                line[-1] = '1'
            else:
                line[-1] = '2'

            for j in range(len(line)):
                if line[j] == '':
                    line[j] = np.nan
                    X[i].append(float(line[j]))
                elif j == 1:
                    y[i].append(eval(line[j]))
                else:
                    X[i].append(eval(line[j]))

        return X, y
