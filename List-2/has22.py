# https://codingbat.com/prob/p1193083

def has22(nums):
  for i, elem in enumerate(nums):
    # need enough room to check for next element
    if (len(nums) > (i+1)):
      if (elem == 2) and (nums[i+1] == 2):
        return True
        
  return False
