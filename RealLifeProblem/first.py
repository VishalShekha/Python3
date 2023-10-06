import math

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Function to count the number of children with prime tokens
def count_prime_children(node, token_numbers, adjacency_list):
    count = 0
    if is_prime(token_numbers[node - 1]):
        count += 1
    for child in adjacency_list[node]:
        count += count_prime_children(child, token_numbers, adjacency_list)
    return count

# Function to build the adjacency list representing the family tree
def build_tree_adjacency_list(parents):
    adjacency_list = [[] for _ in range(len(parents) + 1)]
    for i in range(len(parents)):
        adjacency_list[parents[i]].append(i + 2)
    return adjacency_list

# Read input
N = int(input())
token_numbers = list(map(int, input().split()))
parents = [int(x) for _ in range(N - 1) for x in input().split()]
Q = int(input())
queries = [int(input()) for _ in range(Q)]

# Build the family tree as an adjacency list
adjacency_list = build_tree_adjacency_list(parents)

# Answer the queries
for query in queries:
    result = count_prime_children(query, token_numbers, adjacency_list)
    print(result)