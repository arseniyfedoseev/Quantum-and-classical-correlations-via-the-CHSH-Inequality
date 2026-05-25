import numpy as np
from operators import expectation_value, operators_set_creation


def chsh_correlation(state, operators_set):
    """
    Calculates Clauser-Horne-Shimony-Holt correlation.

    Args:
        state: State chosen for an expectation value of the operators.
        operators_set: Set of operators A1, A2, B1, B2.

    Returns:
        The CHSH correlation value S.
    """
    A1, A2, B1, B2 = operators_set

    S = (
            + expectation_value(np.kron(A1, B1), state)
            - expectation_value(np.kron(A1, B2), state)
            + expectation_value(np.kron(A2, B1), state)
            + expectation_value(np.kron(A2, B2), state)
    )
    return S