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

def filter_duplicates(seq):
    seq = list(seq)
    seen = set()
    for i in seq:
        seen.add(i)
    return list(seen)
        
print("Enter number of towns")
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
# assigns all nodes to path_in_numbers list except the start/end town node
path_in_numbers = [str(i) for i in range(num_nodes) if i != start_town]
path_in_string = "".join(path_in_numbers)
permutations(path_in_string, 0)
perms_list_filtered = filter_duplicates(perms_list)

temp_path_cost = 0
minimum = 0
chosen_string_path = ''

for current_path in perms_list_filtered:
    temp_path_cost = 0
    minimum = float('inf')
    current_path = str(start_town) + current_path + str(start_town) # start/end town is added to the string
    
    for index in range(len(current_path) - 1):
        t1 = int(current_path[index])
        t2 = int(current_path[index + 1])
        temp_path_cost += matrix[t1][t2] # cost summation
    
    if temp_path_cost < minimum :
        minimum = temp_path_cost
        chosen_string_path = current_path

print(f"The shortest path {chosen_string_path} is {minimum} long.")

