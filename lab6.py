__author__ = 'fiodar'

from numpy import exp
from pde import *


phi = lambda y: exp(2*y), lambda y: exp(2*y-1)
psi = lambda x: exp(-x), lambda x: exp(2-x)
n = 30
x_bounds = 0, 1
y_bounds = 0, 1
u = dirichlet_problem_2d(x_bounds, y_bounds, phi, psi, n, n, 0.001)


x, y = np.linspace(0, 1, n), np.linspace(0, 1, n)
x, y = np.meshgrid(x, y)
fig = plt.figure('Dirichlet Problem')
ax = fig.gca(projection='3d')
surf = ax.plot_surface(x, y, u)
plt.show()