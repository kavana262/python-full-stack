#day 4 
#2D collection=collection of 1D lists,tuples & set
#Dictionaries=a collection of {key:value} pair and they  are ordered and changeable and no duplicates.
 fruits=["guava","pineapple","sitaphal","orange"]
vegetable=["onion","tomoto","zucchini","carro","beetroot"]
special_foods=["sandwich","cold coffee","pasta","icecream"]
minecombo=[fruits,vegetable,special_foods]
print(minecombo)

print(minecombo[0])  #this is row fruits is row 1 now 
print(minecombo[1])  #this is row fruits is row 2 now 
print(minecombo[2])  #this is row fruits is row 3 now 

print(minecombo[1][0])  # this is 2D
print(minecombo[0][0]) 
print(minecombo[1][2]) 
print(minecombo[2][0]) 
print(minecombo[1][4]) 

#we can store inside one varible also
food_items=[["guava","pineapple","sitaphal","orange"],["onion","tomoto","zucchini","carro","beetroot"],["sandwich","cold coffee","pasta","icecream"]]  #list 2D
for items in food_items:  #we use two for loops because we stores list inside a list.If we want to access single elements we have to put two for loops 
    for i in items:
      print(i)

food_items=[("guava","pineapple","sitaphal","orange"),("onion","tomoto","zucchini","carro","beetroot"),("sandwich","cold coffee","pasta","icecream")]  #set 2D
food_items=[{"guava","pineapple","sitaphal","orange"},{"onion","tomoto","zucchini","carro","beetroot"},{"sandwich","cold coffee","pasta","icecream"}]  #Tuple 2D 

# Dial pad
num_pad=((1,2,3),(4,5,6),(7,8,9),("*",0,"#"))
for numbers in num_pad:
  for num in numbers:
    print(num,end=" ")
  print()
  


#Python quiz game=i will do it later 
libaray={"atomichabits":"A","dsa":"striver","c":"harry"}
  


