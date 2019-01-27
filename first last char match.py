_list = ['abc', 'xyz', 'aba', '1221']
counter = 0

for each in _list:
    if len(each) > 1 and each[0] == each[-1]:
        counter += 1
print(counter)
