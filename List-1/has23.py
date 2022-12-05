# https://codingbat.com/prob/p177892

def has23(nums):
  # Would normally use `any()`, but can't use loops according to directions
  if 2 in nums:
    return True
    
  if 3 in nums:
    return True
    
  return False
