# https://codingbat.com/prob/p195669

def cigar_party(cigars, is_weekend):
  if (cigars >= 40):
    if is_weekend:
      return True
    else:
      if (cigars <= 60):
        return True
      else:
        # Too many cigars
        return False
  else:
    # Not enough cigars
    return False
