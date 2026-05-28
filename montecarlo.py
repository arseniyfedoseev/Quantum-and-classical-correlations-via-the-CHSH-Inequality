import numpy as np

# Local classical functions with hidden variable lambda
def default(theta, lam):
	return 1 if np.cos(theta - lam) >= 0 else -1

def montecarlo(
	a_func=default,
	b_func=default,
	theta_A1=0,
	theta_A2=np.pi / 4,
	theta_B1=np.pi / 8,
	theta_B2=-np.pi / 8,
	N=100000,
):


	# Expectation values
	A1B1 = 0
	A1B2 = 0
	A2B1 = 0
	A2B2 = 0

	for _ in range(N):
	
		# Shared hidden variable
		lam = np.random.uniform(0, 2 * np.pi)
	
		# Add products ab
		A1B1 += a_func(theta_A1, lam) * b_func(theta_B1, lam)
		A1B2 += a_func(theta_A1, lam) * b_func(theta_B2, lam)
		A2B1 += a_func(theta_A2, lam) * b_func(theta_B1, lam)
		A2B2 += a_func(theta_A2, lam) * b_func(theta_B2, lam)

	# Divide by N to get expectation values
	A1B1 /= N
	A1B2 /= N
	A2B1 /= N
	A2B2 /= N

	# Classical CHSH value	
	S = A1B1 - A1B2 + A2B1 + A2B2

	return {
		"S": S,
		"A1B1": A1B1,
		"A1B2": A1B2,
		"A2B1": A2B1,
		"A2B2": A2B2,
	    }
