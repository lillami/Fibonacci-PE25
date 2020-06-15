#EULER PRoject Problem 25

def fib():
	count = 1
	current = 0
	last = 0
	while count:
		new = current + last
		if count == 1:
			new += 1
		elif len(str(new)) == 1000:
			print(count)
			break
		last = current
		current = new
		count += 1	

fib()