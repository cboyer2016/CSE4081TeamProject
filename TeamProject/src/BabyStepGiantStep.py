########################################################################################################################################
# Author: Chad Boyer (cboyer2016@my.fit.edu), Connor Roth (croth2016@my.fit.edu), & Alan Guzman (aguzman2015@my.fit.edu)
# Course: CSE 4081
# Team Project: Discrete Logarithm Analysis
# Implemented Algorithm: Small-Step, Giant Step
########################################################################################################################################

from math import ceil, sqrt

########################################################################################################################################
# This function calculates the discrete logarithm using the Small-Step, Giant-Step algorithm. The worst case time complexity of this
    # algorithm is O(square root(m)). The algorithm begins on line 25-30. Lines 17 - 22 are part of the precomputation process.
########################################################################################################################################
def babyStepGiantStep(base, value, modulus):
    
    # Calculate the Baby Step
    m = int(ceil(sqrt(modulus-1)))                      # Take the ceiling square root of the Modulus -1
    babyStep = {}                                       # Store the baby step values in an array
    for x in range(m):                                  # Iterate over modulus - 1 square root
        babyStep[pow(base, x, modulus)] = x             # Store (base ^ x) % modulus and x
    
    c = pow(base, m * (modulus - 2), modulus)           # Calculate inverse log with Fermat's Little Theorem
 
    # Take the Giant Step now
    for x in range(m):                                  # Iterate over modulus -1 square root
        y = (value * pow(c, x, modulus)) % modulus      # Calculate the giant step: (value * (c ^ x) % modulus) % modulus
        if y in babyStep:                               # Check if the giant step is in the baby step list
            return x * m + babyStep[y]                  # If so, multiply m by x and add the baby step

    return None                                         # If not found, return nothing


if __name__ == "__main__":
    print babyStepGiantStep(2, 7709318, 20084173)