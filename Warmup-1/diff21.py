# https://codingbat.com/prob/p197466

def diff21(n):
  abs_diff = abs(n-21)
  return (abs_diff if (n <= 21) else (2 * abs_diff))
