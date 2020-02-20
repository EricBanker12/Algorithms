#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
  combinations = set()
  for item in items:
    combinations.add((item,))
  while True:
    temp = set()
    temp_cleanup = set()
    for combo in combinations:
      for item in items:
        # add new items to combo, if they fit
        if not item in combo:
          if sum([it[1] for it in combo]) <= capacity - item[1]:
            combi = [*combo, item]
            combi.sort(key=lambda item: item[0])
            temp.add(tuple(combi))
            temp_cleanup.add(combo)
    # delete combos that were extended
    for combo in temp_cleanup:
      combinations.remove(combo)
    for combo in temp:
      combinations.add(combo)
    # end loop if no combos were extended
    if not temp:
      break
  # return highest value combo
  max_combo = None
  max_value = None
  for combo in combinations:
    value = sum([item[2] for item in combo])
    if not max_value or value > max_value:
      max_value = value
      max_combo = combo
  return {'Value': max_value, 'Chosen': [item[0] for item in max_combo]}


if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')