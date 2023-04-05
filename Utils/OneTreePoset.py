def OneTreePoset(input):
    # sample input: [[1234, 1243, 1432], [2142, 2314], [3214], [4321]]
    setOfPosets = []
    for subgroup in input:
        # m = number of linear orders; n = length of Vertex set
        subgroup = [str(item) for item in subgroup]
        m = len(subgroup)     
        n = len(subgroup[0])

        minRank = [0 for i in range(n)]
        numCoverRelation = 0
        coverRelationP = []

        for i in range(1,n):
            for j in range(m):
                v2 = rankInverse(i, subgroup[j])
                if minRank[int(v2)-1] == 0:
                    v1 = rankInverse(i-1, subgroup[j])
                    coverRelationP.append((int(v1),int(v2)))
                    minRank[int(v2)-1] = i
                    minRank[int(v1)-1] = i-1
                    numCoverRelation+=1
            if numCoverRelation == n-1:
                break

        setOfPosets.append(coverRelationP)

    return setOfPosets
        
        # if VERIFY(P,Y):
        #     return P
        # else
        #     return null

def rankInverse(index, linearOrder):
    # sample input: index = 3; linearOrder = 1234
    return linearOrder[index]

inputLinearOrders = [[1234, 1243, 1432], [2142, 2314], [3214], [4321]]
print(OneTreePoset(inputLinearOrders))
