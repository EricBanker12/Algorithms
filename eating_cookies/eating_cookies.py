#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  # 1,1,2,4,7,13,24,44,81,149... n=(n-1)+(n-2)+(n-3)
  if not cache or not cache[0]:
    cache = [1,1,2]
  try:
    return cache[n]
  except IndexError:
    result = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
    cache.append(result)
    return result

import random
def generate_perm(n):
  """generate permutations through brute force"""
  results = set()
  for i in range(1,n+1):
    for j in range(100000):
      test = [random.choice([1,2,3]) for k in range(i)]
      if sum(test) == n:
        results.add(str(test))
  return results

# print(len(generate_perm(3)))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')