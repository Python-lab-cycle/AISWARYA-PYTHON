color1 = input("Enter a set of colors(Space separated): ")
color2 = input("Enter a set of colors(Space separated) :")
c1 = set(color1.split())
c2 = set(color2.split())
print("The difference between", c1, "and", c2, "is", c1.difference(c2))

