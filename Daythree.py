#Revise DayOne and Daytwo topics
#Topics covered in this day
#1.lists,sets and tuples


#Collection=single variable used to store multiple values
#List=[] ordered( Items stays in the same sequence in which we added) and changeable. can have duplicates
#set={}  unordered and immutable,but add/remove ok. no duplicates
#Tuple=()  ordered and immutable.Can have duplicate and faster.

#list
#eg1
"""names=["kavana","hemavathi","karthik","zak"]
print(names)
names.append("Karthik") #Adding new elments to the list
print(names)
print(names[0]) #we can also use indexing 
print(names[1])
#print(names[6])  #if indexing number is not found it will throw list out of range error
print(names[0:2])
print(names[-3:-1]) #excluding -3
print(names[::2])

#we ca also iterate over for loop

names=["kavana","hemavathi","karthik","zak"]
for xy in names:
    print(xy)
#print(dir(names))

#print(help(names))  # give description

print(len(names)) # to find length 
print(len(names[0])) # to find length of each word . here indexing start from 1
print(len(names[1])) # to find length 
print(len(names[-1])) # to find length 
print(len(names[-4])) # to find length 
print("kavana" in names) # gives Boolean answer
print("milan" in names) # "in" opearot checks if the element is in the lists or not 


names[1]="milan"
print (names) # we can change the element
names.append("nethra") #adding a element at the last
names.remove('kavana')  #remove the element
names.insert(4,  "kavana")  # adding a element where ever we want
print(names)
names.sort()  #sort the list acc to alpha order
names.reverse # it is in the reverse order of whocih we added not alpha order
#names.clear()  #to delete all elemenst in list
print(names.index("kavana"))  # to find the index of an element
print(names.index("kavana"))  # if ele in not in the list it will throw error x not in list

print(names.count("hemavathi")) # to find how many of the elements are +nt 



#set(unordered,no indexing, no duplicate and changeable)
animals={"dog","cat","cow",'calf',"horse"}
print(animals) # unordered(the elements r not in order of insertion)
animals.add("rabbit") # to add elements
print(animals)
animals.remove("horse") # to remove el
print(animals)
print("cow" in animals) #"in" is used to check if the ele is +nt in set
animals.add("cow") #no duplicate if we add same elemnts to the set no changes are made
print(animals)


#Tuples
brands=("dell","nike","adidas","rolex")
print(len(brands)) #indexing of tuples start from 0

print(len(brands[1]))#Indexing of elements start from 1
print(brands.index("rolex"))
for names in brands:
    print(names)"""


#Shopping cart program
food=[]
prices=[]
total=0
while True:
    food=input("Enter a food to buy(Enter q to quit)")
    if food.lower()=="q":
        break
    else:
        price=float(input(F"Enter the price of a{food}: inr"))
        foods.append(food)
        prices.append(price)
print("------Your cart----")
for food in foods:
    print(food)