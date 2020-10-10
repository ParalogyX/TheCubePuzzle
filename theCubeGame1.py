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


print ("Original setup: ")
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
    print ("setup after first move: ")
    for k in range(6):
        print (new_setup[k])
    print()
    
    print ("num after first move: ", num)
    print ("sel after first move: ", sel)
    print ("next_move after first move: ", next_move)
    
#other 35 moves  
    all_done = False
    while not all_done:  
        for i in range(1, 36):
            
            #second move (next_move[1]) = 0
            curr_move = next_move[i]
            #curr_move = 0
            num = selectable_number(new_setup, sel[curr_move][0], sel[curr_move][1])
            #num = 
            new_sel = selectable(new_setup, sel[curr_move][0], sel[curr_move][1])
            #new_sel = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1]] = second row
            while num == 0 and next_move[i] < 5:
                print ("num == 0, increase next_move[", i, "]: ")
                
                next_move[i] += 1
                curr_move = next_move[i]
                print ("next_move: ", next_move)
            
                num = selectable_number(new_setup, sel[curr_move][0], sel[curr_move][1])
                
                new_sel = selectable(new_setup, sel[curr_move][0], sel[curr_move][1])
                print ("num after increasing next_move[", i,"]: ", num)
                print ("new_sel after increasing next_move[", i,"]: ", new_sel)
            if num == 0 and next_move[i] >= 5:
                print ("change ", i, " + 1 move")
                next_move[i-1] += 1
                print ("next_move: ", next_move)
                break
            
            
            new_setup = select(new_setup, sel[curr_move][0], sel[curr_move][1])
            sel = new_sel
            
            for k in range(6):
                print (new_setup[k])
            print()
          
            for i in range (6):
                line = new_setup[i]
                if all(elem == '0' for elem in line):
                    all_done = True
                else:
                    all_done = False
                    break

        if all_done:
            print ('Done')
            print (next_move)
            
        
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
    
    print ("num after ", i," move: ", num)
    #print ("new_num after ", i," move: ", new_num)
    print ("sel after ", i," move: ", sel)
    print ("new_sel after ", i," move: ", new_sel)
    print ("next_move after ", i," move: ", next_move)
    
    print ("All done: ", all_done())
    
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
                