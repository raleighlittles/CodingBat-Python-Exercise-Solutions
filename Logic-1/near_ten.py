# https://codingbat.com/prob/p165321

def near_ten(num):
  remainder = (num % 10)
  
  # within 2 means you could either go up by 2 (from 8 to 10, an even divisor)
  # OR go down by 2, i.e. subtract 2 to get to 0 (another even divisor)
  return ((remainder >= 8) or (remainder <= 2))
