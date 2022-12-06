# https://codingbat.com/prob/p186048

def count_code(str):
  
  # Regex would be an easy way to solve this, but can't use them here
  
  occurences = 0
  
  for idx, ch in enumerate(str):
    if (ch == 'c'):
      
      # make sure there's enough string left, ie. that there are at least 3 characters
      # left to spell out 'co_e'
      if (len(str) > (3 + idx)):
        # check that next letter is o, and then two letters after is e
        if (((str[idx + 1]) == 'o') and ((str[idx + 3]) == 'e')):
          occurences += 1
          
      else:
        # Not enough string left, so there's no possibility of finding substring
        return occurences
    
  return occurences
        
