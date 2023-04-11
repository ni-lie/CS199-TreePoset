import copy #https://stackoverflow.com/questions/37895718/appending-to-a-list-in-recursive-function?rq=1#:~:text=2-,import%20copy,-arr%20%3D%20%5B1

setofPosets = []
def OneTreePoset(inputLinearOrder):
    # sample input: [1234, 1243, 1432]
    # m = number of linear orders; n = length of Vertex set

    inputLinearOrder = [str(item) for item in inputLinearOrder]
    m = len(inputLinearOrder)     
    n = len(inputLinearOrder[0])

    minRank = [0 for i in range(n)]
    numCoverRelation = 0
    coverRelationP = []
    uncoveredLinearOrders = []

    for i in range(1,n):
        for j in range(m):
            v2 = int(rankInverse(i, inputLinearOrder[j]))
            v1 = int(rankInverse(i-1, inputLinearOrder[j]))
            if minRank[v2-1] == 0:
                if(v2, v1) not in coverRelationP:
                    coverRelationP.append((v1,v2))
                    minRank[v2-1] = i
                    minRank[v1-1] = i-1
                    numCoverRelation+=1
            # accounts for uncovered linear orders:
            elif (v2,v1) in coverRelationP:
                uncoveredLinearOrders.append(inputLinearOrder[j])

        # if numCoverRelation == n-1:
        #     break

    setofPosets.append(copy.deepcopy(coverRelationP))

    if len(uncoveredLinearOrders) != 0:
        OneTreePoset(uncoveredLinearOrders)
        

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
            

# inputLinearOrders = [1234, 1243, 1432] # correct
# inputLinearOrders = [1234, 1243, 1423] # correct
# inputLinearOrders = [1234, 1243, 1432, 1423] # correct
inputLinearOrders = [1234, 1243, 1342, 1423, 1432]  
# inputLinearOrders = [1234, 1243, 1432, 1423, 1342, 1324] # correct

OneTreePoset(sorted(inputLinearOrders))

for i in range(len(setofPosets)):
    print('P'+str(i+1)+':', setofPosets[i])
