from random import choice

#1. choose dishes

def chooseDishes(days):
    while len(myMenu)< int(days):
        
        chosenDish = choice(foodWeLike)
        if chosenDish not in myMenu:
            myMenu.append(chosenDish)
    print("done! here's your menu")
    print()
    for dish in myMenu:
        print(myMenu.index(dish) + 1, dish)
    print("out of all, my fav dish is..." + choice(myMenu))
    print()
        

#2. build shopping list
def buildShoppingList():
    myShoppinglist=[]
    if "pizza" in myMenu:
        myShoppinglist.append(Pizza)
    if "beef burgers" in myMenu:
        myShoppinglist.append(beefburgers)
    if "pork stir fry" in myMenu:
        myShoppinglist.append(porkstirfry)
    if "chilli chicken" in myMenu:
        myShoppinglist.append(chillichicken)
    if "baby corn" in myMenu:
        myShoppinglist.append(babycorn)
    for dish in myShoppinglist:
        for ingridient in dish:
            print(ingridient)
        print()
    print("Alice")


#-------LISTS------

foodWeLike = ["pizza","beef burgers","pork stir fry","chilli chicken","baby corn"]

Pizza=["pizza base", "tomato sauce", "cheese","pepperconi","chillis"]
beefburgers=["beef patty","burger rolls","lettuce","tomatoes","relish"]
porkstirfry=["pork","peppers","onion","hoi sin sauce","noodles"]
chillichicken=["1/4 cup olive oil more  needed","3 medium lemons, washed, ends trimmed"]
babycorn=["corn","soup"]
myMenu = []


# how many days to plan ?
print("hello,i am munch! i'll help you plan your dinner now..")

answer= input("how many days would you like me to plan: " )
print("ok,i am going to plan " + answer + " dinner from your favourite meal")
print()


# choose dishes


chooseDishes(answer)


# building shopping list


answer= input("would you like a shopping list for this menu? ")

if answer=='y':
    buildShoppingList()
else:
    print("end program")
