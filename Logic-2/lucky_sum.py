# https://codingbat.com/prob/p107863

def lucky_sum(a, b, c):
  # Not supposed to use loops... prevents you from making a more generic approach
  disallowed_value = 13
  
  if (a == disallowed_value):
    # everything to the right is discarded
    return 0
    
  elif (b == disallowed_value):
    return a
    
  elif (c == disallowed_value):
    return (a+b)
    
  else: # all values are good
    return (a + b + c)
