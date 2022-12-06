# https://codingbat.com/prob/p149391

def xyz_there(str):
  
  target_str = "xyz"
  xyz_index = str.find(target_str)
  
  if (xyz_index == 0):
    # string starts with 'xyz', so there can't be a period before it
    return True
    
  elif (xyz_index == -1):
    # the substring wasn't found at all
    return False
    
  else:
    # More complex case. Iterate through the string, window searching
    for i, ch in enumerate(str):
      if (i > 0):
        # Target substring found
        if ((str[i-1] != ".") and (str[i:i+3] == target_str)):
          return True
          
    # Made it to the end without finding anything
    return False
    
    
