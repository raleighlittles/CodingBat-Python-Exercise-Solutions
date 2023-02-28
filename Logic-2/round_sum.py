# https://codingbat.com/prob/p179960

def round_sum(a, b, c):
  return int(sum([round10(a), round10(b), round10(c)]))
  
def round10(num):
  # Special Python hack
  return round(num, -1)
