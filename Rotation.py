"""
General tools for homework involving rotation ciphers.
:author: Nick Patel
:language: Python3.7
"""


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


def main():
    """
    Driver to bruteforce words using a rotation cipher.
    :return: None
    """
    l = list()
    s = set()
    with open('Resources/dictionary.txt') as f:
        for line in f:
            s.add(line.strip())

    valid = []
    for e in s:
        if len(e) < 4:
            continue
        for i in range(1,25):
            rot = rot_n(e, i)
            if rot in s:
                valid.append((e, rot, i))
                print("word: ", e, " new: ", rot, " rotation: ", i)
                #print(e, '$\\rightarrow$', rot, ' with rotation: ', i, '\\newline') # Provides LaTeX syntax


if __name__ == "__main__":
    main()
