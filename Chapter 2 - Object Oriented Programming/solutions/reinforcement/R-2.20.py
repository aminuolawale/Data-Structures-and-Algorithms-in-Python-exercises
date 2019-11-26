#What are some potential efﬁciency disadvantages of having very deep inheritance trees, that is, a large set of classes,
#  A, B, C, and so on, such that B extends A, C extends B, D extends C, etc.?


# A major efficiency disadvantage comes up during the Namespace lookup when a method is called on an object. If an
# instance of class Z calls a method implemented in class A, the interpreter would have to look through each class Z
# through A till it eventually finds it in A. This could cause significant overhead

# If all the classes call their derived class's constructor then for every instantiation of an object, each constructor
# in the inheritance chain is called and are all stored on the stack, leading to inefficient memory usage

# Another disadvantage is that if a method is overriden in several of the classes then things get messy.