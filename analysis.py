"""
----------- TO RUN -----------------
python TreePoset.py <vertex count*> 

where <vertex count*> = {3, 4, 5, 6}

"""

import sys, os
from ast import literal_eval

args = sys.argv

#
with open(f'optsol/trees/{args[1]}treesoptsol.txt', 'r') as optimal_file, open(f'outputs/output_{args[1]}.txt', 'r') as HeuristicOutput_file:
    #Optimal Solution Data
    inputs = []
    optcost = []
    optsol = []
    insert_optsols = 0
    for line in optimal_file:
        if line[:7] == "Input: ":
            inputs.append(literal_eval(line[7:-1]))
        elif line[:23] == "Optimal solution cost: ":
            optcost.append(int(line[23:]))
            insert_optsols = int(line[23:])
        elif line == "\n":
            continue
        else:
            if insert_optsols == optcost[-1] and line[0] == '[': #first poset is added to the list of optimal solutions
                lst = literal_eval(line)
                optsol.append([])
                optsol[-1].append(lst)
                insert_optsols -= 1     #decrement until 0 (all posets are added)
            else:
                #print(insert_optsols)
                lst = literal_eval(line)
                optsol[-1].append(lst) #n + 1 posets are added to the latest group of posets added
                insert_optsols -= 1

    #Heuristic data
    heuristicsol = []
    for line in HeuristicOutput_file:
        if line[:7] == "Input: ":
            continue
        elif line[:2] == "P1":
            #first poset is added to the list of heuristic solutions
            start = line.index('[')
            lst = literal_eval(line[start:])
            heuristicsol.append([])
            heuristicsol[-1].append(lst)
        elif line == "\n":
            continue    
        else:
            start = line.index('[')
            lst = literal_eval(line[start:])
            heuristicsol[-1].append(lst)