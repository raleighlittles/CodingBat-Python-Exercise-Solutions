# https://codingbat.com/prob/p167025

def sum13(nums):
  if not nums:
    # empty array
    return 0
    
  else:
    running_sum, idx = 0, 0
    
    while (idx < len(nums)):
      if (nums[idx] == 13):
        # Skip next element
        idx += 2
        
      else:
        # Safe to add
        running_sum += nums[idx]
        idx += 1
        
    return running_sum
        
