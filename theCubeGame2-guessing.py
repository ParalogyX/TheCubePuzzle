# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 14:43:48 2020

@author: vpe
"""
import copy


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

    new_setup = copy.deepcopy(current_setup)
    new_setup[row][col] = '0'
    return new_setup

def max_moves(lenght):

    i = 0
    
    k = 10**lenght
    for kCount in range(lenght + 1):
        while len(base10toN(int(i),6)) < lenght + 1:
            i += k
        
        #debug comments
# =============================================================================
#         
#         print ("kCount: ", kCount)
#         print ("lenght: ", len(base10toN(int(i),6)))
#         print("k: ", k)
#         print ("i: ", i)
#         print ("max result + 1: ", base10toN(int(i),6))
#         print ("max result: ", base10toN(int(i - 1),6))
# =============================================================================
        
        i -= k
        k /= 10
        k = int(k)
    
    return i


def move_generator (index):
    string = str (base10toN (index, 6)).zfill(36)

    result = [int(string) for string in string]
    
    #result = []
    #result = int(d) for d in str(n)
    return result

def dec2hex(num):
    if num == 0:
        return 0
    ans = ""
    while num > 0:
        ans = str(num%6) + ans
        num /= 6
    return int(ans)       

def base10toN(num, base):
    """Change ``num'' to given base
    Upto base 36 is supported."""

    converted_string, modstring = "", ""
    currentnum = num
    if not 1 < base < 37:
        raise ValueError("base must be between 2 and 36")
    if not num:
        return '0'
    while currentnum:
        mod = currentnum % base
        currentnum = currentnum // base
        converted_string = chr(48 + mod + 7*(mod > 10)) + converted_string
    return converted_string

def isDone(current_setup):
    for i in range (6):
        line = current_setup[i]
        if all(elem == '0' for elem in line):
            return True
        else:
            return False


def find_solution_guessing(current_setup):
        
    #diffetent start position
    for x in range (6):
        for y in range (6):
            for movesSel in range (max_moves(36)):
                next_move = move_generator(movesSel)
                #new_setup = [] 
                #new_setup.extend(current_setup)
                new_setup = copy.deepcopy(current_setup)
                num = selectable_number(new_setup, x, y) 
                sel = selectable(new_setup, x, y)
                new_setup = select(new_setup, x, y)
                
                for i in range(36):
                    
                    #second move (next_move[1]) = 0
                    curr_move = next_move[i]
                    #curr_move = 0
                    num = selectable_number(new_setup, sel[curr_move][0], sel[curr_move][1])
                    #num = 
                    sel = selectable(new_setup, sel[curr_move][0], sel[curr_move][1])
                    
                    
                    if num == 0 and not isDone(new_setup):
                        print ("moves: ", next_move, ", started on x = ", x, " and y = ", y, " are compromised")
                        break
                
                    if  isDone(new_setup):
                        print ("Please start on x = ", x, " and y = ", y, " and use moves: ", next_move)
                
                    new_setup = select(new_setup, sel[curr_move][0], sel[curr_move][1])
                    
                    
                    
def check_solution(current_setup, start, moves, moves_number = 36):
    """
    

    Parameters
    ----------
    current_setup : setup
        DESCRIPTION.
    start : [x, y]
        DESCRIPTION.
    moves : moves
        DESCRIPTION.
    moves_number : int, optional
        DESCRIPTION. The default is 36.

    Returns
    -------
    movesLeft : int
        36 - moves done before stacked.

    """
    
    new_setup = copy.deepcopy(current_setup)
    x = start[0]
    y = start[1]
    num = selectable_number(new_setup, x, y) 
    sel = selectable(new_setup, x, y)
    new_setup[x][y] = '0'
    #debug print
    print ("selected start point")
    for k in range(6):
        print (new_setup[k])
    print()
    
    print ("num after first move: ", num)
    print ("sel after first move: ", sel)
    movesLeft = moves_number
    print ("moves left", movesLeft)
    
    for i in range (len(moves)):
        curr_move = moves[i]
        print (i + 1, " move: ", curr_move)
        print ("current setup")
        for k in range(6):
            print (new_setup[k])
        print()
        
        num = selectable_number(new_setup, sel[curr_move][0], sel[curr_move][1])
        sel = selectable(new_setup, sel[curr_move][0], sel[curr_move][1])
        print ("num before ", i + 1, " move: ", num)
        print ("sel before ", i + 1, " move: ", sel)
        if num != 0:
            movesLeft -= 1
            #there are less possible moves, when in "DNA". Need to be solved!!!
            new_setup = select(new_setup, sel[curr_move][0], sel[curr_move][1])
            print ("setup after ", i + 1, " move")
            for k in range(6):
                print (new_setup[k])
            print()
            
            print ("moves left", movesLeft)
            
        else:
            print ("num = 0")
            break
        
    return movesLeft


def find_solution_iter(current_setup):
    new_setup = current_setup
    next_move = []
    for i in range(36):
        next_move.append(0)
        
    
            #next_move[len(next_move)] += 1
    
        
     
    for i in range(36):
        for j in range(6):
            next_move[len(next_move)] += 1
        next_move[len(next_move)] = 0
        next
     
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
            
            
            print ("num after ", i," move: ", num)
            #print ("new_num after ", i," move: ", new_num)
            print ("sel after ", i," move: ", sel)
            print ("new_sel after ", i," move: ", new_sel)
            print ("next_move after ", i," move: ", next_move)
          
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
    
        
        
        print ("All done: ", all_done())
    
    return next_move

#print(dec2hex(78))        
#find_solution_guessing(copy.deepcopy(setup))
#find_solution_guessing(setup.copy())
    
moves = move_generator (1237678234231928716247634234234)

print(moves)

test = check_solution(setup, [0, 0], moves)

print (test)

#print (find_solution_iter(setup))

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
                