#Draw a class inheritance diagram for the following set of classes: 
# • Class Goat extends object and adds an instance variable tail and methods milk() and jump(). 
# • Class Pig extends object and adds an instance variable nose and methods eat(food) and wallow(). 
# • Class Horse extends object and adds instance variables height and color, and methods run() and jump(). 
# • Class Racer extends Horse and adds a method race(). 
# • Class Equestrian extends Horse,adding an instance variable weight and methods trot() and is_trained().


#                   ________________________________________________
#                   |                                              |               
#                   |                    Object                    |
#                   |                                              |
#                   ________________________________________________
#                    ^                    ^                       ^
#                    |                    |                       |
#                  Goat                  Pig                    Horse
#        |--------------------|  |------------------------ | |--------------------|
#        |attr: _tail         |  |attr: _nose              | |attr:_height, _color|
#        |meth: milk(), jump()|  |meth: eat(food), wallow()| |meth: run(), jump() |
#        |____________________|  |_________________________| |____________________|
#                                                                ^             ^
#                                                                |             |
#                                                              Racer       Equestrian
#                                                        |------------|  |--------------------------|
#                                                        |attr:       |  |attr: _weight             |
#                                                        |meth: race()|  |meth: trot(), is_trained()|
#
#
#
#
#
#
