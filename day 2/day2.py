'''
Advent of Code
Day 2
'''

##### PART 1 #####

# Initialize safe report counter:
safe_report_count = 0

# Read the input file:
with open('day2_input.txt', 'r') as f:

    for line in f.readlines():

        # Extract the five numbers:
        num_list = line.split(' ')

        # Convert them to integer types:
        int_list = [int(x) for x in num_list]

        # Check work:
        # print(int_list)

        # Check 1 - all increasing?
        loop1 = True
        for i in range(len(int_list)):
            while int_list[i+1] > int_list[i]:
                continue
            
