#! /usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

def fibonacii(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('num', help = 'Calculate the fabonacci number.', type = int)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-v', '--verbose', action = 'store_true')
    group.add_argument('-q', '--quiet', action = 'store_true')
    parser.add_argument('-o', '--output', help = 'Output the result to a file', action = 'store_true')
    args = parser.parse_args()
    result = fibonacii(args.num)

    if args.verbose:
        print 'The fibonacii number of %d is %d' %(args.num, result)
    elif args.quiet:
        print 'result: ', result
    else:
        print "fibonacii(%d) is %d" %(args.num, result)

    if args.output:
        with open('fibonacii.txt', 'a') as f:
            f.write('The result is: ' + str(result) + '\n')

if __name__ == '__main__':
    main()
