# 以下には小問(1)〜(4)のコードを掲載しています。
# 実行したい小問のコード以外はコメントアウトするか削除してから実行してください。

# (1)
temp = list()
for n in range(10):
    data = float(input('{}個目のデータを入力 >>'.format(n+1)))
    temp.append(data)

# (2)
for count in range(len(temp)):
    print('{}時 {}度'.format(count+8, temp[count]))

# (3)
temp_new = list()
for count in range(len(temp)):
    if count == 5:
        temp_new.append('N/A')
    else:
        temp_new.append(temp[count])
print(temp)
print(temp_new)

# (4)
total = 0
for data in temp_new:
    if isinstance(data, float):
        total = total + data
print(total / (len(temp_new) - 1))