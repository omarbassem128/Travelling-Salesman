def swp(s, index1, index2):
    swapped = list(s)
    swapped[index1], swapped[index2] = swapped[index2], swapped[index1]
    return ''.join(swapped)

def permutations(s, i):
    if i == len(s)-1:
        return perms_list
    for j in range(i, len(s)):
        temporary = swp(s, i, j)
        perms_list.append(temporary)
        permutations(temporary, i+1)



print("Enter number of nodes")
num_nodes = int(input())
perms_list = []
# inner comprehension creates num_nodes number of zeroes, 
# while the outer comprehension creates num_nodes number of lists.
matrix = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]
print("Enter start town zero-indexed")
start_town = int(input())
for i in range(num_nodes):
    for j in range(i+1, num_nodes):
        print(f"Enter distance between town {i} and town {j}")
        matrix[i][j] = int(input())
        matrix[j][i] = matrix[i][j]
""" for i in range(num_nodes):
    print(matrix[i]) """
path_in_numbers = [str(i) for i in range(num_nodes) if i != start_town]
path_in_string = "".join(path_in_numbers)
permutations(path_in_string, 0)

print(perms_list)