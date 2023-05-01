"""
# source: songsong and angeles
# generate input linear orders
----------- TO RUN -----------------
python linearorders.py <vertex count*> 

where <vertex count*> = {3, 4, 5, 6}

"""


import os, sys
sys.path.append('Utils')
from Input_Utils import generateRootedRelations, isAllConnected
from classes import Poset

if not os.path.exists("inputs/"):
    os.makedirs("inputs/")

args = sys.argv
args[1] = int(args[1])
n = args[1] # the length of a linear order. Ex: linearOrder = 1234, n = 4

vertices = [v for v in range(1, n+1)]
rels = []

for root in vertices:
    newVertices = [v for v in vertices if v!=root]

    rootedRels = generateRootedRelations(root, newVertices, [])
    
    for rel in rootedRels:
        if isAllConnected(vertices, rel) and rel not in rels:
            rels.append(rel)


lst = [Poset(args[1], relations).generateLinearExtensions() for relations in rels]
output = open(f"inputs/{args[1]}.txt", "w")
for setOfLinOrder in lst:
    output.write(str([int(''.join(map(str, linOrder))) for linOrder in setOfLinOrder]) + "\n")

output.close()

print(f"Generated all tree linear order sets with {args[1]} vertices")