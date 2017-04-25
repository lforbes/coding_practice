#!/bin/python

import sys


"""
From http://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/
Also https://www.hackerrank.com/challenges/balanced-brackets
Given an expression string exp, examine whether the pairs and the orders of "{","}","(",")","[","]" are correct in exp.
For example, the program should print 'balanced' for exp = "[()]{}{[()()]()}" and 'not balanced' for exp = "[(])"
"""


def is_balanced(exp):
    """
    Description:
        Checks if given string contains balanced parentheses.
    Args:
        exp (str): String to check.
    Returns:
         str: "YES" if balanced. "NO" otherwise.
    """
    # List of opening parentheses
    opening = ['{', '(', '[']
    # List of closing parentheses
    closing = ['}', ')', ']']

    # Keep a record of opening parentheses to match with closing parentheses
    checklist = []

    for char in exp:
        if char in opening:
            checklist.append(char)
        else:
            # Only check for closing parentheses if list is not empty
            if not checklist:
                return "NO"

            # Find position of closing char in closing list
            closing_char = closing.index(char)
            # Check if corresponding char in opening list matches opening char to be removed from checklist
            if opening[closing_char] == checklist[-1]:
                # Remove matched parentheses
                del checklist[-1]
            else:
                return "NO"

    if not checklist:
        # If no chars left in checklist
        return "YES"
    return "NO"

# Get the number of strings to check
num_of_strs = int(raw_input().strip())
for _ in range(num_of_strs):
    print is_balanced(raw_input().strip())
