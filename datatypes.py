def data_type(n=None):
  
  if type(n) == str:
    return len(n)
    
  elif n == None:
    return "no value"
    
  elif type(n) == bool:
    return n
    
  elif type(n) == int:
    if n < 100:
      return 'less than 100'
    elif n == 100:
      return "equal to 100"
    else:
      return 'more than 100'
      
  elif type(n) == list:
    if len(n) >= 3:
      return n[2]
    else:
      return None