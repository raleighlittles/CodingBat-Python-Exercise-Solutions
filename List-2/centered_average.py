# https://codingbat.com/prob/p126968

def centered_average(nums):
  # Sort the array
  sorted_nums = sorted(nums)
  arr_length = len(nums)
  # Minus 2 because you're disregarding min and max
  return (sum(sorted_nums[1:arr_length-1]) / (arr_length - 2))
