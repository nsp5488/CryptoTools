"""
Solver for an Affine Cipher. Provide alpha and beta, and solve will return the plaintext.
:author: Nick Patel nsp5488@rit.edu
:language: python3.7
"""

CIPHER_TEXT = "./Resources/CipherTexts/cipher3"


def solve(aInv, b, ciphertext):
    """
    Solves :ciphertext using simple substitutions.
    :param aInv:
    :param b:
    :param ciphertext:
    :return:
    """
    outStr = ''
    with open(ciphertext) as f:
        for line in f:
            for ch in line:
                if ch != ' ':
                    outStr += chr(((aInv*(ord(ch) - 65) - b) % 26) + 65).lower()
    return outStr


def find_mult_inv(a):
    """
    Brute force calculates the multiplicative inverse of :a: modulo 26.
    :param a: in place of alpha for the Affine Cipher.
    :return: The multiplicative inverse of :a:
    """
    for i in range(26):
        if (i*a) % 26 == 1:
            return i


def main():
    """
    Driver for affineSolver.
    :return:
    """
    a = int(input("Enter alpha: "))
    b = int(input("Enter beta: "))
    aInv = find_mult_inv(a)

    print(solve(aInv,b, CIPHER_TEXT))


if __name__ == "__main__":
    main()
