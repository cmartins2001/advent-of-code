'''
Advent of Code
Day 1
'''

##### PART 1 #####

# Read the input file:
with open('day1_input.txt', 'r') as f:

    # Initialize:
    count = 0
    first_list = []
    second_list = []

    for line in f.readlines():

        count += 1

        # Identify the first number:
        first_space = line.find(' ')
        first_num = int(line[0:(first_space)])

        # Extract the second number:
        second_num = int(line[(first_space + 3):])

        # Append the numbers to their lists:
        first_list.append(first_num)
        second_list.append(second_num)

    # Close the file:
    f.close()

# Sort the lists in ascending order:
for x in [first_list, second_list]:
    x = x.sort()

# Compute the "distance" between the sorted values:
total_distance = 0
for first, second in zip(first_list, second_list):
    dist = abs(first - second)
    total_distance += dist

# Solution 1:
print(f"Total Distance Between Sorted List Items: {total_distance}")

##### PART 2 #####
from collections import Counter

# Initialize the similiarity score:
sim_score = 0

for first_item in first_list:

    # For each item in the first list, find how many times it appears in the second list:
    item_count = second_list.count(first_item)
    
    # Multiply the instance count by the item itself:
    delta = item_count * first_item

    # Change the similarity score by delta:
    sim_score += delta

print(f"\nSimilarity Score: {sim_score}")
