# https://codingbat.com/prob/p129125

def date_fashion(you, date):
  min_style_needed = 8
  
  if ((you <= 2) or (date <= 2)):
    return 0 # no
  
  if ((you >= min_style_needed) or (date >= min_style_needed)):
    return 2 # yes
    
  else:
    # maybe...
    return 1
