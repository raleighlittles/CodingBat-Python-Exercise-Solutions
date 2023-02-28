# https://codingbat.com/prob/p137202

def caught_speeding(speed, is_birthday):
  speed_allowance = 5 if is_birthday else 0
  
  low_ticket_lim, high_ticket_lim = 60, 81
  
  if (speed > (low_ticket_lim + speed_allowance)):
    if (speed > (high_ticket_lim + speed_allowance)):
      return 2
      
    else:
      return 1
    
  else: # Not speeding
    return 0
  
