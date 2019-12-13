#What are some potential efﬁciency disadvantages of having very shallow inheritance trees, that is, a large set of classes
#  A, B, C, and so on, such that all of these classes extend a single class, Z?

# The major disadvantage here is that there might be duplication of methods and attributes. Some classes that could have simply
# inherited methods and attributes from other derived classes would have to implement them themselves leading to duplicity of code.