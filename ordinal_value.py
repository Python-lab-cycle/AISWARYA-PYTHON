list1=['python','java','linux']
print("The original list:\n",str(list1))
res=[ord(ele) for sub in list1 for ele in sub]
print("The Ascii list is :\n",str(res))
