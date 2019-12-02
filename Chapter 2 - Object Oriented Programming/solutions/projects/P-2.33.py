#Write a Python program that inputs a polynomial in standard algebraic notation and outputs the ﬁrst derivative of 
# that polynomial.

#Done
# My personal additions:
#   add, eval() and some other basic mathematical operations
#TODO
#   sort polynomial
#   refactor this mess

class Polynomial:
    @staticmethod
    def is_first_order_term(s):
        x_pos = s.find('x') 
        if x_pos >= 0:
            if s[len(s)-1] == 'x':
                return True
        return False
    @staticmethod
    def pad_polynomial(coeffs,powers):
        max_power = int(powers[0])
        current_power = max_power
        i=0
        while current_power >0:
            i+=1
            if len(powers) == i:
                current_power-=1
                powers.append(str(current_power))
                coeffs.append('+0')
            elif powers[i] != str(current_power-1):
                current_power -=1 
                powers.insert(i,str(current_power))
                coeffs.insert(i,'+0')
            else:
                current_power -= 1

        return coeffs,powers
        

    def split_by_plus_or_minus(self,s):
        s = s.lower()
        terms = []
        temp = ''
        for i,l in enumerate(s):
            if l ==' ':
                continue
            if l in ['+','-'] and i >0:
                terms.append(temp)
                temp = l 
            elif i == len(s) - 1:
                temp+=l
                terms.append(temp)
            else:
                temp += l
        for i,term in enumerate(terms):
            if not 'x' in terms[i]:
                terms[i] += 'x0'
            if  self.is_first_order_term(term):
                terms[i] += '1'
        return terms

    
    def get_coeffs_and_power(self,terms):
        coeffs, powers =[], []
        for term in terms:
            split_term = term.split('x')
            c,p = split_term[0], split_term[1]
            c = '+{}'.format(c) if not c[0] in ['-','+'] else c
            coeffs.append(c)
            powers.append(p)
        coeffs, powers = self.pad_polynomial(coeffs,powers)
        return coeffs, powers

    def __init__(self,s):
        terms = self.split_by_plus_or_minus(s) 
        coeffs,powers = self.get_coeffs_and_power(terms)
        self._coeffs = coeffs
        self._powers = powers

    def __repr__(self):
        poly = ''
        for coeff, power in zip(self._coeffs, self._powers):
            poly +=' {}X{} '.format(coeff,power)
        return poly
    def __len__(self):
        return self._powers[0]
    def __getitem__(self, index):
        poly = '{}X{}'.format(self._coeffs[index], self._powers[index])
        print(poly)
        return Polynomial(poly)
    def __eq__(self, other):
        for s,o in zip(self._coeffs,other._coeffs):
            if s != o:
                return False
        return True
    def __gt__(self,other):
        return True if self._powers[0] > other._powers[0] else False
    def __lt__(self,other):
        return True if self._powers[0] < other._powers[0] else False
    
    def __add__(self, other):
        if self > other:
            p = repr(other)
            p = '0X{}'.format(self._powers[0]) + p
            other = Polynomial(p)
        elif self < other:
            p = repr(self)
            p = '0X{}'.format(other._powers[0]) + p
        poly =''
        for s, o, power in zip(self._coeffs, other._coeffs,self._powers):
            new_coeff = int(s) + int(o)
            if new_coeff >=0:
                new_coeff = '+'+str(new_coeff)
            poly += '{}X{}'.format(new_coeff,power)
        return Polynomial(poly)

    def derivative(self):
        d=''
        if self._powers[len(self._powers)-1] == '0':
            self._powers.pop()
        for coeff,power in zip(self._coeffs,self._powers):
            new_coeff = str(int(coeff)*int(power))
            if new_coeff[0] != '-':
                new_coeff = '+' + new_coeff
            d+='{}X{}'.format(new_coeff, int(power)-1)
        return Polynomial(d)
    def eval(self, value):
        result = 0
        for coeff,power in zip(self._coeffs,self._powers):
            result += int(coeff)* value**int(power)
        return result
        
            


p = Polynomial('10x5-2x1 +3x1-0')
p1 = Polynomial('-2X5 -10x4-2x1-0')
print(p)
print((p+p1).derivative())
print(p.eval(1))



    


