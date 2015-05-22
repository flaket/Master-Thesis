def preprocess_data(d, n=128, m=255):
    l = len(d)
    data = [0] * n
    s = int(l / n)
    if s == 0:
        s = int(1. / (float(l) / float(n)))
        for i, x in enumerate(d):
            data[i*s] = x/m
    else:
        for i in range(0, n):
            data[i] = sum(d[i*s:(i+1)*s])/(m*s)
    return data