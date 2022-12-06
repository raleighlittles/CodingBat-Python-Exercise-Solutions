# https://codingbat.com/prob/p118366

def string_splosion(str):
  str_len = len(str)
  result_str = ""
  for i in range(0, str_len):
    result_str += str[0:i+1]
    
  return result_str
    
