from math import inf
import numpy as np

def evalt(a, b, store):
    if store == '+':
        return a + b
    elif store == '-':
        return a - b
    elif store == '*':
        return a * b
    else:
        assert False


def min_and_max(m, M, store, i, j):
    tmp_min = inf
    tmp_max = -inf

    for k in range(i, j):
        a = evalt(M[i][k], m[k + 1][j], store[k])
        b = evalt(m[i][k], m[k + 1][j], store[k])
        c = evalt(M[i][k], M[k + 1][j], store[k])
        d = evalt(m[i][k], M[k + 1][j], store[k])

        tmp_min = min(tmp_min, a, b, c, d)
        tmp_max = max(tmp_max, a, b, c, d)

    return (tmp_min, tmp_max)


def get_maximum_value(dataset):
    store = dataset[1:len(dataset):2]
    d = dataset[0:len(dataset) + 1:2]
    n = len(d)
    m = np.zeros(shape=(n, n), dtype=int)
    M = np.zeros(shape=(n, n), dtype=int)
    for i in range(n):
        m[i][i] = int(d[i])
        M[i][i] = int(d[i])

    for s in range(1, n):
        for i in range(n - s):
            j = i + s
            m[i][j], M[i][j] = min_and_max(m, M, store, i, j)
    return M[0][n - 1]


if __name__ == "__main__":
    print(get_maximum_value(input()))