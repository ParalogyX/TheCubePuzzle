# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 14:01:53 2020

@author: Vladimir
"""

from theCubeGame2check import *


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

def tryMoveRecurs(curr_setup, moves, moves_done):
    global globCounter
    globCounter += 1
    if len(moves) == 0:
        return "Empty"
    new_setup = copy.deepcopy(curr_setup)
    queue = moves
    move = queue.pop(0)

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
    
    if new_setup == [['0', '0', '0', '0', '0', '0'], 
                    ['0', '0', '0', '0', '0', '0'],
                    ['0', '0', '0', '0', '0', '0'],
                    ['0', '0', '0', '0', '0', '0'],
                    ['0', '0', '0', '0', '0', '0'],
                    ['0', '0', '0', '0', '0', '0']]:
        print ("Done!!!")
        print (queue)
        return True
    
    if num == 0:
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
    new_setup = copy.deepcopy(curr_setup)
    queue = moves
    while len(queue) != 0:
        
        if iterNumber > 1E6:
            return False
        iterNumber += 1
        move = queue.pop(0)
    
        t1 = move[0]
        t2 = move[1]

        tst = new_setup[t1][t2]
        
            
        num = selectable_number(new_setup,move[0],move[1])
        
        if num == 0:
            if new_setup[move[0]][move[1]] == '0':
                new_setup[move[0]][move[1]] = setup[move[0]][move[1]]       #!!!Reading of global var
                del moves_done[-1]
                #go to the beginning
        else:
            newMoves = selectable(new_setup,move[0],move[1])
            queue.insert(0,move)
            newMoves.extend(queue)
            queue = newMoves
            
            new_setup = select(new_setup,move[0],move[1])
            moves_done.append(move)
            # with open('output_Breadth_first_search.txt', 'a') as f:
            #     print ("Last move is: ", move, file=f)
            #     print("Moves line is: ", moves_done, file=f)
            #     print ("Possible moves are: ", newMoves, file=f)
            #     print ("Current queue is: ", queue, file=f)
            #     for i in range (6):
            #         print (new_setup[i], file=f)
        
        
        if new_setup == [['0', '0', '0', '0', '0', '0'], 
                        ['0', '0', '0', '0', '0', '0'],
                        ['0', '0', '0', '0', '0', '0'],
                        ['0', '0', '0', '0', '0', '0'],
                        ['0', '0', '0', '0', '0', '0'],
                        ['0', '0', '0', '0', '0', '0']]:
            print ("Done!!!")
            print ("queue: ", queue)
            print ("Moves done: ", moves_done)
            return True
        
    print ("No more moves")
    for i in range (6):
        print (new_setup[i])
    print ("Queue: ", queue)
    print ("Moves done: ", moves_done)
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
for i in range (6):
    for j in range (6):
        iterNumber = 0
        tst = tryMoveIterDFS(setup, [[i,j]], [])
        print (iterNumber)
        