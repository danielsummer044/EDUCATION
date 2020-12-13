n = 75312
 
sum_cifr = 0

while n > 0:
	sum_cifr = sum_cifr + n % 10 
	n = n // 10

print(sum_cifr)