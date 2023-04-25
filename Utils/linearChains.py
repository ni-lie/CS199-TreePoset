# Lemma 5

setofPosets = []

def group(inputLinearOrder):
    # sample input: [1234, 1243, 1423]
    # m = number of linear orders; n = length of Vertex set
    inputLinearOrder = [str(item) for item in inputLinearOrder]
    m = len(inputLinearOrder)     
    n = len(inputLinearOrder[0])

    # Let A0 = {v}, A1 = ancestor(v, P), A2 = descendant(v, P), A3 = incomparable(v, P)
    for linearOrder in inputLinearOrder:
        for i in range(1,n):
            v = linearOrder[i]
            c1 = linearOrder[:i] 
            for j in range(i+1, n):
                if(j!=n-1):
                    c2 = linearOrder[i+1:j+1]
                    c3 = linearOrder[j+1:]
                # elif j == n-1:
                else:
                    c2 = linearOrder[i+1:n]
                    c3 = ''
                #  l1 = (C1, v, C2, C3), l2 = (C1, v, C3, C2) and l3 = (C1, C3, v, C2).
                l1 = c1+v+c2+c3
                l2 = c1+v+c3+c2
                l3 = c1+c3+v+c2
                
                # check if l1,l2,l3 are distinct
                li = [l1,l2,l3]
                li.sort()
                if sorted(list(set(li))) == li: 
                    for item in li: 
                        print(item)
                    print('\n')
                
            c2 = ''
            c3 = linearOrder[i+1:n]
            l1 = c1+v+c2+c3
            l2 = c1+v+c3+c2
            l3 = c1+c3+v+c2

            li = [l1,l2,l3]
            li.sort()
            if sorted(list(set(li))) == li: 
                for item in li:
                    print(item)
                print('\n')


# inputLinearOrders = [1234, 1243, 1423] 
# inputLinearOrders = [1324, 1342, 1432] 

# -----------------------------------
inputLinearOrders = [1234, 1243, 1342, 1423, 1432] 
# G1: (1234, 1243, 1423) - should be covered by one tree poset
# uncovered = 1342, 1432
# -----------------------------------

# inputLinearOrders = [1234, 1243, 1432, 1423, 1342, 1324] 

group(sorted(inputLinearOrders))
