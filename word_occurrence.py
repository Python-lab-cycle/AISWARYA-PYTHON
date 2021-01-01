line = input("Enter a Line: ")
count = {}
sentance = line.split()
# print(sentance)
for word in sentance:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
for k, v in count.items():
    print(k, v)

