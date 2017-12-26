def function(n):
	d = dict()
	for i in range(1,n+1):
		d[i] = i*i
	return d

a = int(input("Enter the no. you want : "))
result = function(a)
print(result)