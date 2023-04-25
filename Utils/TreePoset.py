import linearChainsv2 as lc
import OneTreePoset as otp

setOfPosets = []

def findSubgroup(inputLinearOrders):
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
            group.append([x])

    return group



def TreePoset(inputLinearOrders):
    # 1. determine the subgroups
    inputWithSubgroups = findSubgroup(inputLinearOrders)
    # print(inputWithSubgroups)

    # 2. perform OneTreePoset for each subgroups then append the result to setOfPosets
    for item in inputWithSubgroups:
        poset = otp.OneTreePoset(item)
        setOfPosets.append(poset)

    # 3. return/print the list of TreePosets
    for i in range(len(setOfPosets)):
        print('P'+str(i+1)+':', setOfPosets[i])

   

# CORRECT TEST CASES SO FAR
# inputLinearOrders = [1234, 1243, 1423] 
# inputLinearOrders = [1234, 1243, 1423, 1432] 
# inputLinearOrders = [1234] 
# inputLinearOrders = [1234, 1243, 1342, 1423, 1432]  

# WRONG TEST CASES SO FAR
inputLinearOrders = [1234, 1243, 1432, 1423, 1342, 1324] # only one tree poset covers this but outputs two posets since findSubgroup outputs two subgroups; can be combined??

inputLinearOrders.sort()
inputLinearOrders = [str(item) for item in inputLinearOrders]
TreePoset(inputLinearOrders)