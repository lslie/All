
def counter(start=0):
	count=[start]
	def incr():
		count[0]+=1
		return count[0]

	return incr
a=counter(0)
print(a)