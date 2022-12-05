# https://codingbat.com/prob/p179078

def same_first_last(nums):
  # The productive case, eg [1, 2, 3, 1]
  if ((len(nums) > 1) and (nums[0] == nums[len(nums)-1])):
    return True
    
  elif len(nums) == 1: # The trivial case
    return True
    
  else:
    return False
