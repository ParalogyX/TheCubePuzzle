# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 14:01:53 2020

@author: Vladimir
"""

from theCubeGame2check import *

# setup = [['>', 'V', 'V', '<', '<', 'V'], 
#         ['>', '>', '>', 'V', 'V', 'V'],
#         ['>', 'V', 'V', '^', '<', '<'],
#         ['^', '>', '^', '<', '^', '<'],
#         ['^', '^', '<', '>', '<', '^'],
#         ['^', '>', '>', '^', '^', '<']]

setup = [['>', 'V', 'V', '<', '<', 'V'], 
        ['>', '^', '>', 'V', 'V', 'V'],
        ['>', '^', 'V', '^', '<', '<'],
        ['^', '^', '^', '<', '^', '<'],
        ['^', '^', '<', '>', '<', '^'],
        ['^', '^', '>', '^', '^', '<']]

def tryMove(curr_setup, moves, moves_done):
    if len(moves) == 0:
        return "Empty"
    new_setup = copy.deepcopy(curr_setup)
    cue = moves
    move = cue.pop(0)

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
    #     return cue
    
    num = selectable_number(new_setup,move[0],move[1])
    
    if new_setup == [['0', '0', '0', '0', '0', '0'], 
                    ['0', '0', '0', '0', '0', '0'],
                    ['0', '0', '0', '0', '0', '0'],
                    ['0', '0', '0', '0', '0', '0'],
                    ['0', '0', '0', '0', '0', '0'],
                    ['0', '0', '0', '0', '0', '0']]:
        print ("Done!!!")
        print (cue)
        return True
    
    if num == 0:
        #move.extend(cue)
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
            return tryMove(new_setup, cue, moves_done)
        
            #cue.insert(0, move)
        else:
            #cue = tryMove(new_setup,cue)
            #newMoves = selectable(new_setup,move[0],move[1])
            #newMoves.extend(cue)
            #cue = newMoves
            #cue.extend(newMoves)
            #updatedSetup = select(new_setup,move[0],move[1])
            
            return tryMove(new_setup,cue,moves_done)
    else:
        newMoves = selectable(new_setup,move[0],move[1])
        cue.insert(0,move)
        newMoves.extend(cue)
        
        cue = newMoves
        #cue.insert(0,move)
        #cue.extend(newMoves)
        updatedSetup = select(new_setup,move[0],move[1])
        moves_done.append(move)
        
        return tryMove(updatedSetup,cue,moves_done)

        
        

tst = tryMove(setup, [[0,0]], [])