align_0={'color':'green','points':5}
print(align_0['color'])
print(align_0['points'])

# 添加属性
align_0['x_position']=0
align_0['y_position']=25
print(align_0)

# 修改属性
align_0['color']='yellow'
print(align_0)

# 增加速度并跟踪
align_0['speed']='medium'
print(align_0)
# 向右移动并根据速度决定移动距离
print("原始x位置为："+str(align_0['x_position']))
if align_0['speed']=='slow':
    x_increment=1
elif align_0['speed']=='medium':
    x_increment=2
elif align_0['speed']=='fast':
    x_increment=3
# 新位置等于旧位置加上增量
align_0['x_position']=align_0['x_position']+x_increment
print("新x位置为："+str(align_0['x_position']))

# 删除键值对
del align_0['points']

# 用get()方法访问值
point_value=align_0.get('points','没有找到points属性。')
print(point_value)

# test1
person_0={'first_bame':'abc','last_name':'xyz','age':30,'city':'jiangxi'}
for key,value in person_0.items():
    print("\nKey:"+key)
    print("Value:"+str(value))

# test2
favorite_numbers={'alice':3,'bob':7,'carol':9}
for name,number in favorite_numbers.items():
    print(name.title()+"'s favorite number is "+str(number)+".")

# test3
reversed_index={}
reversed_index["append"]="在列表末尾添加元素的方法。"
reversed_index["del"]="删除列表中指定位置的元素的方法。"
reversed_index["insert"]="在列表的指定位置添加元素的方法。"
reversed_index["pop"]="移除列表中的一个元素（默认最后一个），并且返回该元素的值的方法。"
for word,definition in reversed_index.items():
    print(word+": "+definition)

# 遍历字典
for k,v in align_0.items():
    print(k+":"+str(v))

# 遍历所有的键
for name in favorite_numbers.keys():
    print(name.title())

# 遍历所有的值
for number in favorite_numbers.values():
    print(str(number))

# 使用set()函数避免重复值
for number in set(favorite_numbers.values()):
    print(str(number))

# test4
for name,number in favorite_numbers.items():
    print(name.title()+"'s favorite number is "+str(number)+".")
# test5
rivers={'China':'Yangtze River','Egypt':'Nile','Brazil':'Amazon River'}
for country,river in rivers.items():
    print("The "+river+" runs through "+country+".")
for country in rivers.keys():
    print(country)
for river in set(rivers.values()):
    print(river)

# test6
names=['alice','bob','carol','david','eva']
people={'alice':'apple','bob':'banana','carol':'cherry','david':'date','eva':'elderberry'}
for name in names:
    if name in people.keys():
        print("Hi "+name.title()+",I see your favorite fruit is "+people[name]+".")
    else:
        print("Hi "+name.title()+",please take our poll!")

# test7
people_0={'first_name':'john','last_name':'done','age':28,'city':'new york'}
people_1={'first_name':'Bob','last_name':'done','age':22,'city':'los angeles'}
people_all=[people_0,people_1]
for person in people_all:
    for key,value in person.items():
        print(key+":"+str(value))
    print("\n")

# test8
pet_0={'type':'dog','owner':'alice'}
pet_1={'type':'cat','owner':'bob'}
pet_2={'type':'fish','owner':'carol'}
pets=[pet_0,pet_1,pet_2]
for pet in pets:
    for key,value in pet.items():
        print(key+":"+str(value))
    print("\n")

# test9
favorite_places={'alice':['paris','london'],'bob':['new york'],'carol':['tokyo','seoul','bangkok']}
for name,places in favorite_places.items():
    print(name.title()+"'s favorite places are:")
    for place in places:
        print("- "+place.title())
# test10
favorite_numbers_0={'alice':[3,7,9],'bob':[2,4],'carol':[5,11,13]}
for name,numbers in favorite_numbers_0.items():
    print(name.title()+"'s favorite numbers are:")
    for number in numbers:
        print("- "+str(number))

# test11
cities={'new york':{'country':'usa','population':8419600,'fact':'the largest city in the united states.'},
        'tokyo':{'country':'japan','population':13929286,'fact':'the capital of japan.'},
        'paris':{'country':'france','population':2140526,'fact':'the city of lights.'}}
for city,info in cities.items():
    print("\nCity: "+city.title())
    country=info['country']
    population=info['population']
    fact=info['fact']
    print("\tCountry: "+country.title())
    print("\tPopulation: "+str(population))
    print("\tFact: "+fact)

# test12
