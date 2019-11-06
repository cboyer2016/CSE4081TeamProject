########################################################################################################################################
# Author: Chad Boyer (cboyer2016@my.fit.edu), Connor Roth (croth2016@my.fit.edu), & Alan Guzman (aguzman2015@my.fit.edu)
# Course: CSE 4081
# Team Project: Discrete Logarithm Analysis
# Implemented Algorithm: Brute Force
########################################################################################################################################

########################################################################################################################################
# This function calculates the discrete logarithm using a brute force approach. The worst case time complexity of this algorithm
# O(modulus).
########################################################################################################################################
def bruteForce(base, value, modulus):
    exponent = 0                                        # exponent to make the 
    while exponent is not modulus:                      # Iterate over all possible exponent powers
        if (pow(base,exponent, modulus) == value):      # Check if the exponent makes the values congruent
            return exponent                             # Return the value if congruent
        exponent += 1                                   # Increment the value by 1
    return None                                         # Return None if there is not a logarithm

if __name__ == "__main__":
    print bruteForce(10, 5, 541)