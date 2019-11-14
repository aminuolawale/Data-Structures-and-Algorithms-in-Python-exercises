#Had weimplemented the scale function (page 25) as follows, does it work properly?

#def scale(data, factor):
#   for val in data: 
#       val *= factor 

# Explain why or why not.


#ANS
#It will not work properly because the current value in data is copied into val which is then scaled by the factor. This 
#does not affect the contents of data
