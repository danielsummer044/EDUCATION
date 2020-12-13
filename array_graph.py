# 1000 -> *
n = 1000
birth = [10000, 20000, 15000, 8000, 12000, 1000, 3000, 30000, 12000, 8000, 7000, 2000]

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


for i in range(len(birth)):
	t = birth[i] // n
	print(months[i] + " " + "*" * t)