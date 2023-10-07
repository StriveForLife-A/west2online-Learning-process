info_dict = {123456: "张三",
             129585: "王五",
             142857: "郑七",
             114514: "田二"}
new_dict = {}
for key in info_dict:

    if key % 2 == 0:
        new_dict[key]=info_dict[key]

print(new_dict)