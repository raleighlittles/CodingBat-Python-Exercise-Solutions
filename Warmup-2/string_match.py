# https://codingbat.com/prob/p182414

def string_match(a, b):
  
  a_len, b_len = len(a), len(b)
  # Trivial case
  if ((a_len < 2) or (b_len < 2)):
    return 0
  
  num_matches = 0
  # Need to leave room at the end for searching ahead
  for i in range(0, a_len):
    if (a_len >= (i + 2)) and (b_len >= (i + 2)) and (a[i:i+2] == b[i:i+2]):
      num_matches += 1

      
  return num_matches
