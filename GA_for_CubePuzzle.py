# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 15:20:20 2020

@author: vpe
"""

import numpy as np
from theCubeGame2check import *

from pymoo.algorithms.nsga2 import NSGA2
from pymoo.model.problem import Problem
from pymoo.optimize import minimize
from pymoo.visualization.scatter import Scatter
from pymoo.factory import get_algorithm, get_crossover, get_mutation, get_sampling


class MyProblem(Problem):

    
    

    def __init__(self):
        # super().__init__(n_var=38,
        #                   n_obj=1,
        #                   n_constr=0,
        #                   xl=np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
        #                   xu=np.array([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]),
        #                   elementwise_evaluation=True)
        super().__init__(n_var=38,
                         n_obj=1,
                         n_constr=0,
                         xl=0,
                         xu=5,
                         type_var = int,
                         elementwise_evaluation = True)

    def _evaluate(self, x, out, *args, **kwargs):
        
        setup = [['>', 'V', 'V', '<', '<', 'V'], 
             ['>', '>', '>', 'V', 'V', 'V'],
             ['>', 'V', 'V', '^', '<', '<'],
             ['^', '>', '^', '<', '^', '<'],
             ['^', '^', '<', '>', '<', '^'],
             ['^', '>', '>', '^', '^', '<']]
        
        moves = []
        for i in range (36):
            moves.append(int(x[i]))
        xs = int(x[36])
        ys = int(x[37])
        func_res = check_solution (setup, [xs, ys], moves)
        
        f1 = func_res
        
        #f1 = x[0] - x[1]
        #f1 = -f1

        
        #f1 = (x[0] + x[1])/x[1]
        #f2 = (x[0] - x[1])/x[1]
        
        #f1 = x[0] ** 2 + x[1] ** 2
        #f2 = (x[0] - 1) ** 2 + x[1] ** 2
        
        #g1 = f1 - 2 
        #g1 = 2 * (x[0] - 0.1) * (x[0] - 0.9) / 0.18
        #g2 = - 20 * (x[0] - 0.4) * (x[0] - 0.6) / 4.8

        #out["F"] = [f1, f2]
        out["F"] = [f1]
        out["G"] = []


problem = MyProblem()

algorithm = NSGA2(op_size=100,sampling = get_sampling("int_random"),crossover=get_crossover("int_sbx", prob=0.95, eta=30.0), mutation=get_mutation("int_pm", eta=6.0))
                  
#get_sampling("int_random")

                  
res = minimize(problem,
               algorithm,
               ("n_gen", 200),
               verbose=True,
               seed=1)
#print(res.F[2])
#res.F[2] = -res.F[2]

plot = Scatter()

plot.add(res.F, color="red")

plot.show()