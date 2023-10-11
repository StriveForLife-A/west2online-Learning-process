list = ["west2online", 12345678, "Python", 12345, 234, 456]
new_list = []
for i in list:
    if type(i) == int:
        new_list.append(i)
new_list.sort()
print(new_list)
