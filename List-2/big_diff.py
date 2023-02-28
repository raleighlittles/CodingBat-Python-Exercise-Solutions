# https://codingbat.com/prob/p184853

def big_diff(nums):
  # Rather than using max()/min() directory, just sort array
  sorted_nums = sorted(nums)
  return abs(sorted_nums[-1] - sorted_nums[0])
