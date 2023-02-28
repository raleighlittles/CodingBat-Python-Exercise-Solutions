# https://codingbat.com/prob/p116620

def sorta_sum(a, b):
  
  sum_result = sum([a, b])
  
  return (20 if ((sum_result >= 10) and (sum_result <= 20)) else sum_result)
