#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  outputs = ['rock', 'paper', 'scissors']

  def next_perm(perm, n):
    if n == 0:
      return perm
    permutations = []
    for arr in perm:
      for hand in outputs:
        permutations.append([*arr, hand])
    return next_perm(permutations, n - 1)

  return next_perm([[]], n)

# print(rock_paper_scissors(3))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')