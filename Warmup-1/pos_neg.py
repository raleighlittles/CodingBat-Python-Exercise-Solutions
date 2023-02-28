# https://codingbat.com/prob/p162058

def pos_neg(a, b, negative):
  if negative:
    return ((a < 0) and (b < 0))
  else:
    # if one is positive and one is negative, then their product will always be negative
    return ((a * b) < 0)
