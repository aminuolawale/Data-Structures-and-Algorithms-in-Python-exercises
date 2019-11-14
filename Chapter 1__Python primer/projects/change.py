denominations={'one_thousand':1000,'five_hundred':500, 'two_hundred':200, 'hundred':100, 
                'fifty':50,'twenty':20, 'ten':10,'five':5 }

def is_valid_cash(cash):
    i = 0
    while cash >= denominations['five']:
        current_denomination =  denominations[list(denominations.keys())[i]]
        if cash - current_denomination >= 0:
            cash -= current_denomination
        else:
            i += 1
    return True if cash == 0 else False

def make_change(charge, cash):
    if not is_valid_cash(charge) or not is_valid_cash(cash):
        print('invalid amount given available denominatons')
        return None
    balance = cash - charge
    if balance == 0:
        return 'no balance to be given'
    result = ''
    changes = list(0 for x in range(0,len(denominations)))
    notes = list(denominations.keys())
    values = list(denominations.values())   
    i=0
    while True:
        if balance - values[i] == 0:
            changes[i] += 1
            break
        elif balance - values[i] > 0:
            balance -= values[i]
            changes[i] += 1
        else:
            i += 1
    for i,change in enumerate(changes):
        if change >0:
            if change >1:
                result += f'{change} {notes[i]} naira notes\n'
            else:
                result += f'{change} {notes[i]} naira note\n'
    result += f'making {cash - charge} naira'
    return result

def make_change_gen(charge, cash):
    if not is_valid_cash(charge) or not is_valid_cash(cash):
        print('invalid amount given available denominatons')
        return None
    balance = cash - charge
    if balance == 0:
        return 'no balance to be given'
    changes = list(0 for x in range(0,len(denominations)))
    notes = list(denominations.keys())
    values = list(denominations.values())   
    i=0
    while True:
        if balance - values[i] == 0:
            changes[i] += 1
            yield f'{changes[i]} {notes[i]} naira notes' if changes[i]>1 else f'{changes[i]} {notes[i]} naira note'
            break
        elif balance - values[i] > 0:
            balance -= values[i]
            changes[i] += 1
        else:
            if changes[i]:
                yield f'{changes[i]} {notes[i]} naira notes' if changes[i]>1 else f'{changes[i]} {notes[i]} naira note'
            i += 1


def compare_outputs(func1, func2, *args):
    r_func1 = func1(*args)
    r_func1 = r_func1.split('\n')[0:len(r_func1)-1]
    are_same = True
    for line,output in zip(r_func1, func2(*args)):
        if output != line:
            are_same = False
    return are_same



print(compare_outputs(make_change, make_change_gen,900,1000))
print(make_change(125,1000))
print('\ngenerator version\n')
for output in make_change_gen(125,1000):
    print(output)




