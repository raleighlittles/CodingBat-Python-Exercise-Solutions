# https://codingbat.com/prob/p174314

def end_other(a, b):
  a_length, b_length = len(a), len(b)
  lowercase_a = a.lower()
  lowercase_b = b.lower()
  
  # Trivial case: both strings are the same length.
  # They're either the same (vacuously True) or different (obviously False)
  if (a_length == b_length):
    return (lowercase_a == lowercase_b)
  
  else:
    # Find whichever string is the longest, search for the other in it...
    if (a_length > b_length):
      # For a substring of length `l`, search only the last `l` characters in the original string
      return (lowercase_a.find(lowercase_b, a_length - b_length) != -1)
      
    else: # (a_length < b_length)
      return (lowercase_b.find(lowercase_a, b_length - a_length) != -1)
  
