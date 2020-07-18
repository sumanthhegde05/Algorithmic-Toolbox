# Uses python3
import sys

def optimal_weight(W, w):
    matrix = [[0 for _ in range(W+1)] for _ in range(len(w))]
    for j in range(0, len(w)):
        for i in range(1, W + 1):
            if w[j] > i:
                matrix[j][i] = matrix[j-1][ i]
            else:
                matrix[j][i] = max(w[j] + matrix[j - 1][i - w[j]], matrix[j-1][i])
    return matrix[len(w) - 1][W]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
