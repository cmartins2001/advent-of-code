'''
Advent of Code
Day 2
'''

##### PART 1 #####

test_list = [1,57,3,4,80]

# Functions:


def check_if_ascending(numbers) -> bool:
    '''Checks if a list of numbers is in ascending order.'''
    if numbers == sorted(numbers, reverse=False):
        return True
    else:
        return False
    

def check_if_descending(numbers) -> bool:
    '''Checks if a list of numbers is in descending order.'''
    if numbers == sorted(numbers, reverse=True):
        return True
    else:
        return False
    

def check_adjacent_numbers(numbers) -> bool:
    '''Checks if the absolute difference between adjacent list items is in the range [1,3].'''
    unsafe_count = 0
    # Iterate up until the last item:
    for x in range(len(numbers)-1):
        adj_diff = abs(numbers[x] - numbers[x+1])
        # Range test:
        if (adj_diff > 3) or (adj_diff < 1):
            unsafe_count += 1
    if unsafe_count > 0:
        return False
    else:
        return True
    

def group_check(numbers) -> bool:
    '''Uses upstream validation functions to check the list for all conditions.'''
    # Check if list is ascending:
    if check_if_ascending(numbers):
        # Check if adjacent numbers are safe:
        if check_adjacent_numbers(numbers):
            # Increment the passed counter:
            return True

    # If not ascending, check if list is descending:
    elif check_if_descending(numbers):
        # Check if adjacent numbers are safe:
        if check_adjacent_numbers(numbers):
            # Increment the passed counter:
            return True
        
    else:
        return False


# Initialize safe report counter:
safe_report_count = 0

# Read the input file:
with open('day2_input.txt', 'r') as f:

    for line in f.readlines():

        # Extract the five numbers:
        num_list = line.split(' ')

        # Convert them to integer types:
        int_list = [int(x) for x in num_list]

        # Testing:
        if group_check(int_list):
            safe_report_count += 1

        # # Initialize a flag for unsafe:
        # unsafe = False

        # # Check if list is ascending:
        # if check_if_ascending(int_list):
        #     # Check if adjacent numbers are safe:
        #     if check_adjacent_numbers(int_list):
        #         # Increment safe report counter:
        #         safe_report_count += 1

        # # If not ascending, check if list is descending:
        # elif check_if_descending(int_list):
        #     # Check if adjacent numbers are safe:
        #     if check_adjacent_numbers(int_list):
        #         # Increment safe report counter:
        #         safe_report_count += 1
        # else:
        #     unsafe = True
            
    # Close the file:
    f.close()

# Print the safe report count:
print(f"Number of safe reports in Part 1: {safe_report_count}")

##### PART 2 #####

# Initialize safe report counter and loop variable:
safe_report_count_v2 = 0
dampener_loop = True

# Read the input file:
with open('day2_input.txt', 'r') as f:

    for line in f.readlines():

        # Extract the five numbers:
        num_list = line.split(' ')

        # Convert them to integer types:
        int_list = [int(x) for x in num_list]

        # Standard checks:
        if group_check(int_list):
            safe_report_count_v2 += 1

        # Dampener check:
        else:

            while dampener_loop:
            
                # Introduce the problem dampener:
                for i in range(len(int_list)):

                    # # Temporarily remove the current item:
                    temp_num_list = int_list.copy()
                    temp_num_list.pop(i)

                    # Run a group check on the temporary list:
                    if group_check(temp_num_list):
                        # Increment the counter and end the while loop:
                        safe_report_count_v2 += 1
                        dampener_loop = False

                    # Allow the while loop to end on the last number without incrementing:
                    elif (not group_check(temp_num_list)) & (i == len(temp_num_list)):
                        dampener_loop = False

# Print the safe report count:
print(f"Number of safe reports in Part 2: {safe_report_count_v2}")


# # Test functions:
# test_list2 = [1, 2, 56, 3, 4]
# print(f"Test List: {test_list}")

# test = True

# # Introduce the problem dampener:
# while test:
#     for i in range(len(test_list2)):

#         # Temp safety counter (can only have 1 safe case per report):
#         temp_safety_counter = 0

#         # # Temporarily remove the current item:
#         temp_num_list = test_list2.copy()
#         temp_num_list.pop(i)

#         # Run a group check on the temporary list:
#         if group_check(temp_num_list):
#             # Increment the counter and end the while loop:
#             safe_report_count_v2 += 1
#             test = False
        
#         # Allow the while loop to end on the last number without incrementing:
#         elif (not group_check(test_list2)) & (i == len(test_list2)):
#             test = False

# print(safe_report_count_v2)
