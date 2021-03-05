list=[10,20,110,30,40,300]
result=[]
for i in list:
    if i>100:
        result.append('over')
    else:
        result.append(i)
print(result)
