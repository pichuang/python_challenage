__author__ = 'roan'

"""
http://www.pythonchallenge.com/pc/return/sequence.txt
https://oeis.org/search?q=1%2C+11%2C+21%2C+1211%2C+111221&language=english&go=Search
"""


def A005150(n):
    seq = [1] + [None] * (n - 1) # allocate entire array space

    def say(s):
        acc = '' # initialize accumulator
        while s:
            i = 0
            c = s[0]  # char of first run
            while i < len(s) and s[i] == c:  # scan first digit run
                i += 1
            acc += str(i) + c  # append description of first run
            if i == len(s):
                break  # done
            else:
                s = s[i:]  # trim leading run of digits
        return acc
    for i in range(1, n):
        seq[i] = int(say(str(seq[i-1])))
    return seq

ANSWER = 30
print(str(A005150(ANSWER+1)[ANSWER]).__len__())
