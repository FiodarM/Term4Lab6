__author__ = 'fiodar'

import numpy as np


def dirichlet_problem_2d(x_bounds, y_bounds, conditions_x, conditions_y, n_x=50, n_y=50, tol=0.01):

    x = np.linspace(x_bounds[0], x_bounds[1], n_x)
    y = np.linspace(y_bounds[0], y_bounds[1], n_y)
    phi = conditions_x[0](x), conditions_x[1](x)
    psi = conditions_y[0](y), conditions_y[1](y)
    u = np.zeros((len(x), len(y)))
    u[0] = conditions_y[0](y)
    u[-1] = conditions_y[1](y)
    u = u.transpose()
    u[0] = conditions_x[0](x)
    u[-1] = conditions_x[1](x)
    u = u.transpose()

    iterations = 0
    while True:
        iterations += 1
        u0 = np.copy(u)
        for i, item in enumerate(u[1:-1]):
            for j in xrange(1, len(item)-1):
                u[i+1][j] = 0.25 * (u[i][j]+u[i+2][j]+u[i+1][j+1]+u[i+1][j-1])

        if np.max(np.abs(u-u0))/np.mean(np.abs(u)) <= tol:
            print 'Number of iterations:', iterations
            break

    return u


