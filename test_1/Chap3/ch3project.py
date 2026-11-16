t1=input("please enter first topping:")
t2=input("please enter second toppping:")
t3=input("Please enter third topping:")

cost=0

if t1 == "yogurt":
    cost += 1.00
elif t1 == "tomato":
    cost +=0.50
elif t1=="lettuce":
    cost += 0.30
elif t1 == "skittles":
    cost+= 0.75
else:
    cost+= 0.00 

if t2 == "yogurt":
    cost += 1.00
elif t2 == "tomato":
    cost +=0.50
elif t2=="lettuce":
    cost += 0.30
elif t2 == "skittles":
    cost+= 0.75
else:
    cost+= 0.00 

if t3 == "yogurt":
    cost += 1.00
elif t3 == "tomato":
    cost +=0.50
elif t3=="lettuce":
    cost += 0.30
elif t3 == "skittles":
    cost+= 0.75
else:
    cost+= 0.00

print("Your toppings cost $"+ format(cost, ".2f"))

if cost >= 1.50:
    discount = cost * 0.10
else:
    discount =0

print("You saved $"+ format(discount, ".2f"))

total = cost - discount

print("Your total is $"+ format(total, ".2f"))