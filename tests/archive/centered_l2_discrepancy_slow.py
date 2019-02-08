import numpy as np


def centered_l2_discrepancy_slow(X, check_bounds=True):
    if check_bounds and (np.any(np.min(X) < 0 or np.max(X) > 1)):
        raise Exception("Make sure that all X are between 0 and 1.")

    n_points, n_dim = X.shape

    acmh = np.abs(X - 0.5)

    val = 0

    for k in range(n_points):
        temp = 1
        for i in range(n_dim):
            temp = temp * (1 + 0.5 * (acmh[:, i] + acmh[k, i] - np.abs(X[:, i] - X[k, i])))
        val += np.sum(temp)

    val = ((13 / 12) ** n_dim - 2 / n_points * np.sum(
        np.prod(1 + 0.5 * (acmh - acmh ** 2), axis=1)) + val / n_points ** 2) ** 0.5

    return val
