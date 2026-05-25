import numpy as np
import matplotlib.pyplot as plt
from simulation import estimate_s

def plot_relative(points, density_matrix):
    """
    Plots the estimated CHSH correlation S in function of phi;
    put plt.show() afterwards to see the graph.

    Args:
        points: a number of different phi values.
        density_matrix: a density matrix used to estimate the CHSH correlation.

    Returns:
        fig: a matplotlib figure object.
        ax: a matplotlib axes object.
    """
    fig, ax = plt.subplots()

    phis = np.linspace(0, 2*np.pi, points)
    s = np.zeros(points)
    for i, phi in enumerate(phis):
        s[i] = estimate_s(phi, density_matrix).real
    ax.plot(phis, s)
    ax.set_xlabel(r'$\phi$, rad')
    ax.set_ylabel(r'$S$')
    ax.set_title(r'S as a function of $\phi$')
    ax.grid()

    ax.tick_params(axis='x', top=True, labeltop=True)
    ax.tick_params(axis='y', right=True, labelright=True)
    return fig, ax
