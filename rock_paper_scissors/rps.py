#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  outputs = ['rock', 'paper', 'scissors']
  permutations = []

  if n < 1:
    return [[]]

  for hand in outputs:
    permutations.append([hand])
  
  while len(permutations[-1]) < n:
    for arr in permutations.copy():
      for hand in outputs:
        permutations.append([*arr, hand])
  
  return [perm for perm in permutations if len(perm) == n]

# print(rock_paper_scissors(3))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')