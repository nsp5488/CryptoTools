"""
Solver for cipher1, which is a simple cipher.
"""


def main():
    """
    Driver for the solver.
    :return: None
    """
    s = ''
    with open('p1.txt') as file:
        for line in file:
            s += line.replace('\n', '')
    newS = ''
    for ch in s:
        if ch.isalpha():
            newS += ch

    num = '7876565434321123434565678788787656543432112343456567878878765654433211234'
    output = ''

    for i in range(len(newS)//8):

        output += newS[(i * 8) + int(num[i]) - 1]
    print(output)


if __name__ == "__main__":
    main()
