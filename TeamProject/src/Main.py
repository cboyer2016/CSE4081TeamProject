########################################################################################################################################
# Author: Chad Boyer (cboyer2016@my.fit.edu), Connor Roth (croth2016@my.fit.edu), & Alan Guzman (aguzman2015@my.fit.edu)
# Course: CSE 4081
# Team Project: Discrete Logarithm Analysis
# Implemented Algorithm: None
########################################################################################################################################

import SmallStepGiantStep
import BruteForce
import sys

########################################################################################################################################
# This function outputs the values in an equation to visualize the value solved for
########################################################################################################################################
def outputEqn(base, value, modulus):
    print value, "= (", base, " ^ x ) %" , modulus          # Output the values in an equation format

########################################################################################################################################
# This function is used to run all of the algorithms along with running multiple different test cases
########################################################################################################################################
def main (fileName):
    fileOpen = open(fileName, 'r')                          # Read the input from the file
    
    
    for line in fileOpen.readlines():                       # Iterate over all the lines
        info = line.split(" ")                              # Break the line into parts
        base = int(info[0])                                 # Take the base from the input
        value = int(info[1])                                # Take the value from the input
        modulus = int(info[2])                              # Take the modulus from the input

        outputEqn(base, value, modulus)                     # Output the equation being solved

        # Output values of the algorithms
        print "Brute Force:\t\tx =", BruteForce.calculateExponent(base, value, modulus)
        print "Small-Step, Giant-Step:\tx =", SmallStepGiantStep.calculateExponent(base, value, modulus)


# This is done to run the main function
if __name__ == "__main__":
    main(sys.argv[1])                                       # Pass in the test file input name