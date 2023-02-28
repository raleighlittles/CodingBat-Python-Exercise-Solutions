# https://codingbat.com/prob/p145834

def last2(str):
  
  str_len = len(str)
  
  if (str_len < 2):
    return 0
    
  else:
    end_substr = str[str_len-2:str_len]
    counts = 0
    for i in range(0, str_len - 2):
      if (str[i:i+2] == end_substr):
        counts += 1
        
    return counts
