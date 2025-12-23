magicians=['alice','david','carolina']
for magician in magicians:
    print(magician) 

    print("good!")

pizza_kinds=['hls','zz','zghb']
for pizza in pizza_kinds:
    print(f"I like {pizza} pizza.")
print("I raelly love pizza!")

pets=["dog",'cat','fish']
for pet in pets:
    print(f"A {pet} would make a great pet.")
print("Any of these animals would make a great pet!")
# range(开始数，结束数的后一位数，跨度)，表示生成规定顺序的数，list（）指转化为数组
numbers=list(range(1,10,2))
print(numbers)

squares=[]
for value in range(1,10,2):
    square=value**2
    squares.append(square)
print(squares)
print(sum(squares))
print(min(squares))
print(max(squares))

for num in range(1,21):
    print(num)

single_numbers=list(range(1,21,2))
for number in single_numbers:
    print(number)

threes=list(range(3,31,3))
for three in threes:
    print(three)

AAAs=[num3**3 for num3 in range(1,11)]
for AAA in AAAs:
    print(AAA)

print(f"The first three items in the list are:{AAAs[0:3]}.")
print(f"Three items from the middle of the list are:{AAAs[2:5]}.")
print(f"The last three items in the list are:{AAAs[-3:]}.")

friend_pizzas=pizza_kinds[:]
friend_pizzas.append("aaaa")
for favorate_pizza in pizza_kinds:
    print(f"my favorate pizzas are:{favorate_pizza.title()}")
for frient_favorate_pizza in friend_pizzas:
    print(f"my friend is favorate pizzas are:{frient_favorate_pizza.title()}")

print('Old means:')
foods=("milk",'banana','apple','rice','beef')
for food in foods:
    print(food)
# foods[1]='aaa' 错误，元组内为常量
print("\nNew means:")
foods=("milk",'banana','apple','222e','111')
for new_food in foods:
    print(new_food)