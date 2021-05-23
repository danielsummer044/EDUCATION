filename = 'chisla.txt'

"""
f = open(filename)
content = f.read()
f.close()
"""

with open(filename) as f:
    content = f.read()

chisla = [int(chislo) for chislo in content.split()]
print(sum(chisla))