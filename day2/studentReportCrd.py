nme=input("Enter student name: ")
sub1=float(input("Enter marks for OS(out of 100): "))
sub2=float(input("Enter marks for DBMS(out of 100): "))
sub3=float(input("Enter marks for OOP(out of 100): "))
if((sub1>100 or sub1<0) or (sub2>100 or sub2<0) or (sub3>100 or sub3<0)):
    print("Invalid marks entered. Please enter marks between 0 and 100.")
else:
    ttl=sub1+sub2+sub3
    avg=ttl/3
    per=(ttl/300)*100

if avg>=90:
    grade="A+"
elif avg>=75:
    grade="A"
elif avg>=60:
    grade="B"
elif avg>=40:
    grade="C"
else:
    grade="F"

passed=avg>=40

print()
print("="*40)
print(f"Report Card- {nme.upper()}")
print("="*40)
print(f"OS: {sub1}")
print(f"DBMS: {sub2}")
print(f"OOP: {sub3}")
print("="*40)
print(f"Total Marks     : {ttl}/300")
print(f"Average Marks   : {avg:.1f}")
print(f"Percentage      : {per:.2f}%")
print(f"Grade           : {grade}")
print(f"Result          : {'PASS' if passed else 'FAIL'}")
print("="*40)
