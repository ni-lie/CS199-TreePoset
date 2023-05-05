import sys
sys.path.append('Utils')

import TreePoset_Utils_v2 as util


def TreePoset(input):
    Initialize_Poset = []

    for linear_order in input:
        Initialize_Poset.append(util.linear_order_to_binary_relation(linear_order))
        
    


input_linear_order = [1234, 1243, 1324, 1342, 1423, 1432]
input_linear_order = [str(item) for item in input_linear_order]
input_linear_order.sort()
TreePoset(input_linear_order)
