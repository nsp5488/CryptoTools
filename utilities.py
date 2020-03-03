"""
A collection of utility functions useful in solving cryptographic problems
:author: Nick Patel nsp5488@rit.edu
"""


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

