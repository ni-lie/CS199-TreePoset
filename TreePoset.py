import sys
sys.path.append('Utils')

import TreePoset_Utils_v2 as util

def TreePoset(P):
    setPoset = P.copy()
    covered = []
    isCombined = False
    m = len(P)

    Y = []
    # get maximal poset 
    common_binary_rel = set(setPoset[0]).intersection(*setPoset[1:])
    # get Y or upsilon
    for binaryRel in setPoset:
        Y.append(''.join(util.get_linear_extensions(binaryRel)))

    # if L(P) == Y: return
    if set(util.get_linear_extensions(list(common_binary_rel))) == set(Y):
        return [list(common_binary_rel)]

    for i in range(m):
        for j in range(i+1, m):
            combined = util.combinePoset(P[i], P[j])
            # if P_i and P_j can be combined
            if combined != None and P[i] not in covered and P[j] not in covered:
                # check if L(i) U L(j) = L(combined)
                LE_Pi = util.get_linear_extensions(P[i])
                LE_Pj = util.get_linear_extensions(P[j])
                LE_combined = util.get_linear_extensions(combined)

                if set(LE_Pi).union(set(LE_Pj)) == set(LE_combined):
                    # append covered linear orders to covered
                    covered.append(P[i])
                    covered.append(P[j])
                    
                    # remove from setPoset P_i and P_j
                    setPoset.remove(P[i])
                    setPoset.remove(P[j])

                    # append to setPoset the combined poset
                    setPoset.append(combined)

                    combined = None     # reset
                    isCombined = True
    if isCombined == False:
        return setPoset
    # print(setPoset)
    setPoset = TreePoset(setPoset)
    return setPoset

# gets binary relation for each linear order
def binaryRelation(input):
    P = []
    for linear_order in input:
        binaryRel = util.linear_order_to_binary_relation(linear_order)
        P.append(binaryRel)
    return P


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

