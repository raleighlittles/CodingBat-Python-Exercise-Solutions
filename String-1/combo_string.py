# https://codingbat.com/prob/p194053

def combo_string(a, b):
  short_str = a if ( len(a) < len(b) ) else b
  long_str = b if (short_str == a) else a
  return short_str + long_str + short_str
