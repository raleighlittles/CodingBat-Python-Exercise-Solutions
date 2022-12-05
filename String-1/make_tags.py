# https://codingbat.com/prob/p132290

def make_tags(tag, word):
  start_tag, end_tag = ("<" + tag + ">"), ("</" + tag + ">")
  return (start_tag + word + end_tag)
