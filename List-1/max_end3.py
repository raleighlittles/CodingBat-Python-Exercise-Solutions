# https://codingbat.com/prob/p135290

def max_end3(nums):
  nums_length = len(nums)
  max_element = nums[0] if (nums[0] > nums[nums_length-1]) else nums[nums_length-1]
  # Without lists?
  return [max_element, max_element, max_element]
