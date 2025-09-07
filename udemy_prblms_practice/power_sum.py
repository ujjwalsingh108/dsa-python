def power_sum(array, power = 1):
  total = 0
  for item in array:
    if isinstance(item, list): # check if nested list
      total = power_sum(item, power + 1)
    else:
      total += item
    
  return total ** power   

