#Demonstrate how to use Python’s list comprehension syntax to produce the list [ a , b , c , ..., z ], 
# but without having to type all 26 such characters literally.

print(list(chr(97+a) for a in range(0,26)))
