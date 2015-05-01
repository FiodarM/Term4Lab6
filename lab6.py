__author__ = 'fiodar'

from numpy import exp
from pde import *
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D


phi = lambda y: exp(2*y), lambda y: exp(2*y-1)
psi = lambda x: exp(-x), lambda x: exp(2-x)
n = 20
x_bounds = 0, 1
y_bounds = 0, 1
u = dirichlet_problem_2d(x_bounds, y_bounds, phi, psi, n, n, 0.01)

x, y = np.linspace(x_bounds[0], x_bounds[1], n), np.linspace(y_bounds[0], y_bounds[1], n)
x, y = np.meshgrid(x, y)
fig = plt.figure('Dirichlet Problem')
ax = fig.gca(projection='3d')
surf = ax.plot_surface(x, y, u, rstride=2, cstride=2, cmap=cm.coolwarm)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('u')
fig.set_tight_layout(True)
plt.show()