def greet_user(username):
    '''打印Hello'''
    print(f"Hello,{username.title()}!")
greet_user("bob")

# text
def display_message():
    '''本章主旨'''
    print('学习函数')
display_message()

# text 
def favorite_message(title):
    '''喜欢的书'''
    print(f'\nOne of my favorate books is {title}.')
favorite_message("Alice in Wonderland")

# text 
def describe_pet(pet_name,animal_type='bbb'):
    '''描述宠物'''
    print(f"this pet name is {pet_name},it a {animal_type}.")
describe_pet("sfssa",animal_type="cat")


# text
def make_shirt(size,word):
    '''T恤'''
    print(f'\nThe size of T-shirt is {size},and the words on it are {word}.')
make_shirt(word="good",size="30")
# make_shirt()
# make_shirt("M")
make_shirt(word="iii",size="qqqq")

# text
def city_country(city,country):
    '''城市描述'''
    message=city+country
    return message
print(city_country("BeiJing",",China"))

# text
def mahe_album(singer='',collection='',songs=None):
    '''描述音乐专辑的字典'''
    music_message={"siger_name":singer,"singer_collection":collection}
    if songs:
        music_message["songs"]=songs
    return music_message
print(mahe_album("caixukun","jinitaimei"))

# text
# while True:
#     print("\nInputing 'q' can quit!")
#     singer=input("Please input singer: ")
#     if singer=="q":
#         break
#     print("\nInputing 'q' can quit!")
#     collection=input('Please input collection: ')
#     if singer=="q":
#         break
#     print(mahe_album(singer,collection))

# text
text1_list=['111','222','333','444','555']
sent_messages=[]
def show_messages(messages):
    '''打印每条消息'''
    for message in messages:
        print(message)
show_messages(text1_list[:])

def sent_message(list1,sent1):
    '''打印两个列表'''
    while list1:
        current_message=list1.pop()
        sent1.append(current_message)
    print(list1)
    print(sent1)
sent_message(text1_list[:],sent_messages)
print(text1_list)

# text
def sandwich(*foods):
    '''收集食材'''
    print('You added food: ')
    for food in foods:
        print(f'{food}')
sandwich('111','222','333')

# text
def build_profile(first_name,last_name,**discrabe):
    '''用户简介'''
    discrabe['first_name']=first_name
    discrabe['last_name']=last_name
    return discrabe
print(build_profile('Li',"Shun",habit='play game',height=170))