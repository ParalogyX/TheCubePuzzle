# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 14:01:53 2020

@author: Vladimir
"""

from theCubeGame2check import *
import time

setup = [['>', 'V', 'V', '<', '<', 'V'], 
          ['>', '>', '>', 'V', 'V', 'V'],
          ['>', 'V', 'V', '^', '<', '<'],
          ['^', '>', '^', '<', '^', '<'],
          ['^', '^', '<', '>', '<', '^'],
          ['^', '>', '>', '^', '^', '<']]
# setup = [['>', 'V', 'V', '<', '<', 'V'], 
#         ['>', '^', '^', '^', 'V', '^'],
#         ['>', '^', '^', '^', '<', 'V'],
#         ['^', '^', '^', '<', '^', '<'],
#         ['^', '^', '^', '>', '<', '^'],
#         ['^', '^', '^', '^', '^', '^']]

globCounter = 0


def matrixToLine(curr_setup):
    result = []
    for i in range (6):
        for j in range (6):
            result.append(curr_setup[i][j])   
    return result

def tryMoveRecurs(curr_setup, moves, moves_done, memoDeadEnds = {}):
    global globCounter
    globCounter += 1
    if len(moves) == 0:
        return "Empty"
    new_setup = copy.deepcopy(curr_setup)
    queue = moves
    move = queue.pop(0)
    #move = tuple(move)
        
    if tuple(move) in memoDeadEnds.keys():
        if memoDeadEnds[tuple(move)] == new_setup:
            #del queue[-1]
            if len(queue) == 0:
                return "Empty"
            move = queue.pop(0)
            #move = tuple(move)
    
    t1 = move[0]
    t2 = move[1]

    tst = new_setup[t1][t2]

    # if new_setup[move[0]][move[1]] == '0':
    #     # print ("move: ", move, " 0: ", move[0], " 1: ", move[1])
    #     # print (new_setup[move[0]][move[1]])
    #     # print (setup[move[0]][move[1]])
    #     new_setup[move[0]][move[1]] = setup[move[0]][move[1]]       #!!!Reading of global var
    #     # print (new_setup[move[0]][move[1]])
    #     # print (setup[move[0]][move[1]])
    #     # new_setup[move[0]][move[1]] = 'XXX'
    #     # print (new_setup[move[0]][move[1]])
    #     # print (setup[move[0]][move[1]])
    #     return queue
    
    num = selectable_number(new_setup,move[0],move[1])
    
    

    if matrixToLine(new_setup).count('0') > 33:
    
    # if new_setup == [['0', '0', '0', '0', '0', '0'], 
    #                 ['0', '0', '0', '0', '0', '0'],
    #                 ['0', '0', '0', '0', '0', '0'],
    #                 ['0', '0', '0', '0', '0', '0'],
    #                 ['0', '0', '0', '0', '0', '0'],
    #                 ['0', '0', '0', '0', '0', '0']]:
        print ("Done!!!")
        print ("queue: ", queue)
        print ("Moves done: ", moves_done)
        for i in range (6):
            print (new_setup[i])
        return True
    

    if num == 0: 
        memoDeadEnds[tuple(move)] = new_setup
        #move.extend(queue)
        #Need previous move
        if new_setup[move[0]][move[1]] == '0':
            # print ("move: ", move, " 0: ", move[0], " 1: ", move[1])
            # print (new_setup[move[0]][move[1]])
            # print (setup[move[0]][move[1]])
            new_setup[move[0]][move[1]] = setup[move[0]][move[1]]       #!!!Reading of global var
            # print (new_setup[move[0]][move[1]])
            # print (setup[move[0]][move[1]])   
            # new_setup[move[0]][move[1]] = 'XXX'
            # print (new_setup[move[0]][move[1]])
            # print (setup[move[0]][move[1]])
            del moves_done[-1]
            #return 0
            return tryMoveRecurs(new_setup, queue, moves_done)
        
            #queue.insert(0, move)
        else:
            #queue = tryMoveRecurs(new_setup,queue)
            #newMoves = selectable(new_setup,move[0],move[1])
            #newMoves.extend(queue)
            #queue = newMoves
            #queue.extend(newMoves)
            #updatedSetup = select(new_setup,move[0],move[1])
            
            return tryMoveRecurs(new_setup,queue,moves_done)
    else:
        newMoves = selectable(new_setup,move[0],move[1])
        queue.insert(0,move)
        newMoves.extend(queue)
        
        queue = newMoves
        #queue.insert(0,move)
        #queue.extend(newMoves)
        updatedSetup = select(new_setup,move[0],move[1])
        moves_done.append(move)
        
        return tryMoveRecurs(updatedSetup,queue,moves_done)


def tryMoveIterDFS(curr_setup, moves, moves_done):
    global iterNumber
    memoDeadEnds = {}
    new_setup = copy.deepcopy(curr_setup)
    queue = moves
    while len(queue) != 0:
        
        
        if iterNumber > 1E7:
            print ("too long")
            return False
        iterNumber += 1
        move = queue.pop(0)
        
        while tuple(move) in memoDeadEnds.keys():
            if memoDeadEnds[tuple(move)] == new_setup:
            #if memoDeadEnds[tuple(move)]:
                #del queue[-1]
                # if len(queue) == 0:
                #     return "Empty"
                # print ("Move: ", move)
                # print ("Setup: ", )
                # for i in range (6):
                #     print (new_setup[i])
                move = queue.pop(0)
                # print ("Move after: ", move)
            else:
                break
    
        t1 = move[0]
        t2 = move[1]

        tst = new_setup[t1][t2]
        
            
        num = selectable_number(new_setup,move[0],move[1])
        
        if num == 0:
            # if move == [1,4]:
            #     print
            if tuple(move) not in memoDeadEnds.keys():
                memoDeadEnds[tuple(move)] = new_setup
            
            #memoDeadEnds[tuple(move)] = True
            if new_setup[move[0]][move[1]] == '0':
                new_setup[move[0]][move[1]] = setup[move[0]][move[1]]       #!!!Reading of global var
                #if moves_done[-1] == [2,2]:
                    # print('remove [2,2]')
                del moves_done[-1]
                #go to the beginning
        else:
            newMoves = selectable(new_setup,move[0],move[1])
            queue.insert(0,move)
            newMoves.extend(queue)
            queue = newMoves
            
            new_setup = select(new_setup,move[0],move[1])
            moves_done.append(move)
            
            ##assert moves_done == [[0,0], [0,0]]
            # with open('output_Breadth_first_search.txt', 'a') as f:
            #     print ("Last move is: ", move, file=f)
            #     print("Moves line is: ", moves_done, file=f)
            #     print ("Possible moves are: ", newMoves, file=f)
            #     print ("Current queue is: ", queue, file=f)
            #     for i in range (6):
            #         print (new_setup[i], file=f)
        
        if matrixToLine(new_setup).count('0') > 34:
        # if new_setup == [['0', '0', '0', '0', '0', '0'], 
        #                 ['0', '0', '0', '0', '0', '0'],
        #                 ['0', '0', '0', '0', '0', '0'],
        #                 ['0', '0', '0', '0', '0', '0'],
        #                 ['0', '0', '0', '0', '0', '0'],
        #                 ['0', '0', '0', '0', '0', '0']]:
            print ("Done!!!")
            print ("queue: ", queue)
            print ("Moves done: ", moves_done)
            for i in range (6):
                print (new_setup[i])
            return True
        
    # print ("No more moves")
    # for i in range (6):
    #     print (new_setup[i])
    # print ("Queue: ", queue)
    # print ("Moves done: ", moves_done)
    return False
        
# for i in range (6):
#     for j in range (6):
#         try:     
#             print (i, j)
#             globCounter = 0
#             tst = tryMoveRecurs(setup, [[i,j]], [])
#             print (tst, globCounter, i, j)
#         except:
#             print ("error")
iterNumber = 0
i = 0
j = 0

# tst = tryMoveRecurs(setup, [[i,j]], [], {})
#tst = tryMoveIterDFS(setup, [[i,j]], [])

#TEST RECUR with all starts
# for i in range (6):
#     for j in range (6):
#         print (i, j)
#         globCounter = 0
#         try:
#             tst = tryMoveRecurs(setup, [[i,j]], [], {})
#         except:
#             #print("error")
#             tst = "error"
#         print (tst, globCounter, i, j)

#TEST ITER with 0 0
# i = 5
# j = 1
# print (i, j)
# globCounter = 0
# tst = tryMoveRecurs(setup, [[i,j]], [], {})
# print (tst, globCounter)   


#TEST ITER with all starts
iters = {}
for i in range (6):
    for j in range (6):
        print (i, j)
        iterNumber = 0
        tst = tryMoveIterDFS(setup, [[i,j]], [])
        if tst != False:
            print (tst, iterNumber)
        else:
            print ("Not found: ", tst, iterNumber)
        iters[(i,j)] = iterNumber
        print()
        
            
#TEST ITER with 0 0
# i = 0
# j = 2
# print (i, j)
# iterNumber = 0
# tst = tryMoveIterDFS(setup, [[i,j]], [])
# print (tst, iterNumber)            
            
            
            
# start = time.time()       
# for i in range (int(1E9)):
#     pass
# end = time.time()
# print("Empty sycle (1E9): ", end - start)
# print (i)
# i = 0
# j = 0
# start = time.time() 
# tst = tryMoveIterDFS(setup, [[i,j]], [])
# end = time.time()
# print("tryMoveIterDFS (1000001): ", end - start)
