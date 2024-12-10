'''
Advent of Code
Day 3
'''

##### PART 1 #####

# Functions:


def validate_num(num) -> bool:
    try:
        int(num)
        return True
    except ValueError:
        print("Not an int. Cannot multiply.")
        return False


# Read the input file:
sum_total = 0
with open('day3_input.txt', 'r') as f:

    # chars = [char for char in f.read()]
    chars = f.read()

    for char in range(len(chars)):

        # Start by checking if the character is m and the next 3 characters are ul(:
        if (chars[char] == 'm') & (chars[(char+1):(char + 4)] == 'ul('):
            print(f"mul( detected. Looking for the next comma:")

            # Define the parentheses character:
            first_paren_index = char+3
            rest_of_string = chars[first_paren_index:]

            # Find the next comma:
            next_comma_index = rest_of_string.find(',')

            # Get characters between the parentheses and the comma:
            first_test = chars[first_paren_index:next_comma_index+1]
            print(f"First test: {first_test}")

            # Test if int type:
            if validate_num(first_test):
                first_num = int(first_test)

                # Find the next parentheses:
                second_paren_index = rest_of_string.find(')')

                # Get characters between the comma and the next parentheses:
                second_test = chars[next_comma_index:second_paren_index+1]
                print(f"Second test: {second_test}")

                # Test if int type:
                if validate_num(second_test):
                    second_num = int(second_test)

                # Get the product and increment the counter:
                product = first_num * second_num
                sum_total += product

        #         # Check the 4th character from m:
        #         if validate_num(chars[char+5]):
        #             first_num = int(chars[char+5])
        #             # print(f"First number found: {first_num}")
                    
        #             # Check the 5th character from m:
        #             if chars[char+6] == ',':

        #                 # Check the 6th character from m:
        #                 if validate_num(chars[char+7]):
        #                     second_num = int(chars[char+7])
        #                     print(f"Second number found: {second_num}")
        #                     print(f"Character after the second number: {chars[char+8]}")

        #                     # Check the 7th character from m:
        #                     if chars[char+8] == ')':
        #                         print("Last parentheses found.")

        #                         # All checks pass - get product and increment counter:
        #                         product = first_num * second_num
        #                         sum_total += product
        # else:
        #     continue

print(f"Sum Total: {sum_total}")
