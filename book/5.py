cars=['aaa','bbb','ccc','ddd','eee']
for car in cars:
    if car=='bbb':
        print(car.upper())
    else:
        print(car.title())

if 'bbb' in cars:
    print('right')
else:
    print("not")

banned_users=['111','222','333','444','555']
user="bob"
if user not in banned_users:
    print(f"{user.title()},you can post a resoonse if you wish.")
else:
    print(f"{user.title()},you can not post response because you are banned.")

# 5.1 text 
food="milk"
print("Is food =='milk'?I predict Ture")
print(food=="milk")
print("Is food =='banana'?I predict False")
print(food=="banana")


topic1="good morning"
topic2="good aftnoon"
print('Is topic1==topic2?I predict False.')
print(topic1==topic2)

topic1_1="Good morning"
print("Is topic1==topic1_1.lower()?I predict Ture.")
print(topic1==topic1_1.lower())

numbers=[10,20,30,40,50,60]
number1=10
number2=25
# Ture
print(number1<=number2)
# False
print(number2>=numbers[3])
# Ture
print(number1<=number2 or number2>=numbers[3])
# False
print(number1<=number2 and number2>=numbers[3])
# 经测定不在集合中,False
print(number2 in numbers)
# 经测试在集合中，Ture
print(number1 in numbers)

# 5.3外星人练习
# 选择绿色获得五分。
alien_color1='green'
if alien_color1=='green':
    print("玩家获得了五分！")
elif alien_color1=="yellow":
    print("玩家获得了十分！")
else:
    print("零分！")
# 选择红色零分。
alien_color2="red"
if alien_color2=='green':
    print("玩家获得了五分！")
elif alien_color2=="yellow":
    print("玩家获得了十分！")
else:
    print("零分！")
# 选择黄色满分十分。
alien_color3="yellow"
if alien_color3=='green':
    print("玩家获得了五分！")
elif alien_color3=="yellow":
    print("玩家获得了十分！")
else:
    print("零分！")

# 年龄区分
age=15
if age<2:
    print("这个人是婴儿。")
elif age<4:
    print("这个人是幼儿。")
elif age<13:
    print("这个人是儿童。")
elif age<18:
    print("这个人是少年.")
elif age<65:
    print('这个人是中年')
elif age>=65:
    print('这个人是老年。')
# 喜欢的食物
favorate_foods=['banana','apple','orange']
if 'banana' in favorate_foods:
    print("yes")
if 'apple' in favorate_foods:
    print("yes")
if 'orange' in favorate_foods:
    print("yes")
if '111' in favorate_foods:
    print("yes")
if '222' in favorate_foods:
    print("yes")

# 5.8test
users=['asmin','jaden','bob','alice','tom']
if 'asmin' in users:
    print("抓住了！")
else:
    print("你好普通人。")
if users ==[]:
    print("We need to find some users!")

current_users=['aaa','bbb','ccc','ddd','eee']
current_users_upper=current_users[:]
new_users=['ddd','eee','fff','ggg','hhh']
for new_user in new_users:
    if new_user in current_users and new_user in current_users_upper:
        print(f'{new_user}已被使用。')
    elif new_user not in current_users and new_user not in current_users_upper:
        print(f'{new_user}未被使用。')

number1_9=[1,2,3,4,5,6,7,8,9]
for num in number1_9:
    if num==1:
        print(f"{num}st")
    elif num==2:
        print(f"{num}nd")
    elif num==3:
        print(f"{num}rd")
    else:
        print(f"{num}th")