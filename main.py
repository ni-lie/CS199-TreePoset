"""
----------- TO RUN -----------------
python main.py <vertex count*> 

where <vertex count*> = {3, 4, 5, 6}

"""

import sys
sys.path.append('Utils')

import OneTreePoset as otp
import TreePoset_Utils as tpu
import ast, sys, os 

args = sys.argv

if not os.path.exists("outputs/"):
    os.makedirs("outputs/")


def TreePoset(inputLinearOrders):
    setOfPosets = []
    linear_extensions = []
    # 1. determine the subgroups
    inputWithSubgroups = tpu.findSubgroup(inputLinearOrders)
    # print(inputWithSubgroups)

    # 2. perform OneTreePoset for each subgroups then append the result to setOfPosets
    for item in inputWithSubgroups:
        poset = otp.OneTreePoset(item)
        setOfPosets.append(poset)

    # 3. VERIFY(P;Y) 
    for poset in setOfPosets:
        linear_extension = tpu.get_linear_extensions(poset)
        linear_extensions.extend(linear_extension)

    if tpu.VERIFY(linear_extensions, inputLinearOrders):
        return setOfPosets
    
    return None

    # 3. return/print the list of TreePosets
    # return setOfPosets

with open(f'inputs/{args[1]}.txt', 'r') as input_file, open(f'outputs/output_{args[1]}.txt', 'w') as output_file:
    for line in input_file:
        inputLinearOrders = [int(x) for x in line.strip('[]\n').split(',')]
        inputLinearOrders.sort()
        inputLinearOrders = [str(item) for item in inputLinearOrders]

        posets = TreePoset(inputLinearOrders)
        if posets != None:
            output_file.write(f"Input: {inputLinearOrders}\n")
            for i in range(len(posets)):
                output_file.write(f"P{str(i+1)}: {posets[i]}\n")
            output_file.write("\n")

if posets != None:
    print(f"Generated all output of input linear order sets with {args[1]} vertices")
    print("Check 'output' directory")
else:
    print("Generated nothing")

