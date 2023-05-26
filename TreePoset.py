"""
----------- TO RUN -----------------
python TreePoset.py <vertex count*> 

where <vertex count*> = {3, 4, 5, 6}

"""
import sys, os
sys.path.append('Utils')
from TreePoset_Utils_v2 import binaryRelation, combinePosetv2, get_linear_extensions, gen_tree_poset, getDifference, intersection_difference, isTreePoset, binaryToCover

args = sys.argv

if not os.path.exists("outputs/"):
    os.makedirs("outputs/")

def TreePoset(Pstar, inputlinearorders):
    output_posets = []

    #base case: return intersection if |Pstar| == 1

    not_covered = []
    not_covered_linear = []
    while len(Pstar) >= 1:
        if len(Pstar) == 1:
            output_posets.append(Pstar[0])
            Pstar = not_covered.copy()
            inputlinearorders = not_covered_linear.copy()
            not_covered = []
            not_covered_linear = []
            continue
        #1. getting intersection and difference of all posets
        I_D = intersection_difference(Pstar)
        intersection = I_D[0]
        difference = I_D[1]
        #2. check if number of binary relations >= n - 1   
        n = len(inputlinearorders[0])
        if len(binaryToCover(intersection)) < n - 1 or (not isTreePoset(binaryToCover(intersection))):
            not_covered += [Pstar.pop(-1)] #remove the poset at the end of Pstar and go back to step 1
            not_covered_linear += [inputlinearorders.pop(-1)]
        #3. If condition above was satisfied, proceed to eliminating binary relations. [COMBINING POSETS]
        else:
            go_back_to_step_2 = False
            while len(difference) > 0:
                (a,b) = difference[0]
                if (b,a) in difference:
                    difference.remove((a,b))
                    difference.remove((b,a))
                else:
                    go_back_to_step_2 = True
                    break
            if go_back_to_step_2:
                not_covered += [Pstar.pop(-1)] 
                not_covered_linear += [inputlinearorders.pop(-1)]
            else:
                #VERIFY if intersection of posets is a tree poset
                cover_relations_intersection = binaryToCover(intersection)
                if len(cover_relations_intersection) == n - 1:
                    if isTreePoset(cover_relations_intersection) and sorted(get_linear_extensions(cover_relations_intersection)) == sorted(getDifference(inputlinearorders, not_covered_linear)):
                        #4. add intersection to output_posets
                        output_posets.append(intersection)
                        inputlinearorders = not_covered_linear
                        #go back to step 1
                        Pstar = not_covered.copy()
                        inputlinearorders = not_covered_linear.copy()
                        not_covered = []
                        not_covered_linear = []
                    else:
                        not_covered += [Pstar.pop(-1)] 
                        not_covered_linear += [inputlinearorders.pop(-1)]
                else:
                    not_covered += [Pstar.pop(-1)] 
                    not_covered_linear += inputlinearorders[-1]
    return output_posets

#with open(f'inputs/{args[1]}.txt', 'r') as input_file, open(f'outputs/output_{args[1]}.txt', 'w') as output_file:
with open(f'optsol/inputs/{args[1]}treesinput.txt', 'r') as input_file, open(f'outputs/output_{args[1]}.txt', 'w') as output_file:
    for line in input_file:
        inputLinearOrders = [int(x) for x in line.strip('[]\n').split(',')]
        inputLinearOrders.sort()
        inputLinearOrders = [str(item) for item in inputLinearOrders]

        Pstar = binaryRelation(inputLinearOrders)
        posets = TreePoset(Pstar, inputLinearOrders)

        if posets != None:
            output_file.write(f"Input: {[int(x) for x in inputLinearOrders]}\n")
            for i in range(len(posets)):
                output_file.write(f"P{str(i+1)}: {posets[i]}\n")
            output_file.write("\n")
        else:
            output_file.write(f"Input: {[int(x) for x in inputLinearOrders]}\n")
            output_file.write("None!!!!!\n\n")

if posets != None:
    print(f"Generated all output of input linear order sets with {args[1]} vertices")
    print("Check 'output' directory")
else:
    print("Generated nothing")


# # input_linear_order = [1234, 1243, 1324, 1342, 1423, 1432]
# input_linear_order = [1234, 1243, 1324, 1342, 1423]

# # # 
# # # input_linear_order = [1234, 1324, 1423, 1432]       # returns a hammock poset (P1)
# # # input_linear_order = [1243, 1423, 1432, 4123, 4132] # haven't considered inputs with different roots
# # # input_linear_order = ['12345', '12354', '12435', '13245', '13254', '13524', '14253', '14523', '14532', '15342', '15423', '15432']     # outputs 4 posets (optimal solution: 2 posets only)

# # # current test case
# # # input_linear_order = ['12345', '12354', '12435', '13245', '13254', '13524', '14253', '14523', '14532', '15342', '15423', '15432']
# # # input_linear_order = ['12345', '12354', '12435', '13245', '13254', '13524']


# input_linear_order = [str(item) for item in input_linear_order]
# input_linear_order.sort()
# Pstar = binaryRelation(input_linear_order)

# # run TreePoset
# result = TreePoset(Pstar)

# for i in range(len(result)):
#     print(f"P{str(i+1)}: {result[i]}")

