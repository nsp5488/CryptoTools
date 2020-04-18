"""
A collection of utility functions useful in solving cryptographic problems
:author: Nick Patel nsp5488@rit.edu
"""
import collections
import math


def find_mult_inv(a):
    """
    Brute force calculates the multiplicative inverse of :a: modulo 26.
    :param a: in place of alpha for the Affine Cipher.
    :return: The multiplicative inverse of :a:
    """
    for i in range(26):
        if (i*a) % 26 == 1:
            return i


def rot_n(word, n):
    """
    Rotates word by n
    :param word: The plaintext
    :param n: The rotation parameter (beta)
    :return:
    """
    new = ""
    for ch in word:
        new += chr((ord(ch) + n))
    return new


def gcd(a, b):
    """
    Computes the gcd of two numbers using the Euclidean Algorithm.
    :param a: The first number to compute GCD of.
    :param b: The second number to compute GCD of.
    :return: The GCD of a, b
    """
    while b:
        a, b = b, a % b
    return a


def phi(a):
    """
    Computes the Euler's Totient Function of a number, a, which represents the number of invertible elements modulo a.
    :param a: The number to compute the Totient function of.
    :return: The number of invertible elements modulo a.
    """
    b = a-1
    c = 0
    while b:
        if not gcd(a, b)-1:
            c += 1
        b -= 1
    return c


def sieve(n):
    """
    An efficient implementation of the Sieve of Eratosthenes to find all prime numbers up to a given input, :n:.
    :param n: The upper bound to determine primes.
    :return: A list of all prime integers from 2..n.
    """
    sieve_list = [True for i in range(n + 1)]
    sieve_list[0] = False
    sieve_list[1] = False
    init = 2
    while init * init <= n:
        if sieve_list[init]:
            for i in range(init * init, n + 1, init):
                sieve_list[i] = False
        init += 1

    out = [i for i, e in enumerate(sieve_list) if e]

    return out


def print_alphabet_numerical():
    """
    Prints out a conversion table from uppercase English letters to integers in the range [0..25].
    :return: None
    """
    for i in range(26):
        if i < 10:
            print(chr(i+65), end=' ')
        else:
            print(chr(i+65), end='  ')
    print()
    for i in range(26):
        print(i, end=' ')


def convert_to_nums(string):
    """
    Converts an English string to its numeric representation
    :param string: The string to convert
    :return: The numeric string.
    """
    out = ''
    for ch in string:
        i = ord(ch) - 65
        out += ch(i) + ' '
    return out


def baby_step_giant_step(h, g, p):
    """
    Implementation of Shank's Baby-Step-Giant-Step Algorithm to solve the DLP (h = g**m (mod p)) efficiently.
    :param h: The target number.
    :param g: A generator of the group or field.
    :param p: The prime modulus.
    :return: m, such that g**m = h, if such an m exists; else, None
    """
    # Only do this computation once.
    n = math.floor(math.sqrt(p))
    baby_steps = collections.defaultdict()

    for i in range(1, n-1):
        # Compute the 'Baby-Step'
        baby_step = g**i % p
        baby_steps[baby_step] = i

    for i in range(1, n):
        exp = (-i * n) % (p-1)  # Reduce the exponent using Euler's Theorem.
        giant_step = h*(g**exp) % p  # Compute the 'Giant-Step'

        if giant_step in baby_steps:
            return i*n+baby_steps[giant_step]
    return None


def find_prime_factors(n):
    """
    Returns the prime factorization of n as a list.
    :param n: The input number to factorize.
    :return: A list of prime factors.
    """
    i = 2
    factors = []
    while i * i < n:
        if n % i == 0:
            factors.append(i)
        while n % i == 0:
            n /= i
        i += 1
    factors.append(int(n))
    return factors


def is_generator(g, p, prime_factors):
    """
    Checks if a given number, g, is a generator for the group Z/[p] efficiently using the prime factorization of phi(p)
    :param g: The generator to check
    :param p: The prime modulus of the group in which we are working.
    :param prime_factors: A list of prime factors of phi(p).
    :return: True if <g> = Z/[p]; else, false.
    """
    if prime_factors is None:
        prime_factors = find_prime_factors(p-1)

    for factor in prime_factors:
        k = int(g**((p-1)//factor) % p)
        if k == 1:
            return False

    return True


def find_generators(p):
    """
    Finds all generators for a cyclic group using the property that 1 generator can generate all other generators using
    ord(g**k) = s/gcd(s, k) => if gcd(s,k) == 1 then we have that g**k is a generator for Z/[p]
    :param p: The modulus of the group that we are dealing with.
    :return: A list of the group's generators
    """
    factors = find_prime_factors(phi(p))
    generators = []
    for i in range(1, p-1):
        if is_generator(i, p, factors):
            break

    g = i
    for k in range(p-1):
        if gcd(k, p-1) == 1:
            generators.append(g**k % p)

    return sorted(generators)
