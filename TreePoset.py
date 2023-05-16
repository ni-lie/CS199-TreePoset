import sys
sys.path.append('Utils')
from TreePoset_Utils_v2 import linear_order_to_binary_relation 

# import TreePoset_Utils_v2 as util

def TreePoset(P):



# CORRECT TEST CASES
input_linear_order = [1234, 1243, 1324, 1342, 1423, 1432]
input_linear_order = [1234, 1243, 1324, 1342, 1423]


# WRONG TEST CASES
# input_linear_order = [1234, 1324, 1423, 1432]       # returns a hammock poset (P1)
# input_linear_order = [1243, 1423, 1432, 4123, 4132] # haven't considered inputs with different roots
# input_linear_order = ['12345', '12354', '12435', '13245', '13254', '13524', '14253', '14523', '14532', '15342', '15423', '15432']     # outputs 4 posets (optimal solution: 2 posets only)

# current test case
input_linear_order = ['12345', '12354', '12435', '13245', '13254', '13524', '14253', '14523', '14532', '15342', '15423', '15432']

input_linear_order = [str(item) for item in input_linear_order]
input_linear_order.sort()

poset = binaryRelation(input_linear_order)

# run TreePoset
result = TreePoset(poset)

for i in range(len(result)):
    print(f"P{str(i+1)}: {result[i]}")

