names = list() # リストの場合
print(f'list（変更前）: {id(names)}')
names.append('松田')
print(f'list（変更後）: {id(names)}')

name = '松田'   # 文字列の場合
print(f'str（変更前）: {id(names)}')
name = 'スーパー' + name
print(f'str（変更後）: {id(names)}')