# Question: http://practice.geeksforgeeks.org/problems/check-if-divisible-by-5/0
# Given solution: http://www.geeksforgeeks.org/check-large-number-divisible-5-not/


def div_by_5(number):
    """
    Description:
        Checks whether a number is divisible by 5.
    Args:
        number (int/str): Number to check.
    Returns:
        int: 1 if divisible, 0 if not divisible.
    """
    # If given str, get last char and change to int
    if type(number) == str:
        num_check = int(number[-1])
    elif type(number) == int:
        # Get last digit
        num_check = number % 10
    else:
        return "INVALID ARGUMENT: {0}".format(number)

    if num_check % 5 == 0:
        return 1
    return 0

num_test_cases = int(raw_input("Number of Test Cases: "))

for _ in range(num_test_cases):
    print div_by_5(raw_input("Number to check: "))
