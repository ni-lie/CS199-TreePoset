input = [1234, 1243, 4321, 3214, 2314, 2142, 1432]

# convert the list of int to list of strings
input = [str(item) for item in input]

subgroup = [ [] for i in range(len(str(input[0])))]

for i in range(len(input)):
    subgroup[int(input[i][0])-1].append(int(input[i]))

for item in subgroup:
    item.sort()

print(subgroup)