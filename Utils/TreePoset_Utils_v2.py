def linear_order_to_binary_relation(order):
    """
    Takes a linear order as input and returns its binary relation as a list of tuples.
    """
    n = len(order)
    relation = []
    for i in range(n):
        for j in range(i+1, n):
            relation.append((int(order[i]), int(order[j])))
    return relation

# # Example usage:
# order = '12345'
# relation = linear_order_to_binary_relation(order)
# print(relation)

