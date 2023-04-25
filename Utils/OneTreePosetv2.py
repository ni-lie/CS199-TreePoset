import linearChainsv2 as lc

def OneTreePoset(linearOrder):
    # m = number of linear orders; n = length of Vertex set
    m = len(linearOrder)     
    n = len(linearOrder[0])
    minRank = [0 for i in range(n)]
    numCoverRelation = 0
    coverRelationP = []

    for i in range(1,n):
        for j in range(m):
            v2 = lc.rankInverse(i, linearOrder[j])
            if minRank[int(v2)-1] == 0:
                v1 = lc.rankInverse(i-1, linearOrder[j])
                coverRelationP.append((int(v1),int(v2)))
                minRank[int(v2)-1] = i
                minRank[int(v1)-1] = i-1
                numCoverRelation +=1
        if numCoverRelation == n-1:
            break

    return coverRelationP



# inputLinearOrders = ['1243', '1234', '1324']
# inputLinearOrders.sort()
# P = OneTreePoset(inputLinearOrders)
# print("P0:", P)