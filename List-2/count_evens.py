# https://codingbat.com/prob/p189616

def count_evens(nums):
  # any number divisible by 2 is even
  return sum([ ((x % 2) == 0) for x in nums])
