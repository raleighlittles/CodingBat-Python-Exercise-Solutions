# https://codingbat.com/prob/p124676

def near_hundred(n):
  desired_range = 10
  return ((abs(n-100) <= desired_range) or (abs(n-200) <= desired_range))