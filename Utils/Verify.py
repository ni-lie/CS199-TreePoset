import AllTopologicalSort as ats
from AllTopologicalSort import Poset

def Verify(set_poset, upsilon):
    #This function returns True if L(set_Poset) == upsilon
    #where L(set_poset) == (ats.AllTopologicalOrders(p_1) + ats.allTopologicalOrders(p_2) +  ...
    # ats.allTopoligocalOrders(p_n) 
    #and upsilon == inputLinearOrders
    all_linear_extensions = []
    for p in set_poset:
        all_linear_extensions += p.linearExtensions
    if sorted(all_linear_extensions) == sorted(upsilon):
        return True
    else:
        return False