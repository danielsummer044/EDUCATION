def pominyatu(i,j):
    temp = cinu[i]
    cinu[i] = cinu[j]
    cinu[j] = temp

    temp = tovaru[i]
    tovaru[i] = tovaru[j]
    tovaru[j] = temp


def znaitu_min(index):
    min_cina = cinu[index]
    min_cina_index = index
    for i in range(index, len(cinu)):
        if min_cina > cinu[i]:
            min_cina = cinu[i]
            min_cina_index = i
    return min_cina_index

def znaitu_i_pominyatu_min(index):
    min_cina_index = znaitu_min(index)
    pominyatu(min_cina_index, index)



tovaru = ['хліб', 'молоко', 'риба', 'олія', 'масло']
cinu =   [  17,     25.99,   75.50,    32.90,   40]
for i in range(len(cinu)):
    znaitu_i_pominyatu_min(i)

print(cinu)
print(tovaru)

