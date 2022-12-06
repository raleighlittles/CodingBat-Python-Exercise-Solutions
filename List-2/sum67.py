# https://codingbat.com/prob/p108886

def sum67(nums):
  
  # Trivial case, array is empty
  if not nums:
    return 0
    
  running_sum, safe_to_add = 0, True
  
  for idx, elem in enumerate(nums):
    if elem == 6:
      safe_to_add = False
      
    if elem == 7:
      # Reset the flag if its up, otherwise add
      if not safe_to_add:
        safe_to_add = True
        continue
      
    if safe_to_add:
      running_sum += elem
      
  return running_sum
    
