startyear = int(input("Enter start year: "))
endyear = int(input("Enter last year: "))
print("List of leap years:")
for year in range(startyear, endyear):
    if ((year%4==0) and (year%100!=0) or (year%400==0)):
        print(year)