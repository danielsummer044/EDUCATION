"""
N = 10

* * * * *
 * * * * *
* * * * *
 * * * * *
* * * * *
 * * * * *
* * * * *
 * * * * *
* * * * *
 * * * * * 
"""
N = 4
flag = False

for i in range(N):
	if flag:
		print((" " + "*") * N)
		flag = False
	else:
		print(("*" + " ") * N)
		flag = True