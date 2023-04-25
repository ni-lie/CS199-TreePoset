import math

# This function returns the element v in V such that rank(v, l) = r.
def rankInverse(index, linearOrder):
    # sample input: index = 3; linearOrder = 1234; 
    return linearOrder[index]       # output: 4

# This function gives the position of the element v in the linear extension l
def rank(v, linearOrder):
    return linearOrder.index(v)

# Lemma 5
def get_LinearChains(v, l):
    generatedLinearExtensions = []
    # Let A0 = {v}, A1 = ancestor(v, P), A2 = descendant(v, P), A3 = incomparable(v, P)
    A1 = [x for x in l if x!=v and rank(x,l) < rank(v,l)]

    # for elements that have rank > rank(v): the element can either be a (1) descendant or (2) incomparable:
    n = len(l)
        # A2 = descendant
        # A3 = not in A1 and A2
    C1 = ''.join(A1)
    for d in range(rank(v,l)+1, n):
        A2 = [rankInverse(x,l) for x in range(d,n)]
        A3 = [x for x in l if (x!=v) and (x not in A1) and (x not in A2)]

        C2 = ''.join(A2)
        C3 = ''.join(A3)
        l1 = C1 + v + C2 + C3
        l2 = C1 + v + C3 + C2
        l3 = C1 + C3 + v + C2

        # check if l1, l2, and l3 are distinct
        if (l1 != l2) and (l1 != l3) and (l2 != l3):
            generatedLinearExtensions.append([l1,l2,l3])
            # print('l1: '+ l1 + ' ' + 'l2: '+ l2 +' ' + 'l3: '+ l3 +'\n')
        
        # A2 = not in A1 and A3
        # A3 = incomparable
    for d in range(rank(v,l)+1, n):
        A3 = [rankInverse(x,l) for x in range(d,n)]
        A2 = [x for x in l if (x!=v) and (x not in A1) and (x not in A3)]
    
        C2 = ''.join(A2)
        C3 = ''.join(A3)
        l1 = C1 + v + C2 + C3
        l2 = C1 + v + C3 + C2
        l3 = C1 + C3 + v + C2

        # check if l1, l2, and l3 are distinct
        if (l1 != l2) and (l1 != l3) and (l2 != l3):
            generatedLinearExtensions.append([l1,l2,l3])
            # print('l1: '+ l1 + ' ' + 'l2: '+ l2 +' ' + 'l3: '+ l3 +'\n')
    
    return generatedLinearExtensions

# this functions return a list cointaining distinct root/first element of a linear order
def findProbableMinimumPosets(inputLinearOrders):
    set_distinct = set()
    for linearOrder in inputLinearOrders:
        set_distinct.add(linearOrder[0])

    return list(set_distinct)


def findSubgroup(inputLinearOrders):
    group = []
    covered = []

    # find list containing distinct root
    distinctRoots = findProbableMinimumPosets(inputLinearOrders)

    #--------------------------- (VERIFY THIS with ma'am ivy) ---------------------------
    # m = number of linear orders; n = length of a linear order
    # if (n-1)! == m, the inputLinearOrder can be covered by a single tree poset; see leveled poset definition    
    m = len(inputLinearOrders)
    n = len(inputLinearOrders[0])
    for i in range(len(distinctRoots)):
        if(m >= math.factorial(n-1)):
            for linearOrder in inputLinearOrders:
                if distinctRoots[i] == linearOrder[0] and linearOrder not in covered:
                    if len(group) < i+1 and linearOrder:
                        group.append([linearOrder])
                    else: # elif len(group) <= i
                        group[i].append(linearOrder)
                    covered.append(linearOrder)

    # if(math.factorial(n-1) == m):
    #     group.append(inputLinearOrders)
    #     return group
    # -------------------------------------------------------------------

    for linearOrder in inputLinearOrders:
        for i in range(1, len(linearOrder)):
            v = rankInverse(i, linearOrder)
            generatedLinearExtensions = get_LinearChains(v, linearOrder)

            for subgroup in generatedLinearExtensions:
                shouldAppend = True
                # check if subgroup is a subset of inputLinearOrders
                if set(subgroup).issubset(set(inputLinearOrders)):
                    # if at least one element in subgroup is already covered, do not append it to group
                    for ele in subgroup:
                        if ele in covered:
                            shouldAppend = False
                            break
                    if shouldAppend:
                        group.append(subgroup)
                    # append each element in subgroup to coveredLinearOrders
                        for x in subgroup:
                            covered.append(x)
    
    # checks pairs of uncovered elements -- check if the pair differs by one adjacent transpo graph AT THE TAIL
    # if this is true: put the pair in a single list
    for x in inputLinearOrders:
        for y in inputLinearOrders:
            if x not in covered and y not in covered and x!=y:
                if x == y[:-2] + y[-1] + y[-2]:
                    group.append([x,y])
                    covered.append(x)
                    covered.append(y)
            
    # checks all unconvered elements and append it to group
    for x in inputLinearOrders:
        if x not in covered:
            group.append([x])

    return group

# inputLinearOrders = [1234, 1243, 1342, 1423, 1432] 
# inputLinearOrders = [1234]
# inputLinearOrders = [1234, 1243, 1432, 1423, 1342, 1324]
# inputLinearOrders.sort()
# inputLinearOrders = [str(item) for item in inputLinearOrders] # converts list of int to list of str

# for linearOrder in inputLinearOrders:
#     for i in range(1, len(linearOrder)):
#         v = rankInverse(i, linearOrder)
#         l_ext = get_LinearChains(v, linearOrder)
#         for item in l_ext:
#             print(sorted(item))
