text = 'skueryiweruwoieuo'


substring = 'wer'  # 7 - індекс початку підрядка

#substring = 'abc' # -1 - підрядка немає

#print(text.index(substring))

found = True
for i in range(len(text)):
    if i > len(text) - len(substring):
        break
    found = True
    for j in range(len(substring)):
        if text[i+j] != substring[j]:
            found = False
            break
    if found:
        print(i)
        break

if not found:
    print(-1)
