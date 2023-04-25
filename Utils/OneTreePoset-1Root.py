def OneTreePoset(inputLinearOrder):
    # sample input: [1234, 1243, 1423]
    # m = number of linear orders; n = length of Vertex set
    inputLinearOrder = [str(item) for item in inputLinearOrder]
    m = len(inputLinearOrder)     
    n = len(inputLinearOrder[0])

    minRank = [0 for i in range(n)]
    numCoverRelation = 0
    coverRelationP = []

    for i in range(1,n):
        for j in range(m):
            v2 = rankInverse(i, inputLinearOrder[j])
            if minRank[int(v2)-1] == 0:
                v1 = rankInverse(i-1, inputLinearOrder[j])
                coverRelationP.append((int(v1),int(v2)))
                minRank[int(v2)-1] = i
                minRank[int(v1)-1] = i-1
                numCoverRelation+=1
                
        if numCoverRelation == n-1:
            break

    return coverRelationP
    # # sample input: Y
    # upsilon = [1234, 1243, 1423]

    # # sample :L(P*) (will come from AllTopologicalSort.py)
    # LP = [1234, 1243, 1423]

    # # if true, then it means L(P*) = Y
    # if VERIFY(LP,upsilon):
    #     return coverRelationP

def rankInverse(index, linearOrder):
    # sample input: index = 3; linearOrder = 1234
    return linearOrder[index]

# checks whether L(P)* = Y (upsilon)
def VERIFY(LP, upsilon):
    if LP.sort() == upsilon.sort():
        return True
    return False
            

inputLinearOrders = [1234, 1243, 1423]

P = OneTreePoset(inputLinearOrders)
print("P0:", P)
# for i in range(len(P)):
#     print('P'+str(i+1)+':', P[i])
