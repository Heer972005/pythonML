n=int(input("How many students marks you want to enter? "))
mrksList=[]

for i in range(1,n+1):
    mrk=float(input(f"Enter marks for student {i} (out of 100): "))
    while mrk<0 or mrk>100:
        print("Invalid marks entered. Please enter marks between 0 and 100.")
        mrk=float(input(f"re-enter the marks for student {i} (out of 100): "))
    mrksList.append(mrk)
total=0
highest=mrksList[0]
lowest=mrksList[0]
pssed=0

for m in mrksList:
    total+=m
    if m>highest:
        highest=m
    if m<lowest:
        lowest=m
    if m>=40:
        pssed+=1
avg=total/n
print()
print("="*40)
print("Class Marks Analysis")
print("="*40)
print(f"Number of students          : {n}")
print(f"Total marks                 : {total}")
print(f"Average marks               : {avg:.2f}")
print(f"Highest marks               : {highest}")
print(f"Lowest marks                : {lowest}")
print(f"Number of students passed   : {pssed}/{n}")
print(f"Number of students failed   : {n-pssed}/{n}")
print("="*40)