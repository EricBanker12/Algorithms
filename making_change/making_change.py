#!/usr/bin/python

import sys

def making_change(amount, denominations):
  caps = [amount//d for d in denominations]
  ranges = [range(c + 1) for c in caps]

  # all combinations
  combinations = [[]]
  for i in range(len(denominations)):
    p = []
    for arr in combinations:
      for n in ranges[i]:
        combi = [*arr, n*denominations[i]]
        # filter greater than ammount
        if sum(combi) <= amount:
          p.append(combi)
    combinations = p

  # filter less than amount
  combinations = [p for p in combinations if sum(p) == amount]

  # return count
  return len(combinations)

# for i in range(0,501,5):
#   print(f'{i},{making_change(i, [1,5,10,25,50])}')

# import timeit
# t = timeit.timeit('making_change(300, [1,5,10,25,50])', globals=globals(), number=1)
# print(t)

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")