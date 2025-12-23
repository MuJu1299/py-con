# message=input("")
# print(f'\nYour name is {message}!')

# age=input("How old are you?")
# print(f'your age is {age}!')
# if int(age)>18:
#     print("your are adult!")
# else:
#     print("you are child!")

# text
# question=input('what you want to buy?')
# print(f'\nLet me see if I can find you {question}!')

# text 
# message=input("How many people are having a meal?")
# if int(message)>8:
#     print('Sorry there are no seats available here.')
# else:
#     print("you welcome!")

# text 
# number=input('num: ')
# if int(number)%10==0:
#     print('this number is a muitiple of ten!')
# else:
#     print('this number is not a multiple od ten!')

# prompt='\nTell me somethinng.'
# prompt +='\nEnter "quite to end the progrem: '

# message=""
# while message!="quite":
#     message=input(prompt)
#     if message != "quite":
#         print(message)

# active=True
# while active:
#     message=input(prompt)
#     if message=="quite":
#         active=False
#     else:
#         print(message)

# text:
# prompt="\nPlease select your burdening: "

# while True:
#     message=input(prompt)
#     if message=="quite":
#         break
#     else:
#         print(f'\n{message}')




# text:
# message=input("Please input your age: ")
# if int(message)<3:
#     print('free of charge!')
# elif int(message)<12:
#     print('ten dollar!')
# else:
#     print('fifteen dollar!')

sandwich_orders=['aaa','bbb','ccc','ddd',"aaa",'aaa']
# finished_sandwiches=[]
# while sandwich_orders:
#     current_sandwich=sandwich_orders.pop()
#     finished_sandwiches.append(current_sandwich)
#     print(f"I made your {current_sandwich} sandwich!")
# print(finished_sandwiches)

print("aaa is done")
while "aaa" in sandwich_orders:
    sandwich_orders.remove('aaa')
print(sandwich_orders)

    
