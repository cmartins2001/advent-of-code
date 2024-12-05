'''
Advent of Code
Day 2
'''

##### PART 1 #####

test_list = [1,57,3,4]

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

# Initialize safe report counter:
safe_report_count = 0

# Read the input file:
with open('day2_input.txt', 'r') as f:

    for line in f.readlines():

        # Extract the five numbers:
        num_list = line.split(' ')

        # Convert them to integer types:
        int_list = [int(x) for x in num_list]

        # Initialize a flag for unsafe:
        unsafe = False

        # Check if list is ascending:
        if check_if_ascending(int_list):
            # Check if adjacent numbers are safe:
            if check_adjacent_numbers(int_list):
                # Increment safe report counter:
                safe_report_count += 1

        # If not ascending, check if list is descending:
        elif check_if_descending(int_list):
            # Check if adjacent numbers are safe:
            if check_adjacent_numbers(int_list):
                # Increment safe report counter:
                safe_report_count += 1
        else:
            unsafe = True
            
    # Close the file:
    f.close()

# Print the safe report count:
print(f"Number of safe reports: {safe_report_count}")
