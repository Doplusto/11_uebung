#!/usr/bin/python3.7

from random import randint
from termcolor import colored


# Fancy solution
def print_tree(n):
    for i in range(n):
        s = ('x'  * (i*2-1)).center(n*2)
        # Print Top
        if i == 1:
            print(colored(s.replace('x', 'X'), 'yellow'))
            continue
        color_str = []
        # Make tree green with randomly selected red 'x'
        for j in range(n*2):
            color_str.append(colored(s[j], 'red')
                             if j % randint(3, 12) == 0
                             else colored(s[j], 'green', attrs=['dark']))
        print(''.join(color_str))
    # Print trunk
    for i in range(int(n/4)):
        s = '|' + '|' * int(n/3)
        s = s.center(n*2)
        print(colored(s , 'yellow', attrs=['dark']))


# Tail recursive solution
def print_tree_rec_help(n, i):
    print(('x' * i).center(n))
    if i+2 <= n:
        print_tree_rec_help(n, i+2)


def print_tree_rec(n):
    print_tree_rec_help(n, 1)

print_tree_rec(20)
print_tree(20)
