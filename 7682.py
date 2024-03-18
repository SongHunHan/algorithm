## 단순 구현 

import sys
def input():
    return sys.stdin.readline().rstrip()

while True:
    s_input = input()
    if s_input == 'end':
        break
    
    x_cnt = 0
    o_cnt = 0
    for i in s_input:
        if i == 'X':
            x_cnt += 1
        elif i=='O':
            o_cnt += 1

    check_line = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    o_flag = False
    x_flag = False
    for each_line in check_line:
        if s_input[each_line[0]] == s_input[each_line[1]] and s_input[each_line[0]] == s_input[each_line[2]]:
            if s_input[each_line[0]] != '.':
                if s_input[each_line[0]] == 'O':
                    o_flag = True
                else:
                    x_flag = True
    if x_cnt - o_cnt > 1:
        print("invalid")
    else:
        if x_flag and o_flag:
            print("invalid")
        elif x_flag:
            print('valid')
        elif o_flag and x_cnt - o_cnt == 0:
            print('valid')
        elif not x_flag and not o_flag and '.' not in s_input and x_cnt-o_cnt==1:
            print('valid')
        else:
            print('invalid')


    
        