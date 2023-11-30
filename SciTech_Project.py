## Write a python program that takes a list of student grade as input. Use a loop to 
## Calculate and display tha average grade. then, use if-elf statements to assign a letter grade(A,B,C,etc)
""" print('\t\t\t GRADE CALCULATOR')
Grades= int(input("how many names do you want to enter:"))
GradeList=[]

for r in range(0,Grades):
    b=int(input("enter grades: "))
    GradeList.append(b)
    d=sum(GradeList)/len(GradeList)
if ( 90<= d <100 ):
    letter_grade='A'
elif (80<= d < 90):
    letter_grade='B'
elif (70 <= d < 80):
    letter_grade='C'
elif (60 <= d < 70):
    letter_grade='D'
elif (50 <= d < 60):
    letter_grade='E'
else:
    letter_grade='F'

print(f"the grades are {GradeList}") 
print(f"the Average grade is {d}")
print(f"the Average_grade_Letter is {letter_grade}") """



## Write a program that takes a list of numbers as input. use a loop
# find and display the sum, average, maximum and minimum of the numbers.
""" print("\t\t\t  NUMBER ANALYSIS")
a= int(input("how many names do you want to enter:"))
c=[]

for r in range(0,a):
    b=int(input("enter grades: "))
    c.append(b)
    d=sum(c)
    e=sum(c)/len(c)
    f=max(c)
    g=min(c)
    
    
print(f"the numbers are {c}") 
print(f"the sum of the numbers is {d}")
print(f"the Average of the numbers is {e}")
print(f"the maximum of the number is {f}")
print(f"the minimum of the numbers is {g}") """


## Write a program that takes an array of numbers as input. Use
# a loop and if-elif statements to classify each numbers as even or odd.
# Display the counts of even and odd
""" print("\t\t\t  EVEN or ODD")
nums= int(input("how many names do you want to enter:"))
c=[]
o,e=0,0
odd=[]
even=[]
for r in range(0,nums):
    b=int(input("enter grades: "))
    c.append(b)
    
for a in c:
    if (a%2==0):
        even.append(a)
        e+=1 
    elif(a%2!=0):
        odd.append(a)
        o+=1
print(f"the numbers are {c}") 
print(f"the count of odd numbers is {o}") 
print(f"the count of even numbers is {e}") 
print(f"the odd numbers are {odd}") 
print(f"the even numbers are {even}") """


## 4
print("\t\t\t  MENU DRIVEN CALCULATOR")
while True:
    a=float(input("enter the 1st number: "))
    b=float(input("enter the 2nd number: "))

    Addition= a + b
    Subtraction= a - b
    Multiply= a * b
    Division= a / b
    
    print(f"the sum is {Addition}") 
    print(f"the subtraction is {Subtraction}") 
    print(f"the product is {Multiply}") 
    print(f"the division is {Division}") 

    Continue=input("Do you want to continue. (yes/no): ").lower()
    print(" ")

    if Continue != "yes":
        break

        




    

