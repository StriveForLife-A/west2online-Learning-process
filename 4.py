list=["west2online",12345678,"Python",12345,]
newlist=[]
for i in list:
    if type(i)==int:
        newlist.append(i)
print(sorted(newlist))