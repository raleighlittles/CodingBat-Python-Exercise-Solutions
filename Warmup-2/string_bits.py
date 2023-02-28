# https://codingbat.com/prob/p113152

def string_bits(str):
  result_str = ""
  for i in range(0, len(str)):
    if i % 2 == 0: # even indices: [0, 2, 4, ...]
      result_str += str[i]
      
  return result_str
      
