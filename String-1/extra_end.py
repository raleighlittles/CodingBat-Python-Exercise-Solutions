# https://codingbat.com/prob/p148853

def extra_end(str):
  str_len = len(str)
  return (str[str_len - 2 : str_len] * 3)
