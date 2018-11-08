SEED = 1
A = 48271
M = 2147483647
Q = M // A
R = M % A


def random_gen(seed=SEED):
    tmp_seed = A * (seed % Q) - R * (seed / Q)
    if tmp_seed >= 0:
        seed = tmp_seed
    else:
        seed = tmp_seed + M
    return seed / M
