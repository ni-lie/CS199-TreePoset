import sys
sys.path.append('Utils')

import OneTreePoset as otp
import TreePoset_Utils as tpu

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
# inputLinearOrders = [1234, 1243, 1423, 1432] 
# inputLinearOrders = [1234] 
# inputLinearOrders = [1234, 1243, 1342, 1423, 1432]  
# inputLinearOrders = [1234, 1243, 1423, 4123, 4132]
# inputLinearOrders = [123456, 123465]
# inputLinearOrders = [123456, 123465, 132465, 134265, 134256]

# CORRECT BUT NOT OPTIMAL
inputLinearOrders = [1234, 1243, 1432, 1423, 1342, 1324] # only one tree poset covers this but outputs two posets since findSubgroup outputs two subgroups; can be combined??


inputLinearOrders.sort()
inputLinearOrders = [str(item) for item in inputLinearOrders]
TreePoset(inputLinearOrders)