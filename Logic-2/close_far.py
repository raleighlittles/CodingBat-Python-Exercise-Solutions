# https://codingbat.com/prob/p160533

def close_far(a, b, c):
  
  ab_dist = abs(b-a)
  bc_dist = abs(b-c)
  ac_dist = abs(c-a)
  
  if (ab_dist <= 1): # if b is close, then c must be far
    return ((bc_dist >= 2) and (ac_dist >= 2))
    
  elif (ac_dist <= 1): # if c is close, then b must be far
    return ((ab_dist >= 2) and (bc_dist >= 2))
    
  else: # values are spread out normally
    return False
