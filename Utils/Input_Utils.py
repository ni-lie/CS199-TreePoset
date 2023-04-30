# source: angeles and songsong
def generateRootedRelations(parent, vertices, relations):
    if len(vertices) == 0:
        return [sorted(relations)]
    else:
        rels = []
        for child in vertices:
            newVertices = [v for v in vertices if v!=child]
            rels.extend(generateRootedRelations(parent, newVertices, relations + [(parent, child)]))
            rels.extend(generateRootedRelations(parent, newVertices, relations + [(child, parent)]))
            rels.extend(generateRootedRelations(child, newVertices, relations + [(parent, child)]))
            rels.extend(generateRootedRelations(child, newVertices, relations + [(child, parent)]))

        truerels = []
        for rel in rels:
            if rel not in truerels: truerels.append(rel)

        return truerels
    
def isAllConnected(vertices, relations):
    for vertex in vertices:
        isConnected = False
        for relation in relations:
            if vertex in relation:
                isConnected = True
                break
        
        if not isConnected: return False
    
    return True