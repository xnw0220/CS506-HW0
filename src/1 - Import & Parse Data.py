import numpy as np

def import_data(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        X = [[] for _ in range(len(lines))]
        y = [[] for _ in range(len(lines))]
        
        for i in range(0, len(lines)):
            replace = lines[i].replace("?", str(np.nan))
            line = replace.strip().split(",")
            
            for item in line[:279]:
                if item == str(np.nan):
                    X[i].append(float(item))
                else:
                    X[i].append(eval(item))
                    
            y[i].append(eval(line[279]))

    return X,y
            
            
