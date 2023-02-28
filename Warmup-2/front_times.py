# https://codingbat.com/prob/p165097

def front_times(str, n):
  str_len = len(str)
  front_length = (str_len if (str_len < 3) else 3)
  return (n * str[0:front_length])
