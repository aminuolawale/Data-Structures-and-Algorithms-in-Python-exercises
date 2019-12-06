#different polynomial forms:
# axa, +axa, -axa, xa, +xa,-xa

class PolynomialTerm:
    def __init__(self, a= None, b= None):
        # attributes: _coeff, _power
        if a is None and b is None:
            # sets polynomial to 0X^0
            self._coeff = self._power = 0
        elif a is not None and b is None:
            # i.e. the polynomial term is passed as a string
            # remove extraneous symbols e.g. '^', ' '
            a = self._clean_up(a.lower())
            self._coeff, self._power = self._get_coeff_and_power(a)
        else:
            # i.e polynomial term is passed as (coeff, power)
            self._coeff, self._power = a, b

    def __repr__(self):
        if self._coeff >=0:
            # if coefficient is 1 print only sign eg. + 1x -> +x
            if self._coeff == 1:
                coeff = '+'
            else:
                coeff = '+' + str(self._coeff)
        # negative coeffs
        else:
            coeff = self._coeff

        power = self._power
        if power == 0:
            # dsiplay only constant
            poly_term = '{}'.format(coeff)
        elif power == 1:
            # display only coeff and X
            poly_term = '{}X'.format(coeff)
        else:
            # display full polynomial term AX^b
            poly_term = '{}X^{}'.format(coeff, power)
        return poly_term
    
    def __add__(self, other):
        if not self._same_order(other):
            raise ValueError('Cannot add Polynomial terms of different orders')
        coeff = self._coeff + other._coeff
        power = self._power
        return PolynomialTerm(coeff, power)

    def __sub__(self, other):
        if not self._same_order(other):
            raise ValueError('Cannot subtract Polynomial terms of different orders')
        coeff = self._coeff - other._coeff
        power = self._power
        return PolynomialTerm(coeff, power)

    def __mul__(self,other):
        coeff = self._coeff * other._coeff
        power = self._power + other._power
        return PolynomialTerm(coeff, power)
    def __gt__(self, other):
        return self._power > other._power
    def __lt__(self, other):
        return self._power < other._power
    def __eq__(self, other):
        return self._coeff == other._coeff and self._power == other._power
    def __neq__(self, other):
        return self._coeff != other._coeff or self._power != other._power
    def eval(self, value):
        return self._coeff*value**self._power
    def derivative(self):
        if self._power == 0:
            return PolynomialTerm()
        coeff = self._power * self._coeff
        power = self._power - 1
        return PolynomialTerm(coeff, power)

        
    # utility modifiers
    @staticmethod
    def _clean_up(s):
        # removes extraneous terms e.g '^', ' '
        new_s = ''
        for l in s:
            if l not in '^ ':
                new_s += l
        return new_s
    def _get_coeff_and_power(self,s):
        # constant term
        if not 'x' in s: 
            coeff, power  = s, 0
            return float(coeff), int(power)
        # other terms
        split_poly_term = s.split('x') # [coeff] [X] [power]
        coeff, power = split_poly_term[0], split_poly_term[1]
        if coeff == '' or coeff == '+':
            # i.e. polynomial takes the form x^a or +x^a
            coeff = '+1'
            # so that polynomial now takes the form +1x^a
        elif coeff == '-':
            coeff = '-1'
        if power == '':
            power = '1'
        return float(coeff), int(power)


    # checkers
    def _same_order(self, other):
        return self._power == other._power


# p = PolynomialTerm('3X2')
# p1 = PolynomialTerm('2X1')
# print (p != p1)
        
class Polynomial(PolynomialTerm):
    def __init__(self, s):
        raw_terms = []
        for term in self._split_into_terms(s):
            raw_terms.append(PolynomialTerm(term))
        self._terms = self._shrink_terms(raw_terms)
        
    def __repr__(self):
        poly_string = ''
        for term in self._terms:
            poly_string += repr(term) + ' '
        return poly_string

    def __len__(self):
        return len(self._terms)
    def __getitem__(self, index):
        return self._terms[index]
    def __add__(self, other):
        # fill in the gaps in both polynomials i.e (x2 - 1) -> (x2 +0x -1)
        self._middle_pad()
        other._middle_pad()
        # both polynomials might not be of the same order so pad the lower order one up to the higher order one
        if self < other:
            self._left_pad_to_power(other.order())
        elif self > other:
            other._left_pad_to_power(self.order())
        self_least_power = self.least_non_zero_power()
        other_least_power = other.least_non_zero_power()
        # if they have different least powers pad the higher least power one down to the lower least power one
        if self_least_power > other_least_power:
            self._right_pad_to_power(other_least_power)
        elif self_least_power < other_least_power:
            other._right_pad_to_power(self_least_power)
        poly_string = ''
        for term_self, term_other in zip(self, other):
            poly_string += repr(term_self + term_other)
        return Polynomial(poly_string)

    def __mul__(self, other):
        poly_string = ''
        for self_term in self:
            for other_term in other:
                poly_string += repr(self_term * other_term)
        return Polynomial(poly_string)

        
    def __gt__(self, other):
        return True if self.order() > other.order() else False
    def __lt__(self, other):
        return True if self.order() < other.order() else False
    
    #public methods
    def order(self):
        """ Returns the highest power of the Polynomial  """
        return self._terms[0]._power
    def least_non_zero_power(self):
        return self._terms[len(self._terms)-1]._power
    def eval(self, value):
        """ Evaluates a polynomial with the given value """
        sum =0
        for term in self:
            sum+= term.eval(value)
        return sum

    def derivative(self):
        """ Returns the first order derivative of the polynomial """
        poly_string = ''
        for poly in self:
            if poly.derivative() is not None:
                poly_string += repr(poly.derivative())
        return Polynomial(poly_string)
    
    def nth_derivative(self,order = 1):
        poly = self
        for _ in range(order):
            d_poly = poly.derivative()
            poly = d_poly
        return poly
            



    # utility modifiers
    def _split_into_terms(self, s):
        # split Polynomial into individual polynomial terms
        terms = []
        term = ''
        for index,l in enumerate(s):
            if index == len(s) -1:
                term += l
                terms.append(term)
            if l in '+-' and index >0:
                terms.append(term)
                term = l
            else:
                term += l
        return terms

    def _sort_powers(self,d):
        # sort the dictionary of powers and their positions
        sorted_keys = sorted(d, reverse=True)
        new_d = {}
        for key in sorted_keys:
            new_d[key] = d[key]
        return new_d

    def _shrink_terms(self, terms):
        # collect like terms and evaluate
        powers = [ term._power for term in terms]
        powers_set = set(powers)
        # a dict to store powers and the positions in which they occcur in the polynomial
        powers_and_positions = {}
        for power in powers_set:
            powers_and_positions[power] = []
            for index,present_power in enumerate(powers):
                if power == present_power:
                    powers_and_positions[power].append(index)
        # sort the dict
        powers_and_positions = self._sort_powers(powers_and_positions)
        shrunk_terms = []
        for power,positions in zip(powers_and_positions.keys(), powers_and_positions.values()):
            # if the current power occurs in only one position, just add that term to the list
            if len(positions) == 1:
                shrunk_terms.append(terms[positions[0]])
            # if not, sum all the terms at the given positions
            else:
                # create a base for adding -> 0x^p
                sum = PolynomialTerm(0,power)
                for position in positions:
                    sum += terms[position]
                # ignore zero coefficient terms
                if sum._coeff != 0:
                    shrunk_terms.append(sum)
        return shrunk_terms

    def _left_pad_to_power(self,n):
        poly_order = self.order()
        while poly_order < n:
            poly_order += 1
            self._terms.insert(0,PolynomialTerm(0,poly_order))

    def _right_pad_to_power(self, n):
        least_power = self.least_non_zero_power()
        if least_power <= n:
            return
        while least_power >n:
            least_power -= 1
            self._terms.append(PolynomialTerm(0,least_power))
    def _middle_pad(self):
        order = int(self.order())
        least_power = int(self.least_non_zero_power())
        i = 1
        while order > least_power:
            order -= 1.0
            if self[i]._power != order:
                self._terms.insert(i, PolynomialTerm(0, order))
            i+=1







p = Polynomial('x4 -x3 -x2 -x1 -10 -11x5 -x4 +x3')
print(p.nth_derivative(1))



