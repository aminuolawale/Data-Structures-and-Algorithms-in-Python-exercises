# In our implementation of the scale function (page25), the body of the loop executes the command data[j] = factor. 
# Wehavediscussed thatnumeric types are immutable, andthat use ofthe = operator inthis context causes the creation 
# of a new instance (not the mutation of an existing instance). How is it still possible, then, that our implementation 
# of scale changes the actual parameter sent by the caller?