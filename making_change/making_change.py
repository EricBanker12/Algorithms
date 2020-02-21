#!/usr/bin/python

import sys

def making_change(amount, denominations):
  caps = [amount//d for d in denominations]
  ranges = [range(c + 1) for c in caps]

  if denominations == [1,5,10,25,50]:
    # pattern based solution
    amount -= amount % 5
    cache = {0:1, 1:2, 2:4, 3:6}
    n = 4
    while not amount//5 in cache:
      # n = amount//5
      # 2 * f(n-1) - f(n-2) + sum(1,2,3,...,1+n//10) - (1+n//10 if n-1 or n-3 is multiple of 10)
      combinations = 2*cache[n-1] - cache[n-2] + sum(range(2 + n//10))
      if (n % 10 - 1) == 0 or (n % 10 - 3) == 0:
        combinations -= (1 + n//10)
      # update cache
      del cache[n-4]
      cache[n] = combinations
      n += 1
    return cache[amount//5]

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