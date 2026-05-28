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
    phi_opt = np.pi / 8
    S_opt = 2 * np.sqrt(2)

    for i, phi in enumerate(phis):
        s[i] = estimate_s(phi, density_matrix).real
    ax.plot(phis, s)

    ax.axhline(y=-2, color='k', linestyle='--', label='Classical ±2')
    ax.axhline(y=2, color='k', linestyle='--')
    ax.axhline(y=-2 * np.sqrt(2), color='r', linestyle='--', label='Quantum ±2√2')
    ax.axhline(y=2 * np.sqrt(2), color='r', linestyle='--')

    plt.scatter(phi_opt, S_opt, color='r', s=80, zorder=5)
    plt.annotate(
        r"$\phi=\frac{\pi}{8},\quad S=2\sqrt{2}$",
        xy=(np.pi / 8, 2 * np.sqrt(2)),
        xytext=(0.75, 2.35),
        arrowprops=dict(arrowstyle="->"),
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", alpha=0.9)
    )
    plt.legend(loc="right", framealpha=0.9)
    ax.set_xlabel(r'$\phi$, rad')
    ax.set_ylabel(r'$S$')
    ax.set_title(r'S as a function of $\phi$')
    ax.grid()

    ax.tick_params(axis='x', top=True, labeltop=True)
    ax.tick_params(axis='y', right=True, labelright=True)
    return fig, ax
