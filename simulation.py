import numpy as np


def measurement_operator(theta):
    """
    Creates a measurement operator P = |psi(theta)><psi(theta)|.

    Args:
        theta: an angle in radians.

    Returns:
        a measurement operator P.
    """
    psi = np.array([[np.cos(theta)], [np.sin(theta)]], dtype=complex)
    return np.outer(psi, psi.conj().T)


def set_probabilities(theta_a, theta_b, density_matrix):
    """
    Calculates the probability of an outcome (a, b) after measuring observables A_i and B_j;
    also referred to as P(a, b|theta_a, theta_b) = np.trace[density_matrix @ np.kron(P_A^a, P_B^b)].
    There are 4 possible outcomes:
        1. P(+, +|theta_a, theta_b) = np.trace[density_matrix @ np.kron(P_A^+, P_B^+)];
        2. P(+, -|theta_a, theta_b) = np.trace[density_matrix @ np.kron(P_A^+, P_B^-)];
        3. P(-, +|theta_a, theta_b) = np.trace[density_matrix @ np.kron(P_A^-, P_B^+)];
        4. P(-, -|theta_a, theta_b) = np.trace[density_matrix @ np.kron(P_A^-, P_B^-)].
    Notice that P_A^- = I - P_A^+ and P_B^- = I - P_B^+,
    while P_A^+ = P(theta_a) and P_B^+ = P(theta_b).

    Args:
        theta_a: an angle in radians for Alice's operator A_i.
        theta_b: an angle in radians for Bob's operator B_j.
        density_matrix: a density matrix of a system in question.

    Returns:
        Set of probabilities of outcomes.
    """
    P_A = measurement_operator(theta_a)
    P_B = measurement_operator(theta_b)
    prob_pp = np.trace(density_matrix @ np.kron(P_A, P_B))
    prob_pm = np.trace(density_matrix @ np.kron(P_A, np.eye(2) - P_B))
    prob_mp = np.trace(density_matrix @ np.kron(np.eye(2) - P_A, P_B))
    prob_mm = np.trace(density_matrix @ np.kron(np.eye(2) - P_A, np.eye(2) - P_B))
    return [prob_pp, prob_pm, prob_mp, prob_mm]


def estimated_correlation(probabilities):
    """
    Estimates the correlation between using a set of probabilities for a set of outcomes:
        <A_i, B_i> = (+1) * (+1) * P(+, +)
                   + (+1) * (-1) * P(+, -)
                   + (-1) * (+1) * P(-, +)
                   + (-1) * (-1) * P(-, -).

    Args:
        probabilities: a set of probabilities.

    Returns:
        estimated correlation.
    """
    return probabilities[0] - probabilities[1] - probabilities[2] + probabilities[3]


def estimate_s(phi, density_matrix):
    """
    Estimates the correlation S for a given relative angle phi and a density matrix.

    Args:
        phi: an angle in radians.
        density_matrix: a density matrix of a system in question.

    Returns:
        estimated correlation.
    """
    alice_angles = np.array([0, 2 * phi])
    bob_angles = np.array([phi, 3 * phi])

    result = (+ estimated_correlation(set_probabilities(alice_angles[0], bob_angles[0], density_matrix))
              - estimated_correlation(set_probabilities(alice_angles[0], bob_angles[1], density_matrix))
              + estimated_correlation(set_probabilities(alice_angles[1], bob_angles[0], density_matrix))
              + estimated_correlation(set_probabilities(alice_angles[1], bob_angles[1], density_matrix))
              )
    return result