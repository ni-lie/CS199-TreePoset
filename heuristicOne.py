"""
----------- TO RUN -----------------
python TreePoset.py <vertex count*> 

where <vertex count*> = {3, 4, 5, 6}

"""
import sys, os
sys.path.append('Utils')
from TreePoset_Utils_v2 import VERIFY, get_linear_extensions, rankInverse, group_linearOrders_by_its_root

args = sys.argv

if not os.path.exists("outputs/"):
    os.makedirs("outputs/")

def TreePoset(upsilon):
    Ptree = []
    
    while len(upsilon) > 0:
        m = len(upsilon)     
        n = len(upsilon[0])
        for h in range(m, 0, -1):
            minRank = [0 for i in range(n)]
            numCoverRelation = 0
            coverRelationP = []
            for i in range(1,n):
                for j in range(h):
                    v2 = rankInverse(i, upsilon[j])
                    if minRank[int(v2)-1] == 0:
                        v1 = rankInverse(i-1, upsilon[j])
                        coverRelationP.append((int(v1),int(v2)))
                        minRank[int(v2)-1] = i
                        minRank[int(v1)-1] = i-1
                        numCoverRelation +=1
                if numCoverRelation == n-1:
                    break
            P = get_linear_extensions(coverRelationP)
            if VERIFY(P, upsilon[:h]):
                Ptree.append(coverRelationP)
                upsilon = upsilon[h:]
                break
    
    return Ptree

#with open(f'inputs/{args[1]}.txt', 'r') as input_file, open(f'outputs/output_{args[1]}.txt', 'w') as output_file:
with open(f'optsol/inputs/{args[1]}treesinput.txt', 'r') as input_file, open(f'outputs/output_{args[1]}.txt', 'w') as output_file:
    for line in input_file:
        inputLinearOrders = [int(x) for x in line.strip('[]\n').split(',')]
        inputLinearOrders.sort()
        inputLinearOrders = [str(item) for item in inputLinearOrders]
        
        posets = []
        # group linear orders according to their root
        groupings = group_linearOrders_by_its_root(inputLinearOrders)

        # for each group, there is a set of posets
        # append each poset to the list posets
        for group in groupings:
            poset_group = TreePoset(group)
            for poset in poset_group:
                posets.append(poset)

        if posets != None:
            output_file.write(f"Input: {[int(x) for x in inputLinearOrders]}\n")
            for i in range(len(posets)):
                output_file.write(f"P{str(i+1)}: {posets[i]}\n")
            output_file.write("\n")
        else:
            output_file.write(f"Input: {[int(x) for x in inputLinearOrders]}\n")
            output_file.write("None!!!!!\n\n")

if posets != None:
    print(f"Generated all output of input linear order sets with {args[1]} vertices")
    print("Check 'output' directory")
else:
    print("Generated nothing")




