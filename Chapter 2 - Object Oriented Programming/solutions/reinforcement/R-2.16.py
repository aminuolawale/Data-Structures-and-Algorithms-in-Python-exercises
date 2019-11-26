# Our Range class, from Section 2.3.5, relies on the formula max(0, (stop − start + step − 1) // step) to compute the 
# number of elements in the range. It is not immediately evident why this formula provides the correct calculation, 
# even if assuming a positive step size. Justify this formula, in your own words.

# Normaly, (stop - start)/step should give us the correct answer but the range() function does not include the stop term
# in the sequence. Therefore it becomes (stop -1 - start )/step. The first term is however included in the sequence leading
# to one extra term so we get. 1 + (stop -1 - start)/step which is simply (stop +step -1 - start)/step. Now if we dont get
# a whole number as answer from this expression it means the last interval was not up to the step value so we want to 
# round it off. We use integer division, leading to (stop − start + step − 1) // step. In case invalid values are passed such
# as stop being less than start, we will have 0 terms in the sequence instead of the negative value that would result so
# we use the max function to always default to 0 whenever we get a negative answer, leading to
# max(0, (stop − start + step − 1) // step)