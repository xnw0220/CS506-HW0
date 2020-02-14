def import_data(filename):
    X = []
    y = []
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace("?", "NaN")
            line = line.strip().split(",")
            for item in line[:279]:
                if item == "NaN":
                    X.append(item)
                else:
                    X.append(eval(item))
            y.append([eval(val) for val in line[279:]])
            break

    return X,y
            
            
