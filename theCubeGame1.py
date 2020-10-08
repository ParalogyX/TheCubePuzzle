# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 14:43:48 2020

@author: vpe
"""

setup = [['>', 'V', 'V', '<', '<', 'V'], 
         ['>', '>', '>', 'V', 'V', 'V'],
         ['>', 'V', 'V', '^', '<', '<'],
         ['^', '>', '^', '<', '^', '<'],
         ['^', '^', '<', '>', '<', '^'],
         ['^', '>', '>', '^', '^', '<']]

for i in range(6):
    print (setup[i])
print()
def selectable (current_setup, row, col):
    result =[]
    if current_setup[row][col] == '>':
        for cur_col in range(6):
            if cur_col > col and current_setup[row][cur_col] != '0':
                result.append([row, cur_col])
    elif current_setup[row][col] == '<':
        for cur_col in range(6):
            if cur_col < col and current_setup[row][cur_col] != '0':
                result.append([row, cur_col])
    elif current_setup[row][col] == '^':
        for cur_row in range(6):
            if cur_row < row and current_setup[cur_row][col] != '0':
                result.append([cur_row, col]) 
    elif current_setup[row][col] == 'V':
        for cur_row in range(6):
            if cur_row > row and current_setup[cur_row][col] != '0':
                result.append([cur_row, col])     
    else:
        print ("wrong selected")
        return 0
    return result


def selectable_number (current_setup, row, col):
    result = 0
    if current_setup[row][col] == '>':
        for cur_col in range(6):
            if cur_col > col and current_setup[row][cur_col] != '0':
                result += 1    
    elif current_setup[row][col] == '<':
        for cur_col in range(6):
            if cur_col < col and current_setup[row][cur_col] != '0':
                result += 1
    elif current_setup[row][col] == '^':
        for cur_row in range(6):
            if cur_row < row and current_setup[cur_row][col] != '0':
                result += 1 
    elif current_setup[row][col] == 'V':
        for cur_row in range(6):
            if cur_row > row and current_setup[cur_row][col] != '0':
                result += 1     
    else:
        print ("wrong selected")
        return 0
    return result

def select (current_setup, row, col):

    new_setup = current_setup
    new_setup[row][col] = '0'
    return new_setup



def find_solution_iter(current_setup):
    new_setup = current_setup
    next_move = []
    for i in range(36):
        next_move.append(0)
        
        
    #first move
    num = selectable_number(new_setup, 0, 0) 
    sel = selectable(new_setup, 0, 0)
    #num = 5
    #sel = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]] = first line
    new_setup = select(new_setup, 0, 0)
    
    for k in range(6):
        print (new_setup[k])
    print()
    
#other 35 moves    
    for i in range(1, 36):
        #second move (next_move[1]) = 0
        curr_move = next_move[i]
        #curr_move = 0
        num = selectable_number(new_setup, sel[curr_move][0], sel[curr_move][1])
        #num = 
        new_sel = selectable(new_setup, sel[curr_move][0], sel[curr_move][1])
        #new_sel = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1]] = second row
        while num == 0 and next_move[i] < 5:
            next_move[i] += 1
            curr_move = next_move[i]
            num = selectable_number(new_setup, sel[curr_move][0], sel[curr_move][1])
            new_sel = selectable(new_setup, sel[curr_move][0], sel[curr_move][1])
        
        new_setup = select(new_setup, sel[curr_move][0], sel[curr_move][1])
        sel = new_sel
        
        
        
# =============================================================================
#         sel = selectable(new_setup, 0, next_move[i])
#         while sel == 0 and next_move[i] < 5:
#             next_move[i] += 1
#             sel = selectable(new_setup, 0, next_move[i])
#         new_setup = select(new_setup, 0, next_move[i])
#         curr_move = next_move[i]
#         new_setup = select(new_setup, sel[curr_move][0], sel[curr_move][1])
#         
# =============================================================================
        for k in range(6):
            print (new_setup[k])
        print()
    return next_move
        

print (find_solution_iter(setup))

# =============================================================================
# num = selectable_number(setup, 2, 3)
# sel = selectable(setup, 2, 3)
# print (num) 
# print (sel) 
# for i in range(num):
#     print (setup[sel[i][0]][sel[i][1]])
# 
# current_setup = select(setup, 2, 3)       
# 
# for i in range(6):
#     print (setup[i]) 
# for i in range(num):     
#     new_num = selectable_number(setup, sel[i][0], sel[i][1])
#     new_sel = selectable(setup, sel[i][0], sel[i][1])
#     print (new_num) 
#     print (new_sel) 
# #for i in range (selectable_number(setup, 0, 0):
# =============================================================================
                