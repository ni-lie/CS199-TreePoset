import linearChainsv2 as lc

def subgroup(inputLinearOrders):
    group = []
    covered = []
    uncovered = []
    for linearOrder in inputLinearOrders:
        for i in range(1, len(linearOrder)):
            v = lc.rankInverse(i, linearOrder)
            generatedLinearExtensions = lc.get_LinearChains(linearOrder)

            for subgroup in generatedLinearExtensions:
                # check if subgroup is a subset of inputLinearOrders
                if set(subgroup).issubset(set(inputLinearOrders)):
                    group.append(subgroup)
                    # append each element in subgroup to coveredLinearOrders
                    for x in subgroup:
                        covered.append(x)

    # checks all unconvered elements and append it to group
    for x in inputLinearOrders:
        if x not in covered:
            group.append(x)



def TreePoset(inputLinearOrders):
    # 1. determine the subgroups
    inputWithSubgroups = subgroup[inputLinearOrders]


    # 2. perform OneTreePoset for each subgroups       

    # m = len(inputLinearOrders)
    # n = len(inputLinearOrders[0])

    # minRank = [0 for i in range(n)]
    # numCoverRelation = 0
    # coverRelationP = []

    # 3. collect TreePosets in a list

    # 4. return/print the list of TreePosets

    



inputLinearOrders = [1234, 1243, 1432]
inputLinearOrders = [str(item) for item in inputLinearOrder]
TreePoset(inputLinearOrders)