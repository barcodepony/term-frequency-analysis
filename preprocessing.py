def bubbleSort(c, y):
    for value in range(len(c)-1,0,-1):
        for i in range(value):
            if c[i]<c[i+1]:
                temp = c[i]
                temp_y = y[i]
                c[i] = c[i+1]
                y[i] = y[i+1]
                c[i+1] = temp
                y[i+1] = temp_y
    return(c, y)

def preprocess(X, n, k):
    assert isinstance(X, list), "X needs to be a list of lists of strings"
    assert len(X) == n, "you gave a wrong length"
    assert isinstance(k, int), "k needs to be a integer and smaller or equal to shortest list"

    y = []  # list of text fragments
    c = []  # list of amounts

    for r in X:
        i = 0
        mi = len(r)-1
        while(i <= mi-(k-1)):
            fragment = r[i:i+k]
            if fragment in y:
                c_i = y.index(fragment)
                c[c_i] = c[c_i] + 1
            else:
                y.append(fragment)
                c.append(1)
            i = i + 1

    c, y = bubbleSort(c, y)
    return c, y



