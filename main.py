import numpy as np
from matplotlib import pyplot as plt

from chsh import chsh_correlation
from operators import operators_set_creation
from plotting import plot_relative
from simulation import estimate_s

if __name__ == "__main__":
    #First task
    angles = np.array([0, np.pi / 4, np.pi / 8, 3 * np.pi / 8])
    operators = operators_set_creation(angles)
    bell_state = (1 / np.sqrt(2)) * np.array([[1, 0, 0, 1]])

    x = chsh_correlation(bell_state, operators)[0, 0]
    print(f"S = {x.real:.3f} + {x.imag:.3f}j")

    #Second task
    """
    para ti hermano
    """

    #Third task
    bell_state = (1 / np.sqrt(2)) * np.array([[1, 0, 0, 1]])
    rho = np.outer(bell_state, bell_state.conj().T)
    s = estimate_s(np.pi / 8, rho)
    print(f"S_estimated = {s.real:.3f} + {s.imag:.3f}j")
    fig, ax = plot_relative(1000, rho)
    plt.show()