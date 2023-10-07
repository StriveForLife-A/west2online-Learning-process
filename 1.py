x=int(input("请输入第一个数："))
y=int(input("请输入第二个数："))
z=int(input("请输入第三个数："))

#方法一，利用列表
h=[x,y,z]
f=" "
h.sort()
h.reverse()
print(h)
#如果指定输出字符串
for i in h:
    f+=str(i)+", "
print(f)

#方法二，利用max，min等函数
maxnum=max(x,y,z)
minnum=min(x,y,z)
midnum=x+y+z-maxnum-minnum
print(maxnum,midnum,minnum)