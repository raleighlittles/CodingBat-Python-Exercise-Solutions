# https://codingbat.com/prob/p149524

def missing_char(str, n):
  if (n == 0):
    return str[n+1:len(str)]
    
  elif (n == len(str)):
    return str[0:n]
    
  else:
    return (str[0:n] + str[n+1:len(str)])