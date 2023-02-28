# https://codingbat.com/prob/p193604

def array123(nums):
  
  for idx, elem in enumerate(nums):
    if (elem == 1):
      if ((len(nums) > (idx + 2)) and (nums[idx+1] == 2) and (nums[idx+2] == 3)):
        return True
        
  return False
