# Function 1: Using Python built-in functions
# This function should take three numbers as input and return their max.
def built_in_functions_max(num1, num2, num3):
    maximum = max(num1, num2, num3)

    return (maximum)

# Function 2: Using Python built-in functions
# This function should take three numbers as input and return their min.
def built_in_functions_min(num1, num2, num3):
    minimum = min(num1, num2, num3)

    return (minimum)

# Function 3: Conditional Statements – The If Statement
# This function should check if a number is positive, negative, or zero and return the corresponding message.
def check_number(number):

    if number > 0:
        return("Positive")
    elif number < 0:
        return("Negative")
    else:
        return("Zero")

# Function 4: For Loop – Making a Star Shape
# This function should return a string representing a star shape.
def star_shape(rows):
    stars = ""

    for x in range(1, rows + 1):
        stars += ("*" * x)
        stars += ("\n")
    

    return (stars.strip())
        

# Function 5: While Loop – Counting Multiples of 3
# This function should return a list of numbers from 1 to limit, replacing multiples of 3 with "Multiple of 3".
def count_multiples_of_3(limit):
    result = ""
    x = 1

    while x <= limit:
        result = (x)
        if x % 3 == 0 :
            result += ("\n")
            result += ("Multiple of three")
        else:
            result += ("\n")
    
    x =+ 1

    return (result)



# Function 6: Sum of Even Numbers in a Range
# This function should calculate and return the sum of even numbers within a given range.
def sum_of_even_numbers(start, end):
    print

    
print(count_multiples_of_3(20))
