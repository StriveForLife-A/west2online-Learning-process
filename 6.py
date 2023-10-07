lists = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 11, 22, 33]
dict = {}
for num  in lists:
    if num not in dict:
        dict[num]=1
    else:
        dict[num]+=1
print(dict)
