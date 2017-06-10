"""
From https://www.hackerrank.com/challenges/compare-the-triplets
"""
#!/bin/python

import sys

def solve(a0, a1, a2, b0, b1, b2):
    alice_in = (a0, a1, a2)
    bob_in = (b0, b1, b2)
    # Comparison Points
    alice, bob = 0, 0
    
    for count, num in enumerate(alice_in):
      if alice_in[count] > bob_in[count]:
        alice += 1
      elif alice_in[count] != bob_in[count]:
        bob += 1
    
    return alice, bob

a0,a1,a2 = raw_input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = raw_input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print " ".join(map(str, result))
