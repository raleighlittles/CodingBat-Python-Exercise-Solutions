# https://codingbat.com/prob/p158497

def in1to10(n, outside_mode):
  lower, upper = 1, 10
  if outside_mode:
    return ((n <= lower) or (n >= upper))
  else:
    return ((n >= lower) and (n <= upper))
