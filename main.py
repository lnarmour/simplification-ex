import numpy as np
import sys

global OPS
OPS = 0


def _mul(a, b):
    global OPS
    OPS += 1
    return a * b


# As written, this has an asymptotic complexity of O(N^3).
# Can you rewrite it so that its asymptotic complexity is lower?!
#
def kernel(A, B, Y, N):

    for i in range(N):
        for j in range(i):
            for k in range(i):
                # Y[i] += A[i,j+k] * B[k,j]
                Y[i] += _mul(A[i,j+k], B[k,j])


def main():
    global OPS

    # set default problem size or parse args
    N = 250
    if len(sys.argv) > 1:
        N = int(sys.argv[1])

    # initialize some random data
    A = np.random.randint(0, 1000, size=(N,2*N))
    B = np.random.randint(0, 1000, size=(N,N))
    Y = np.zeros(N, dtype=int)

    # main work
    kernel(A, B, Y, N)

    # print summary
    print('N =', N)
    print('-> OPS =', OPS)


if __name__ == '__main__':
    main()
