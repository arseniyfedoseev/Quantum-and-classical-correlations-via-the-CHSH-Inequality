import numpy as np


#Initialization of the computational basis
computational_basis = np.array(([[1], [0]], [[0], [1]]),  dtype=complex)


def alice_basis(theta):
    """
    Creates Alice's basis:
    |a0> = +cos(theta)|0> + sin(theta)|1>
    |a1> = -sin(theta)|0> + cos(theta)|1>

    Args:
        theta: angle in radians

    Returns:
        Alice's basis

    """
    return np.array(([[[np.cos(theta)], [np.sin(theta)]], [[-np.sin(theta)], [np.cos(theta)]]]), dtype=complex)


def bob_basis(theta):
    """
    Creates Bob's basis:
    |b0> = +cos(theta)|0> + sin(theta)|1>;
    |b1> = -sin(theta)|0> + cos(theta)|1>.
    P.S.: I've chosen this convention because of the second point in 3rd task -
    in other one it just does not make sense. I also have changed angles
    for a maximum value of S.

    Args:
        theta: angle in radians

    Returns:
        Bob's basis
    """
    return np.array(([[np.cos(theta)], [np.sin(theta)]], [[-np.sin(theta)], [np.cos(theta)]]), dtype=complex)


def operator_creation(basis):
    """
    Creates matrix for an operator O so that:
    O|basis[0]> = +|basis[0]>
    O|basis[1]> = -|basis[1]>

    Args:
        basis: basis used for measurement.

    Returns:
        A matrix for an operator O.
    """
    return + np.outer(basis[0].conj().T, basis[0]) - np.outer(basis[1].conj().T, basis[1])


def expectation_value(operator, state):
    """
    Computes the expectation value of an operator in a state.

    Args:
        operator: a matrix (2^n, 2^n)
        state: a state vector (n, n)

    Returns:
        An expectation value of an operator in a state.
    """

    return state.reshape(1, operator.shape[0]) @ operator @ state.reshape(operator.shape[1], 1)

def operators_set_creation(thetas:np.ndarray):
    """
    Initializes operators A1, A2, B1, B2 needed for an experiment.

    Args:
         thetas: an 4-array of angles for different operators.

    Returns:
         set of operators A1, A2, B1, B2.
    """
    bases = [alice_basis(thetas[0]), alice_basis(thetas[1]), bob_basis(thetas[2]), bob_basis(thetas[3])]
    return [operator_creation(base) for base in bases]