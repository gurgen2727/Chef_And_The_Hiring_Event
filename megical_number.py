#!/usr/bin/env python
import sys

# sys.stdin = open('in.txt')
T = input()

# 0 2 4 6 8 20 22 24 26 28

while T > 0:
    T -= 1
    K = input() - 1  # starting from 0
    if K == 0:
        sys.stdout.write('0\n')
    else:
        base5nbr = ''
        while K > 0:
            base5nbr = {0: '0',
                        1: '2',
                        2: '4',
                        3: '6',
                        4: '8'}[K % 5] + base5nbr
        K /= 5
    sys.stdout.write('%s\n' % base5nbr)

