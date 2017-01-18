def min_max(number):
	a = min (number)
	b = max (number)
	
	if a == b:
	  return [len(a)]
	return [a, b]

print (min_max([2, 5, 3, 4, 7]))

