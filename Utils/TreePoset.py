import linearChainsv2 as lc
import OneTreePoset as otp

def subgroup(inputLinearOrders):
    group = []
    covered = []
    for linearOrder in inputLinearOrders:
        for i in range(1, len(linearOrder)):
            v = lc.rankInverse(i, linearOrder)
            generatedLinearExtensions = lc.get_LinearChains(v, linearOrder)

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
                    

    # checks all unconvered elements and append it to group
    for x in inputLinearOrders:
        if x not in covered:
            group.append(x)

    return group



def TreePoset(inputLinearOrders):
    # 1. determine the subgroups
    inputWithSubgroups = subgroup(inputLinearOrders)

    # print(inputWithSubgroups)

    # 2. perform OneTreePoset for each subgroups (if inputWithSubgroups contain only subgroups, can they be covered by a single tree poset? hmmm)   


    # m = len(inputLinearOrders)
    # n = len(inputLinearOrders[0])

    # minRank = [0 for i in range(n)]
    # numCoverRelation = 0
    # coverRelationP = []

    # 3. collect TreePosets in a list

    # 4. return/print the list of TreePosets


# inputLinearOrders = [1234, 1243, 1432] # correct
# inputLinearOrders = [1234, 1243, 1423] # correct
# inputLinearOrders = [1234, 1243, 1432, 1423] # correct
# inputLinearOrders = [1234, 1243, 1342, 1423, 1432]  # correct
inputLinearOrders = [1234, 1243, 1432, 1423, 1342, 1324] # correct
inputLinearOrders.sort()
inputLinearOrders = [str(item) for item in inputLinearOrders]
TreePoset(inputLinearOrders)