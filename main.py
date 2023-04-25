import sys
sys.path.append('Utils')

import OneTreePoset as otp
import TreePoset_Utils as tpu
import AllTopologicalSort as ats
from AllTopologicalSort import Poset

setOfPosets = []

def TreePoset(inputLinearOrders):
    # 1. determine the subgroups
    inputWithSubgroups = tpu.findSubgroup(inputLinearOrders)
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
# inputLinearOrders = [1324, 1342, 1432, 1234] 
# inputLinearOrders = [1234, 1243, 1423, 1432] 
# inputLinearOrders = [1234] 
# inputLinearOrders = [1234, 1243, 1342, 1423, 1432]  
# inputLinearOrders = [1234, 1243, 1423, 4123, 4132]
# inputLinearOrders = [123456, 123465]
# inputLinearOrders = [123456, 123465, 132465, 134265, 134256]

# CORRECT BUT NOT OPTIMAL TEST CASES
# now correct and optimal! but need to verify the algo with ma'am ivy
# inputLinearOrders = [1234, 1243, 1432, 1423, 1342, 1324] # only one tree poset covers this but outputs two posets since findSubgroup outputs two subgroups; can be combined??
inputLinearOrders = [1234, 1243, 1432, 1423, 1342, 1324, 2134, 2143, 2314, 2341, 2413, 2431]

inputLinearOrders.sort()
inputLinearOrders = [str(item) for item in inputLinearOrders]
TreePoset(inputLinearOrders)

#Testing AllTopologicalSort
P1 = Poset((1,2,3,4), [(1,2), (1,3), (1,4)]) 
P2 = Poset((1,2,3,4), [(2,1), (2,3), (2,4)]) 
print("AllTopologicalOrders for P1: ")
ats.printAllTopologicalOrders(P1)
print("AllTopologicalOrders for P2: ")
ats.printAllTopologicalOrders(P2)