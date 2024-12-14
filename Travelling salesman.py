class Town:
    def __init__(self, p):
        self.pos = p
    
    def __str__(self):
        return str(self.pos)
    
    def __repr__(self):
        return str(self)
    
    def __eq__(t1, t2):
        return t1.pos == t2.pos
    
    def __hash__(self):
        return hash(self.pos)

def swp(s, index1, index2):
    swapped = list(s)
    swapped[index1], swapped[index2] = swapped[index2], swapped[index1]
    return swapped

def permutations(s, i):
    if i == len(s)-1:
        return perms_list
    for j in range(i, len(s)):
        temporary = swp(s, i, j)
        perms_list.append(tuple(temporary))
        permutations(temporary, i+1)

def filter_duplicates(seq):
    seq = list(seq)
    seen = set()
    for i in seq:
        seen.add(i)
    return list(seen)

def minimum_path_size(perms_list_filtered):
    temp_path_cost = 0
    minimum = 0
    chosen_string_path = ''
    for current_path in perms_list_filtered:
        temp_path_cost = 0
        minimum = float('inf')
        current_path = ((start_town,) + current_path + (start_town,))
        # start/end town is added to the string
        
        for index in range(len(current_path) - 1):
            t1 = current_path[index].pos
            t2 = current_path[index + 1].pos
            temp_path_cost += matrix[t1][t2] # cost summation
        
        if temp_path_cost < minimum :
            minimum = temp_path_cost
            chosen_string_path = current_path
    
    return chosen_string_path, minimum


print("Enter the number of towns: ", end='')
num_nodes = int(input())
print("Enter the starting town (zero-indexed): ", end='')
start_town = Town(int(input()))

# inner comprehension creates num_nodes number of zeroes, 
# while the outer comprehension creates num_nodes number of lists.
matrix = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]
perms_list = []

print("Enter the distances between all towns:")
for i in range(num_nodes):
    for j in range(i+1, num_nodes):
        print(f"Towns {i} and {j}: ", end='')
        matrix[i][j] = int(input())
        matrix[j][i] = matrix[i][j]

# assigns all nodes to path_in_numbers list except the start/end town node
path_in_numbers = [Town(i) for i in range(num_nodes) if i != start_town.pos]
permutations(path_in_numbers, 0)
perms_list_filtered = filter_duplicates(perms_list)

print(perms_list_filtered)

(string_path, path_size) = minimum_path_size(perms_list_filtered)
print(f"The shortest path {string_path} is {path_size} long.")
