list = [1,1,2,3,4,6,8,1,'banana','banana']
cleanlist =[]
for info in list:
    if info not in cleanlist:
        cleanlist.append(info)

print(cleanlist)