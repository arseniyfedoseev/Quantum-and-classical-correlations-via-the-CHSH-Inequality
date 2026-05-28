import numpy as np

from montecarlo import montecarlo

# default behaviour : angles 0, pi/4, pi/8, -pi/8; function sign cos
results = montecarlo()

print(f"Default S = {results['S']}")

