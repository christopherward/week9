#Christopher Ward
#MPCS 50101, Winter 2015
#Homework 6
import random

def sort(items):
  # 1. TO DO: Implement a "bubble sort" routine here
  swap = -1
  i = -1

  #while-loop conditions determine whether complete pass was made without a swap
  while swap != 0 or i != (len(items) - 1):
    i = 0
    swap = 0
    #while-loop condition determines whether two adjacent values need to be swapped
    while i < (len(items) - 1):
      if items[i] > items[i+1]:
        items[i], items[i+1] = items[i+1], items[i]
        swap = 1
      i += 1
  return items



numbers = list(range(10))
random.shuffle(numbers)

assert list(range(10)) == sort(numbers)
print("The list was sorted correctly!")

# 2. Change this print statement to display the complexity category.
#    Refer to the cheat sheet in week9-class for examples.
print("This algorithm is classified as: O(n^2)")
