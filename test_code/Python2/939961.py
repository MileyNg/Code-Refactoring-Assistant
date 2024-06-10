# -*- coding: utf-8 -*-

import sys

'''

'''

def func():
    '''

    '''
    while True:
        n = int(raw_input())
        if n == 0:
            break

        # line_0
        m = int(raw_input())
        standard_positions = []
        standard_lines = []
        standard_reverse_lines = []

        for pos_num in range(m):
            x, y = map(int, raw_input().split())
            standard_positions.append([x, y])

        for num in range(m-1):
            line = [0, 0]
            if standard_positions[num][0] < standard_positions[num+1][0]:
                line = [0, standard_positions[num+1][0] - standard_positions[num][0]]
            elif standard_positions[num][0] > standard_positions[num+1][0]:
                line = [2, standard_positions[num][0] - standard_positions[num+1][0]]
            else:
                if standard_positions[num][1] < standard_positions[num+1][1]:
                    line = [1, standard_positions[num+1][1] - standard_positions[num][1]]
                elif standard_positions[num][1] > standard_positions[num+1][1]:
                    line = [3, standard_positions[num][1] - standard_positions[num+1][1]]
            standard_lines.append(line)

        for index in range(len(standard_lines)):
            reverse_line = [(standard_lines[-1-index][0] + 2) % 4, standard_lines[-1-index][1]]
            standard_reverse_lines.append(reverse_line)

        # print standard_positions
        # print standard_lines
        # print standard_reverse_lines

        # line_1 - line_n
        for data_num in range(n):
            m = int(raw_input())
            positions = []
            lines = []
            for pos_num in range(m):
                x, y = map(int, raw_input().split())
                positions.append([x, y])
            for num in range(m-1):
                line = [0, 0]
                if positions[num][0] < positions[num+1][0]:
                    line = [0, positions[num+1][0] - positions[num][0]]
                elif positions[num][0] > positions[num+1][0]:
                    line = [2, positions[num][0] - positions[num+1][0]]
                else:
                    if positions[num][1] < positions[num+1][1]:
                        line = [1, positions[num+1][1] - positions[num][1]]
                    elif positions[num][1] > positions[num+1][1]:
                        line = [3, positions[num][1] - positions[num+1][1]]
                lines.append(line)

            for offset in range(4):
                for line in lines:
                    line[0] = (line[0] + offset) % 4
                if lines == standard_lines or lines == standard_reverse_lines:
                    print data_num + 1
            
        print '+++++'
            


                        

    return None

if __name__ == '__main__':
    func()
    