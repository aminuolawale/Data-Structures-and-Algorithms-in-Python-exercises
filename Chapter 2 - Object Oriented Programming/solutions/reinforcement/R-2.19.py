#When using the ArithmeticProgression class of Section 2.4.2 with an increment of 128 and a start of 0, how many calls 
# to next can we make before we reach an integer of 2^63 or larger?


# The first call to next yields 128 = 128 * 1. Therefore 128 * n calls yeilds 2^63
# n = 2^63/128 = 2^56 calls