# -*- coding: utf-8 -*-

import sys

'''

'''

def func():
    '''

    '''
    n = int(raw_input())

    for i in range(n):
        numstr1, numstr2 = raw_input().split()
        
        num1 = 0
        for index, c in enumerate(numstr1):
            if c == 'm':
                if index != 0 and numstr1[index-1].isdigit():
                    num1 += int(numstr1[index-1]) * 1000
                else:
                    num1 += 1000
            if c == 'c':
                if index != 0 and numstr1[index-1].isdigit():
                    num1 += int(numstr1[index-1]) * 100
                else:
                    num1 += 100
            if c == 'x':
                if index != 0 and numstr1[index-1].isdigit():
                    num1 += int(numstr1[index-1]) * 10
                else:
                    num1 += 10

            if c == 'i':
                if index != 0 and numstr1[index-1].isdigit():
                    num1 += int(numstr1[index-1])
                else:
                    num1 += 1

        num2 = 0
        for index, c in enumerate(numstr2):
            if c == 'm':
                if index != 0 and numstr2[index-1].isdigit():
                    num2 += int(numstr2[index-1]) * 1000
                else:
                    num2 += 1000
            if c == 'c':
                if index != 0 and numstr2[index-1].isdigit():
                    num2 += int(numstr2[index-1]) * 100
                else:
                    num2 += 100
            if c == 'x':
                if index != 0 and numstr2[index-1].isdigit():
                    num2 += int(numstr2[index-1]) * 10
                else:
                    num2 += 10

            if c == 'i':
                if index != 0 and numstr2[index-1].isdigit():
                    num2 += int(numstr2[index-1])
                else:
                    num2 += 1

        s = num1 + num2
        sstr = ''

        if s / 1000 == 0:
            pass
        elif s / 1000 == 1:
            sstr += 'm'
        else:
            sstr += str(s / 1000) + 'm'
                    
        if (s / 100) % 10 == 0:
            pass
        elif (s / 100) % 10 == 1:
            sstr += 'c'
        else:
            sstr += str((s / 100) % 10) + 'c'

        if (s / 10) % 10 == 0:
            pass
        elif (s / 10) % 10 == 1:
            sstr += 'x'
        else:
            sstr += str((s / 10) % 10) + 'x'
        
        if s % 10 == 0:
            pass
        elif s % 10 == 1:
            sstr += 'i'
        else:
            sstr += str(s % 10) + 'i'

        print sstr


if __name__ == '__main__':
    func()
    