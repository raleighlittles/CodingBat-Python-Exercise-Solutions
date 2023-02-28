# https://codingbat.com/prob/p100347

def no_teen_sum(a, b, c):
  
  return sum([fix_teen(a), fix_teen(b), fix_teen(c)])
  
  
def fix_teen(n):
  if n in [13, 14, 17, 18, 19]: # problem says to skip 15 and 16
      return 0
  else:
    return n
