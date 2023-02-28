# https://codingbat.com/prob/p120546

def monkey_trouble(a_smile, b_smile):
  # Conditions match up with XNOR 
  return not ((a_smile ^ b_smile))
