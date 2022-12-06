# https://codingbat.com/prob/p135815

def squirrel_play(temp, is_summer):
  upper_temp_limit = 100 if is_summer else 90
  lower_temp_limit = 60
  
  return ((temp >= lower_temp_limit) and (temp <= upper_temp_limit))
