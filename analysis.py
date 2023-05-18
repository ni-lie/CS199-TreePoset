"""
----------- TO RUN -----------------
python TreePoset.py <vertex count*> 

where <vertex count*> = {3, 4, 5, 6}

"""

import sys, os
from ast import literal_eval
sys.path.append('Utils')
from Analysis_Utils import isTreePoset, areTreePosets, isAllConnected

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

    #write to a new file <vertex>analysis.py on directory /analysis
    #write analysis per input in this format:
    #Input: [123, 132]
    #Optimal Solution: [[(1, 2), (1, 3)]]
    #Heuristic Solution: [[(1, 2), (1, 3)]]
    #Analysis: CORRECT - OPTIMAL
    # ... UNTIL EOF
    #SUMMARY
    #Total Number of Inputs:
    #Total Number of Correct Heuristic Solutions:
    #Total Number of Optimal Heuristic Solutions:

    if not os.path.exists("analysis/"):
        os.makedirs("analysis/")
    
    output = open(f"analysis/{args[1]}analysis.txt", "w")

    #for summary
    len_inputs = len(inputs)
    correct = 0
    optimal = 0
    for (input, cost, O_sol, H_sol) in zip(inputs, optcost, optsol, heuristicsol):
        n = len(str(input[0])) #number of vertices
        output.write("Input: "+ str(input)+"\n")
        output.write("Optimal Solution: "+ str(O_sol)+"\n")
        output.write("Heuristic Solution: "+ str(H_sol)+"\n")
        if areTreePosets(H_sol) and isAllConnected(H_sol, n) and len(H_sol) == cost:
            output.write("Analysis: CORRECT - OPTIMAL\n")
            correct += 1
            optimal += 1
        elif areTreePosets(H_sol) and isAllConnected(H_sol, n) and len(H_sol) != cost:
            output.write("Analysis: CORRECT - NOT OPTIMAL\n")
            correct += 1
        else:
            output.write("Analysis: INCORRECT - NOT OPTIMAL\n")
        output.write("\n")

    output.write("Summary\n")
    output.write("Total Number of Inputs: "+str(len_inputs)+"\n")
    output.write("Total Number of Correct Heuristic Solutions: "+str(correct)+"\n")
    output.write("Total Number of Correct Optimal Solutions: "+str(optimal)+"\n")
    output.close

    print("FINISHED ANALYSING HEURISTIC")