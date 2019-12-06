# Write a simulator, as in the previous project, but add a Boolean gender ﬁeld and a ﬂoating-point strength ﬁeld to 
# each animal, using an Animal class as a base class. If two animals of the same type try to collide, then they only 
# create a new instance of that type of animal if they are of different genders. Otherwise, if two animals of the same 
# type and gender try to collide, then only the one of larger strength survives.

# create a 2 dimensional version of this with more complex behaviour

from random import choice, randrange
import time
from secrets import token_hex
class Animal:
    def __init__(self):
        self.gender = choice(['male', 'female'])
        self.strength = randrange(2,10)
class Bear(Animal):
    def __init__(self):
        super().__init__()
        self.id  = token_hex(2)
        self.name = 'Bear'
        self.stomach = []
        self.HUNGER_THRESHOLD = 2
        self.hunger_period = 0
    def __repr__(self):
        return 'Bear({},{})'.format(self.id, self.gender[0:1])
class Fish(Animal):
    def __init__(self):
        super().__init__()
        self.id  = token_hex(2)
        self.name = 'Fish'
    def __repr__(self):
        return 'Fish({},{})'.format(self.id,self.gender[0:1])

creatures = [Bear, Fish, None]

class Ecosystem:
    def __init__(self, size):
        self.river = []
        self.bear_ids = []
        self.fish_ids = []
        self.simulation_steps =0
        for _ in range(size):
            creature = choice(creatures)
            if creature:
                c = creature()
                id  = c.id
                self.river.append(c)
                if type(c) == type(Bear()):
                    self.bear_ids.append(id)
                elif type(c) == type(Fish()):
                    self.fish_ids.append(id)
            else:
                self.river.append(None)
    def _index_of_nearest_None(self):
        for creature in self.river:
            if creature == None:
                return self.river.index(creature)
    def get_fish(self,id):
        for creature in self.river:
            if creature and creature.id == id:
                return creature
    def get_bear(self,id):
        for creature in self.river:
            if creature and creature.id == id:
                return creature
    def move_creature(self,creature):
        directions ={ 'right': 1, 'left': -1, 'stay': 0 }
        if creature is None:
            return
        # choose direction
        if self.river.index(creature) == 0:
            direction = choice(['right', 'stay'])

        elif self.river.index(creature) == len(self.river)-1:
            direction = choice(['left', 'stay'])

        else:
            direction = choice(['left', 'right', 'stay'])

        current_position = self.river.index(creature)
        next_position = self.river.index(creature)+directions[direction]
        other_creature = self.river[next_position]

        if next_position == current_position:
            print('{} remains at {}'.format(creature, current_position))
            return
        
        elif creature and other_creature is None:
            self.river[next_position],self.river[current_position]  = creature, None
            print('{} moves from {} to {}'.format(creature,current_position, next_position))
            return
        # if creatures are of the same type
        elif type(creature) == type(other_creature) and type(creature) != type(None):
            # if same gender
            if creature.gender == other_creature.gender:
                # the stronger kills the weaker
                if creature.strength > other_creature.strength:
                    self.river[next_position] = creature
                    self.river[current_position] = None
                    if type(other_creature) == type(Bear()):
                        self.bear_ids.pop(self.bear_ids.index(other_creature.id))
                    elif type(other_creature) == type(Fish()):
                        self.fish_ids.pop(self.fish_ids.index(other_creature.id))
                    print('{} collides with {} at {} and kills it'.format(creature, other_creature, next_position))
                    return
                elif creature.strength < other_creature.strength:
                    self.river[current_position] = None
                    if type(creature) == type(Bear()):
                        self.bear_ids.pop(self.bear_ids.index(creature.id))
                    elif type(creature) == type(Fish()):
                        self.fish_ids.pop(self.fish_ids.index(creature.id))
                    print('{} collides with {} at {} and dies'.format(creature, other_creature, next_position))
                    return
                # they attacker recoils
                else:
                    print('{} collides with {} at {} and bounces back to {}'.format(creature, other_creature, next_position, current_position))
                    return
            # if not same gender give birth to child
            else:
                father = creature
                mother = other_creature
                birth_position = self._index_of_nearest_None()
                if birth_position:
                    if type(creature) == type(Bear()):
                        new_born = Bear()
                        self.river[birth_position] = new_born
                        self.bear_ids.append(new_born.id)
                    elif type(creature) == type(Fish()):
                        new_born = Fish()
                        self.river[birth_position] = new_born
                        self.fish_ids.append(new_born.id)
                    print('{} and {} meet at {} to give birth to {} at {}'.format(father, mother, next_position, new_born, birth_position))
        # if creatures are not of the same type
        else:
            if type(creature) == type(Bear()):
                eater = creature
                food = other_creature
                print('{} moves from {} to {} and eats {}'.format(eater,current_position, next_position, food))
                if food.id == 419:
                    print('dem don catch you')
            elif type(creature) == type(Fish()):
                eater = other_creature
                food = creature
                print('{} moves from {} to {} and is eaten by {}'.format(food, current_position, next_position, eater))
                if food.id == 419:
                    print('dem don catch you')
            eater.stomach.append(food)
            eater.hunger_period = 0
            self.fish_ids.pop(self.fish_ids.index(food.id))
            self.river[current_position] = None
            self.river[next_position] = eater
    def no_more_fish(self):
        for creature in self.river:
            if type(creature) == type(Fish()):
                return False
        return True
    def only_one_fish(self):
        bear_count = 0
        fish_count = 0
        for creature in self.river:
            if type(creature) == type(Fish()):
                fish_count += 1
            elif type(creature) == type(Bear()):
                bear_count += 1
        return True if bear_count == 0 and fish_count == 1 else False
    def all_fish(self):
        for creature in self.river:
            if type(creature) in [type(Bear()), type(None)]:
                return False
        return True



    def next_state(self):
        if self.no_more_fish():
            return 'no more fish'
        if self.all_fish():
            return 'all fish'
        if self.only_one_fish():
            return 'only one fish'
        for fish_id in self.fish_ids:
            fish = self.get_fish(fish_id)
            self.move_creature(fish)
        for bear_id in self.bear_ids:
            bear = self.get_bear(bear_id)
            bear.hunger_period += 1
            self.move_creature(bear)
            if bear in self.river and bear.hunger_period > bear.HUNGER_THRESHOLD:
                self.river[self.river.index(bear)] = None
                self.bear_ids.pop(self.bear_ids.index(bear.id))
                print('{} has starved to death'.format(bear))
        print(self.river)
        print()
        self.simulation_steps+=1
        time.sleep(1)
        return True
    def run_sim(self, steps):
        for _ in range(steps):
            if self.next_state() == 'no more fish':
                print('Simulation aborted. All fish have been eaten and the bears have now starved to death')
                return
            elif self.next_state() == 'all fish':
                print('Simulation aborted. River is filled to the brim with fish and they have all choked to death')
                return
            elif self.next_state() == 'only one fish':
                print('Simulation aborted. Only one fish remaining in whole river. He will live forever so...')
                return
            self.next_state()
        
if __name__ == '__main__':
    eco = Ecosystem(10)
    print(eco.river)
    eco.run_sim(20)
    # f = Fish()
    # print(f.gender)