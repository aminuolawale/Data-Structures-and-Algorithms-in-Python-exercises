#Write a Python program that inputs a polynomial in standard algebraic notation and outputs the ﬁrst derivative of 
# that polynomial.

# Overdone
# still todos: factorize, solve
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
            if self._coeff == 1 and self._power > 0:
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
        if type(other) in [type(1),type(1.0)]:
            coeff = self._coeff *other
            power = self._power
        elif type(other) == type(self):
            coeff = self._coeff * other._coeff
            power = self._power + other._power
        else:
            raise ValueError('Polynomial can only be multiplied by Polynomial or numeric types')
        return PolynomialTerm(coeff, power)
    def __gt__(self, other):
        return self._power > other._power
    def __lt__(self, other):
        return self._power < other._power
    def __eq__(self, other):
        return self._coeff == other._coeff and self._power == other._power
    def __neq__(self, other):
        return self._coeff != other._coeff or self._power != other._power
    def __call__(self, value):
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

        
class Polynomial(PolynomialTerm):
    def __init__(self, s=None):
        if s is None:
            self._terms = [PolynomialTerm()]
        else:
            raw_terms = []
            for term in self._split_into_terms(s):
                raw_terms.append(PolynomialTerm(term))
            self._terms = self._shrink_terms(raw_terms)
        
    def __repr__(self):
        poly_string = ''
        for term in self._terms:
            if term._coeff !=0:
                poly_string += repr(term) + ' '
        return poly_string

    def __len__(self):
        return len(self._terms)
    def __getitem__(self, index):
        return self._terms[index]
    def __add__(self, other):
        self,other = self._conform(other)
        poly_string = ''
        for term_self, term_other in zip(self, other):
            poly_string += repr(term_self + term_other)
        return Polynomial(poly_string)
    def __radd__(self, other):
        self,other = self._conform(other)
        poly_string = ''
        for term_self, term_other in zip(self, other):
            poly_string += repr(term_self + term_other)
        return Polynomial(poly_string)
    def __sub__(self, other):
        self,other = self._conform(other)
        poly_string = ''
        for term_self, term_other in zip(self, other):
            poly_string += repr(term_self - term_other)
        return Polynomial(poly_string)
    def __rsub__(self, other):
        self,other = self._conform(other)
        poly_string = ''
        for term_self, term_other in zip(self, other):
            poly_string += repr(term_self - term_other)
        return Polynomial(poly_string)
    def __neg__(self):
        return Polynomial() - self
    def __mul__(self, other):
        if type(other) in [type(1), type(1.0)]:
            poly_string = ''
            for term in self._terms:
                poly_string += repr(term*other)
        elif type(other) == type(self):
            poly_string = ''
            for self_term in self:
                for other_term in other:
                    poly_string += repr(self_term * other_term)
        else:
            raise ValueError('Polynomial can only be multiplied by Polynomial or numeric types')
        return Polynomial(poly_string)
    def __rmul__(self, other):
        if type(other) in [type(1), type(1.0)]:
            poly_string = ''
            for term in self._terms:
                poly_string += repr(term*other)
        elif type(other) == type(self):
            poly_string = ''
            for self_term in self:
                for other_term in other:
                    poly_string += repr(self_term * other_term)
        else:
            raise ValueError('Polynomial can only be multiplied by Polynomial or numeric types')
        return Polynomial(poly_string)
    def __pow__(self, value):
        poly = self
        for _ in range(value-1):
            poly *= self
        return poly

    def __gt__(self, other):
        return True if self.order() > other.order() else False
    def __lt__(self, other):
        return True if self.order() < other.order() else False
    def __call__(self, value):
        """ Evaluates a polynomial with the given value """
        sum =0
        for term in self:
            sum+= term(value)
        return sum

    
    #public methods
    def order(self):
        """ Returns the highest power of the Polynomial  """
        return self._terms[0]._power
    def least_non_zero_power(self):
        return self._terms[len(self._terms)-1]._power
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
    def _conform(self, other):
        if type(other) in [type(1), type(1.0)]:
            other = Polynomial(str(other)+'x0')
        self, other = self._match_polynomials(self, other)
        return self, other

    @staticmethod
    def _match_polynomials(p1, p2):
        # fill in the gaps in both polynomials i.e (x2 - 1) -> (x2 +0x -1)
        p1._middle_pad()
        p2._middle_pad()
        # both polynomials might not be of the same order so pad the lower order one up to the higher order one
        if p1 < p2:
            p1._left_pad_to_power(p2.order())
        elif p1 > p2:
            p2._left_pad_to_power(p1.order())
        p1_least_power = p1.least_non_zero_power()
        p2_least_power = p2.least_non_zero_power()

        # if they have different least powers pad the higher least power one down to the lower least power one
        if p1_least_power > p2_least_power:
            p1._right_pad_to_power(p2_least_power)

        elif p1_least_power <p2_least_power:
            p2._right_pad_to_power(p1_least_power)
        return p1,p2

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
            order -= 1
            if self[i]._power != order:
                self._terms.insert(i, PolynomialTerm(0, order))
            i+=1







