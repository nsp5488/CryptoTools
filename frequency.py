"""
A frequency analysis tool developed to aid in decrypting ciphers.
:author: Nick Patel nsp5488@rit.edu
:language: python3.7
"""

CIPHER_FILE = "./Resources/CipherTexts/cipher3"
SUBSTITUTION_FILE = './Resources/subs'


def report(dct, n, type):
    """
    Handles the generation and printing of the report.
    :param dct: Maps a given key to the number of occurrences in the ciphertext. (Map[symbol->frequency])
    :param n: The number of symbol->frequency pairs to print.
    :param type: The type of symbol (monogram, digrams, trigrams...)
    :return: None
    """
    most_freq = []
    for k in dct:
        most_freq.append((k, dct[k]))

    most_freq.sort(key=lambda x: x[1], reverse=True)

    print("The", n, "most frequent", type, "are: ", end='')
    for i in range(n):
        print(most_freq[i], end=' ')


def substitute(string, key):
    """
    Substitutes ciphertext according to :key:.
    :param string: The ciphertext to substitute in to.
    :param key: The key to substitute into the ciphertext.
    :return: The ciphertext with the substitutions from :key: made.
    """
    new_string = ''
    for ch in string:
        if ch in key:
            new_string += key[ch]
        else:
            new_string += ch
    return new_string


def freq(cipherfile):
    """
    Counts occurrences of monograms, digrams, trigrams, and quadgrams in :cipherfile: and generates a report for each.
    :param cipherfile: Encrypted text.
    :return: None
    """
    prev = []
    totals = dict()
    digrams = dict()
    trigrams = dict()
    quadgrams = dict()
    with open(cipherfile) as file:
        for line in file:
            line = line.strip()
            lst = line.split(' ')
            for e in lst:
                for ch in e:
                    if len(prev) > 1:
                        if prev[len(prev) - 1] + ch in digrams:
                            digrams[prev[len(prev) - 1] + ch] += 1
                        else:
                            digrams[prev[len(prev) - 1] + ch] = 1
                    if len(prev) > 2:
                        if prev[len(prev) - 2] + prev[len(prev) - 1] + ch in trigrams:
                            trigrams[prev[len(prev) - 2] + prev[len(prev) - 1] + ch] += 1
                        else:
                            trigrams[prev[len(prev) - 2] + prev[len(prev) - 1] + ch] = 1
                    if len(prev) > 3:
                        if prev[len(prev)-3] + prev[len(prev) - 2] + prev[len(prev) - 1] + ch in trigrams:
                            quadgrams[prev[len(prev)-3] + prev[len(prev) - 2] + prev[len(prev) - 1] + ch] += 1
                        else:
                            quadgrams[prev[len(prev)-3] + prev[len(prev) - 2] + prev[len(prev) - 1] + ch] = 1

                    if ch in totals:
                        totals[ch] += 1
                    else:
                        totals[ch] = 1

                    prev.append(ch)
    report(totals, 10, 'monograms')
    print()
    report(digrams, 10, 'digrams')
    print()
    report(trigrams, 10, 'trigrams')
    print()
    report(quadgrams, 10, 'quadgrams')


def main():
    """
    Driver for frequency.py
    :return: None
    """
    freq(CIPHER_FILE)
    string = ''
    with open(CIPHER_FILE) as file:
        for line in file:
            string += line.replace(' ', '').strip()

    key = dict()

    with open(SUBSTITUTION_FILE) as subs:
        for line in subs:
            lst = line.strip().split(' ')
            key[lst[0]] = lst[1]

    print()
    print('original:   ', string)
    print('substituted:', substitute(string, key))


if __name__ == "__main__":
    main()
