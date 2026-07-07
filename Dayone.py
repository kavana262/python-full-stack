#Following brocode one shot
#Topics covered in Dayone
# 1.variables
# 2.Type casting and Type conversion
# 3.Input functions
# 4.mathematics
# 5.Conditional statementa
# 6.Logical operators


#my first program
print("i am kavana")
print("this is my first day of learning")


#variables=container for a value(string,integer,float,boolean)


#String
edu = "B.tech"
name="kavana"  
print("name")
print(name)
#this is formatted string 
print(f"my edu is {edu} and my name is {name}")

#Integer
age=30
no_of_stu=5
print("i am " , age ,"years old")
print(f"my age is {age}.my students are {no_of_stu}")

#float
price=5.8
cgpa=9.9
distance=15.9
print("my cgpa is" , cgpa)


#Boolean=either true or false
is_student=True
r_u_gone_crack_gsoc=True
R_u_gone_fail_in_life=False
if r_u_gone_crack_gsoc:
    print("u r going to do it.Go Girl")
else:
    print("try harder ")

#TypeCasting=the process of converting a variable from one data type to another(manual way) 
name='kavana'
age=33
gpa=9.8
is_success=True
print(type(name))   #tell the type of variable
print(type(age))
print(type(gpa))
print(type(is_success))

#eg
gpa=int(gpa)
print(gpa)

age=bool(age)
print(age)

age=str(age)
print(age)

#Type conversion=Python interpreter do conversion itself.
no1=19
no2=13.55
no3=no1+no2
print(no3)
print(type(no3))


#input()=Taking input from the users
Age=int(input("enter your age:"))
print(f"Your age is {Age}")
Name=input("What is your name?:")
print(f"Your name is {Name} and your age is {Age}")


#Excercise 1=Rectangle Area calculation
length=float(input("Enter Rectangle length:"))
breadth=float(input("Enter Rectangle breadth:"))
Area=length*breadth
print(f"Area of Rectangle is {Area}")


#Excercise 2=Shopping cart program

Item=input("What items would you like to buy?: ")
Price=float(input("what is the price?:"))
Quantity=int(input("How many would you like?:"))
Total=Price * Quantity
print(f"Your item is {Item} and each one of it cost {Price} and the quantity you selected is {Quantity} and your total price is {Total}")



#Excercise 3=Madlibs game
# word game where you create a story by filling in blanks with random words
adjective1=input("Enter an adjective(description):")
noun1=input("Enter a noun(person,place,thing):")
adjective2=input("Enter an adjective(description):")
verb1=input("Enter an verb ending with 'ing' :")
adjective3=input("Enter an adjective(description):")

print(f"Today i went to {adjective1} park.")
print(f"In my farewell i saw {noun1}.")
print(f"{noun1} was {adjective2} and {verb1}")
print(f"I was {adjective3}.")



#Mathematics

x=3.78
x=round(x) # function for rounding 
print(x)

y=4
y=abs(y)
print(y)    # function for absolute value
y=pow(4,3)
print(y)
max(x,y)
print(max)


#Conditional statements 
#1.if=do some code only if statement is true

age=int(input("Enter your age:"))
if age>=18:
    print("Your eligible to vote!")


#2.if else
age=int(input("Enter your age:"))
if age>=18:
    print("Your eligible to vote!")
else:
    print("Your not eligible!")


#3.elif =if more than one condititon
num=int(input("Enter a number:"))
if num%2==0:
    print("Entered number is even")
elif num%2!=0:
    print("Enteres number is odd")

else:
    print("Entered number is invalid")


#eg2
online=True
if online:
    print(" The User is online")
else:
    print("The user is offline ")



#python calculator
operator=input("Enter a operator(=,-,*,/) ")
num1=float(input("Enter a number1:"))
num2=float(input("Enter a number2:"))
if operator =="+" :
    Result=num1+num2
    print(f"{num1} + {num2} = {sum}")
elif operator== "-" :
    Result=num1-num2
    print(f"{num1} - {num2} = {sum}")
elif operator=="*":
    Result=num1*num2
    print(f"{num1} * {num2} = {sum}")
elif operator=="/":
    Result=num1/num2
    print(f"{num1} / {num2} = {sum}")
else:
    print("Enter a valid operator")


#logical opertors=Evaluate multiple conditions(or,and,not)
#or=Atleast one condition must be true
#and=Both the condition must be true 
#not=Inverts the condition(not false,not true )
#eg1
age=30
password=kavu
print=int(input("Enter your age:"))
print=input("Enter your password")
if (age==30 and password==kavu):
  print("You successfully  loged in")
else:
    print("You cannot login.")


#eg2
age=30
password=kavu
print=int(input("Enter your age:"))
print=input("Enter your password")
if (age==30 or password==kavu):
  print("You successfully  loged in")
else:
    print("You cannot login.")

#eg3
age=20
if not age<=18:
    print("Your  eligible")
else:
    print("Your not eligible ")


