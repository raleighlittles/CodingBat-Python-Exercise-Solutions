# https://codingbat.com/prob/p153599

def front_back(str):
  # Trivial case
  if len(str) < 2:
    return str
    
  else:
    str_len = len(str)
    return (str[str_len - 1] + str[1:str_len-1] + str[0])
