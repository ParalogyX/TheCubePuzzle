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

def tryMove(curr_setup, moves):
    new_setup = copy.deepcopy(curr_setup)
    cue = moves
    move = cue.pop(0)

    t1 = move[0]
    t2 = move[1]

    tst = new_setup[t1][t2]

    if new_setup[move[0]][move[1]] == '0':
        new_setup[move[0]][move[1]] = setup[move[0]][move[1]]       #!!!Reading of global var
        return cue
    
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
        return tryMove(new_setup,cue)
    else:
        newMoves = selectable(new_setup,move[0],move[1])
        newMoves.extend(cue)
        cue = newMoves
        #cue.extend(newMoves)
        updatedSetup = select(new_setup,move[0],move[1])
        
        return tryMove(updatedSetup,cue)

        
        

tst = tryMove(setup, [[1,1]])