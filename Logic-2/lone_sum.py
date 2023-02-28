# https://codingbat.com/prob/p143951

def lone_sum(a, b, c):
  
  starting_sum = sum([a, b, c])
  
  if (a == b):
    # The terms that are equal don't count in the sum
    starting_sum = starting_sum - (a+b)
    
  if (b == c):
    starting_sum = starting_sum - (b+c)
    
  if (a == c):
    starting_sum = starting_sum - (a+c)
    
  # If you're negative, then all terms are equal
  return starting_sum if (starting_sum > 0) else 0
