# In our implementation of the scale function (page25), the body of the loop executes the command data[j] = factor. 
# We have discussed that numeric types are immutable, and that use of the = operator in this context causes the creation 
# of a new instance (not the mutation of an existing instance). How is it still possible, then, that our implementation 
# of scale changes the actual parameter sent by the caller ?


#ANS
#Though numeric types are immutable, lists of numeric types are mutable: the values within them can change. The list thus
#retains its identity while its contents can change theirs

