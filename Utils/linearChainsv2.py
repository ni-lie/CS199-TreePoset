# This function returns the element v in V such that rank(v, l) = r.
def rankInverse(index, linearOrder):
    # sample input: index = 3; linearOrder = 1234; 
    return linearOrder[index]       # output: 4

# This function gives the position of the element v in the linear extension l
def rank(v, linearOrder):
    return linearOrder.index(v)

def get_chains(v, l):
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


# inputLinearOrders = [1234, 1243, 1342, 1423, 1432] 
inputLinearOrders = [1234]
inputLinearOrders = [str(item) for item in inputLinearOrders] # converts list of int to list of str

for linearOrder in inputLinearOrders:
    for i in range(1, len(linearOrder)):
        v = rankInverse(i, linearOrder)
        get_chains(v, linearOrder)

