#Note:Revise Dayone's topic and move on 

#Conditional expression=one line shortcut fot if-else ststement(ternery operator)
# x if condition else y
#eg1
num=5
print("Positive"  if num>0 else "Negative")

#eg2
age=int(input("Enter your age:"))
print("Your eligible to vote" if age>=18 else "Your not elgible to vote")

#eg3
age=19
life="die" if age>=50 else "live long"
print(life)

#String methods 

name=input("Enter your name:")
print("The length of your name is :",len(name))  #len() gives length of a string include spaces
print("The first occurence of the alpahbet entered is:",name.find("a"))  # .find return the first occurenc from the first.And strings index always start from zero
print("The reverse occurence of the alpahbet entered is:",name.rfind("Z"))  # .find return the first occurence  from the last.And strings index always start from zero and if there is no matching it will return -1
print("The capitalize form of your name is :",name.capitalize()) # we can captailize the  strings first alphabet by .capitalize fun
print("The capitalize form of your name is :",name.upper()) # we can captailize the whole strings  by .upper fun
print("The lower form of your name is :",name.lower()) # we can lower case the whole strings  by .lower fun
print("your string contains only digits :",name.isdigit())  # we can find if our string is contain only digits.It returns boolean(true only if string contains only digit else false).
print("your string contains only alphabets :",name.isalpha())  # we can find if our string is contain only alphabets. It returns boolean(true only if string contains only alphabets(excluding space also) else false).
letter=input('Enter a alphabet:')
print("The number of times",letter,"is occured in",name ,  "is:", name.count(letter))     # the alphabet or digit occured how many times in  string 
replacing_letter=input("Enter a letter to replace: ")
print("Replace ",letter,"with",replacing_letter ,":", name.replace(letter,replacing_letter)) # replace a aphablet in a srting with another alphabet


#Excercise1
#Validate use input 
#1.username is no more than 12 characters
#2.username must not contains spaces
#3.username must not contian digits

username=input("Enter your full name(without any spaces ,any digits and name must not exceed 12 characters):")

if len(username)<=12 and username.isalpha() == True and username.isdigit()==False:
    print("Entered name is valid")
else:
    print("Entered name is invalid")


#Indexing=Accessing elements of a sequence using[](indexing operator)
#[start:end:step].Always start from 0
#eg1:
number="1234567890"  # indexing only work with string, tuples,list not with numbers 
print(number[0:7])  # Give only number from 0 to 7
print(number[0:7:2])  # Give only number from 0 to 7 and skip 2's position 
print(number[:8])    # It will automaticlaly take from index 0 if we dont enter anything
print(number[0:])     # It will automaticlaly take from index 0 if we dont enter anything
print(number[0:9:3])
print(number[-4:])     #Negative indexing
print(number[-4:-1])  # stops befor -1(befor 0) this is slicing     
print(number[0:4])
print(number[-2])
print(number[-9:-1:2])
print(number[-4])


#format specifiers={value:flags} format a value based on what flags are inserted
#  .(number)f= round to that many decimal places(fixed point)
#  :(number)=allocate that many spaces
#  :03 = allocate and zero pad that many spaces 
#  :<=left justify
#  :>=right justify
#  :^=center allign
#  :+=use a plus sign to indicate positive value
#  := =place sign to leftmost position
#  :  = insert a space befor positive numbers 
#  :, = comma separator
#
# eg1

price1=3.141456
price2=-987.65
price3=12.34

print(f"price 1 is {price1:.2f}")
print(f"price 1 is {price1:.3f}")
print(f"price 2 is {price2:.2f}")
print(f"price 1 is {price3:.2f}")
#format specifiers={value:flags} format a value based on what flags are inserted
#  .(number)f= round to that many decimal places(fixed point)
#  :(number)=allocate that many spaces
#  :03 = allocate and zero pad that many spaces 
#  :<=left justify
#  :>=right justify
#  :^=center allign
#  :+=use a plus sign to indicate positive value
#  := =place sign to leftmost position
#  :  = insert a space befor positive numbers 
#  :, = comma separator
#
# eg1

price1=3.141456
price2=-987.65
price3=12.34

print(f"price 1 is {price1:.2f}")
print(f"price 1 is {price1:.3f}")
print(f"price 2 is {price2:.2f}")
print(f"price 3 is {price3:.2f}")
print(f"price 1 is {price3:<4}")
print(f"price 1 is {price3:>3}")
print(f"price 1 is {price3:^10}") 

#while loop= execute some code while some condition remains true 
name=input("Enter your name:")
while name=="":
    print("You did not enter your name")
    name=input("Enter your name:")
print(f"hello {name}")

#eg2
crct_password="kavu123"
password=input("Enter your password:")
while password!=crct_password:
    print("Your password in wrong")
    password=input("Enter your password:")
print("You successfully loged in to your account")


#eg3
age=int(input("Enter your age:"))
while age<0:
    print("Age cannot be negative")
    age=int(input('Enter your age:'))
print(f"your {age} years old" )

#eg4
food=input("Enter a food you like(Enter q to quit):")
while not food=="q":
    print(f"You like {food}!")
    food=input("Enter a food you like(Enter q to quit):")
print("Thankyou so much! Bye")


#eg5
num=int(input("Enter a number:"))
i=0
while i<=num:
    print(i)
    i=i+1


#for loops=execute a block of code a fixed number of time.
# you can iterate over a range,string,sequence etc.
#range(start(included),stop(not included),step)
#eg1
for r in range(1,20):
    print(r,end="")  # give all number in same line
    r=r+1

#eg2

name=input("Enter your nam:")
for letter in name:
    print(letter)


#eg3

house=["keys",'books','pen','bike']
for elements in house:
    print(elements)

#eg4
for countdown in reversed(range(1,11)):
    print(countdown)
    if countdown ==2:
        break

print("Happiest birthday my dear friend!")



#Nested loops= A loop within another loop(outer,inner)
#outer loop:
#     inner loop:

for x in range(4):
    
    for y in range (1 ,11):
        print(y,end="")
    print()

