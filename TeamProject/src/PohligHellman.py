import math
from functools import reduce

# Modulus must be prime
# Generator must be modulus' primitive root.

def calculate_key(generator, generator_exponent, modulus):
    return (generator ** generator_exponent) % modulus

def calculate_public_key(public_generator, private_key, public_modulus):
    return calculate_key(public_generator, private_key, public_modulus)

def calculate_secret_key(public_key, private_key, public_modulus):
    return calculate_key(public_key, private_key, public_modulus)

def simulate_key_exchange(public_generator, public_modulus, a_private_key, b_private_key):
    # Calculated and shared over unprotected communication.
    a_public_key =  calculate_public_key(public_generator, a_private_key, public_modulus)
    b_public_key =  calculate_public_key(public_generator, b_private_key, public_modulus)
    # Calculated and kept. Never shared.
    a_secret_key = calculate_secret_key(b_public_key, a_private_key, public_modulus)
    b_secret_key = calculate_secret_key(a_public_key, b_private_key, public_modulus)
    # Note, both a_secret_key and b_secret_key are equal.
    return a_public_key, b_public_key

def extended_euclidean(a, b): 
    if a == 0: 
        return (b, 0, 1) 
    else: 
        g, y, x = extended_euclidean(b % a, a) 
        return (g, x - (b // a) * y, y) 
  

def modinv(a, m): 
    g, x, y = extended_euclidean(a, m) 
    return x % m 

def crt(m, x): 
    while True: 
        temp1 = modinv(m[1],m[0]) * x[0] * m[1] + modinv(m[0],m[1]) * x[1] * m[0] 
        temp2 = m[0] * m[1] 
        x.remove(x[0]) 
        x.remove(x[0]) 
        x = [temp1 % temp2] + x  
        m.remove(m[0]) 
        m.remove(m[0]) 
        m = [temp2] + m 
        if len(x) == 1: 
            break
    return x[0] 


class base_exponent_pair:
    def __init__(self, base, exponent):
        self.base = int(base)
        self.exponent = int(exponent)
    def increment_exponent(self):
        self.exponent += 1
        
    def get_value(self):
        return self.base ** self.exponent

class list_of_base_exponent_pairs:
    bep_list = []

    def add_base(self, base):
        for x in self.bep_list:
            if x.base == base:
                #print(str(base) + ' INCREMENTED')
                x.increment_exponent()
                return
        self.bep_list.append(base_exponent_pair(base, 1))
        #print(str(base) + ' NEWLY ADDED')
        
    def print_product(self):
        for pair in self.bep_list:
            print('(' + str(pair.base) + '^' + str(pair.exponent) + ')', end = '') 
        print()
        
    def print_to_be_determined(self):
        for pair in self.bep_list:
            print('     x_' + str(pair.base) + ' ≡ ' + 'x mod(' + str(pair.base) + '^' + str(pair.exponent) + ')')
        print()
    


    
    def determine_numbers(self, a, b, p):
        print('     ------------------------------------------')
        
        generators = []
        mods = []
        
        for pair in self.bep_list:
            print('     > base: ' + str(pair.base))
            print('     > power: ' + str(pair.exponent) + '\n')
            print('     for : q = ' + str(pair.base))
            print('     x = ', end = '')
            for x in range(pair.exponent):
                if not x == 0:
                    print(' + ' + str(pair.base ** x) + '*', end = '')    
                print('x_' + str(x), end = '')
            print('\n')

            beta = b
            
            x_underscores_founds = []
            
            for x in range(pair.exponent):
                print('     x_' + str(x) + ' :')
                print('         b^((p-1)/(q_' + str(x) + ')) = a^(((p-1)/q)*x_' + str(x) + ')')
                print('         ' + str(beta) + '^(' + str(p-1) + '/' + str(pair.base ** (x+1)) + ') = ' + str(a) + '^(' + str(p-1) + '/' + str(pair.base) + '*x_' + str(x) + ')')
                #print('         ' + str(b) + '^(' + str((p-1)/(pair.base ** (x+1))) + ') = ' + str(a) + '^(' + str((p-1)/pair.base) + '*x_' + str(x) + ')')
                beta_expo = (beta**int(((p-1)/(pair.get_value())))) % p
                alpha_expo = (a**int((p-1)/(pair.get_value()))) % p
                print('         ' + str(beta_expo) + ' (mod ' + str(p) + ') = ' + str(alpha_expo) + '^(x_' + str(x) + ') (mod ' + str(p) + ')')
                print('         > Finding x_' + str(x) + '...')
                x_underscore = 0
                while (beta_expo % p) != ((alpha_expo**x_underscore) % p):
                    x_underscore += 1
                    #print(((alpha_expo**x_underscore) % p))
                    
                print('         > x_' + str(x) + ' = ' + str(x_underscore))
                x_underscores_founds.append(x_underscore)
                if (x+1) != pair.exponent :
                    new_beta = 0
                    while (beta != ((a**x_underscore)*new_beta)%p):
                        new_beta += 1
                    beta  = new_beta
                    print('NEW BETA : ' + str(beta) + ' mod ' + str(p))
                    
            print('     Recall : ')
            print('         x = ', end = '')
            for x in range(pair.exponent):
                if not x == 0:
                    print(' + ' + str(pair.base ** x) + '*', end = '')    
                print('x_' + str(x), end = '')
            print()
            
            print('         x = ', end = '')
            
            x_sum = 0
            for x in range(pair.exponent):
                if not x == 0:
                    print(' + ' + str(pair.base ** x) + '*', end = '')    
                print(x_underscores_founds[x], end = '')
                x_sum += (x_underscores_founds[x] * (pair.base ** x))
            print()
            x_sum = x_sum % pair.get_value()
            print('         x = ' + str(x_sum) + ' mod(' + str(pair.get_value()) + ')')
            generators.append(x_sum)
            mods.append(pair.get_value())
            print('     ------------------------------------------')
        x_final = crt(mods, generators) % (p - 1)
        print('X FINAL : ' + str(x_final))
        print('Hence ' + str(b) + ' = ' + str(a) + '^(' + str(x_final) + ') (mod ' + str(p) + ')\n')
        print(b == (a**x_final) % p)
        
def find_prime_factors_of(number):
    prime_factors = list_of_base_exponent_pairs()
 
    while number % 2 == 0: 
        prime_factors.add_base(2)
        number = number / 2
          
    for i in range(3,int(math.sqrt(number))+1,2): 
        while number % i== 0: 
            prime_factors.add_base(i)
            number = number / i 

    if number > 2: 
        prime_factors.add_base(number)  

    return prime_factors


def pohlighellman(a, b, p):
    # Problem stated.
    print('\nSolving : ' + str(b) + ' = ' + str(a) + '^(x) (mod ' + str(p) + ')\n')

    # 1. Find prime factors of (public_modulus - 1)
    print('> Finding prime factors of (p - 1) = ' + str(p-1) + '.\n')
    prime_factors = find_prime_factors_of(p - 1)
    print('> Prime factors found.')
    print('     (p - 1) = ' + str(p - 1) + ' = ', end = '')
    prime_factors.print_product()
    print()
    # 2. Determine x_b values.
    print('> We shall determine the numbers : ')
    prime_factors.print_to_be_determined()
    print('> Determination process : ')
    prime_factors.determine_numbers(a, b, p)

# Start
#pohlighellman(3, 22, 31)
#pohlighellman(7, 12, 41)
#pohlighellman(5, 22, 53)
pohlighellman(7, 166, 433)




















