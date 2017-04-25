# Question: http://practice.geeksforgeeks.org/problems/check-if-divisible-by-5/0
# Given solution: http://www.geeksforgeeks.org/check-large-number-divisible-5-not/

num_test_cases = input()
num_test_cases = int(num_test_cases)

for _ in range(num_test_cases):
    num_to_check = input()
    num_to_check = int(num_to_check[-1])
    if num_to_check % 5 == 0:
        print(1)
    else:
        print(0)
