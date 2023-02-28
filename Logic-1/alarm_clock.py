# https://codingbat.com/prob/p119867

def alarm_clock(day, vacation):
  weekend_days = [0, 6] # Saturday and Sunday are the traditional weekends
  
  if day not in weekend_days: # it's a weekday
    return "10:00" if vacation else "7:00"
    
  else:
    return "off" if vacation else "10:00"
