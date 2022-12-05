# https://codingbat.com/prob/p192589

def sum2(nums):
  arr_length = len(nums)
  
  if (arr_length < 2):
    return sum(nums)
    
  else:
    return sum(nums[0:2])
