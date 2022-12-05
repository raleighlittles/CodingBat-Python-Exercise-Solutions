# https://codingbat.com/prob/p181624

def first_last6(nums):
  target_val = 6
  return ((nums[0] == target_val) or (nums[-1] == target_val))
