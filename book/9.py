class Dog:
    '''一次模拟小狗的简单尝试'''
    def __init__(self,name,age):
        '''初始化属性name和age'''
        self.name = name
        self.age = age

    def sit(self):
        '''模拟小狗收到命令时坐下'''
        print(f'{self.name} is now sitting.')
    
    def roll_over(self):
        '''模拟小狗收到命令时打滚'''
        print(f'{self.name} rolled over!')


my_dog=Dog('Bob',6)
my_dog.sit()
my_dog.roll_over()

# text
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        '''self后的name表示为self（也就是Rstaurant）创建一个为name的属性，name属性本质是变量，等号后面的为他的赋值'''
        self.name=restaurant_name
        self.type=cuisine_type
        self.number_served=0

    def increment_number_served(self,increment_number):
        '''增加就餐人数'''
        self.number_served+=increment_number
    def set_number_served(self,number_served):
        '''设置就餐人数'''
        self.number_served=number_served
    def describe_restaurant(self):
        print(f"{self.name} has been in existence for ten years.")

    def open_resturant(self):
        print(f'{self.type} is currently in operation.')

restaurant=Restaurant("Miburg Castle",'Fast food')
print(restaurant.name+f'\n{restaurant.type}')
restaurant.describe_restaurant()
restaurant.open_resturant()
restaurant.set_number_served(9)
print(restaurant.number_served)
restaurant.increment_number_served(2)
print(restaurant.number_served)

# text
class User:
    def __init__(self):
        self.login_attempts=0

    def increment_login_attempts(self):
        '''增加一个登录'''
        self.login_attempts+=1

    def reset_login_attempts(self):
        '''重置登录'''
        self.login_attempts=0

use1=User()
while use1.login_attempts<=6:
    print(use1.login_attempts)
    use1.increment_login_attempts()

use1.reset_login_attempts()
print(use1.login_attempts)

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        '''继承父类的所有属性和方法supper()'''
        super().__init__(restaurant_name,cuisine_type)
        self.flavors=['qqq','ccc','ddd']

    def Ice_cream_flavor(self):
        '''打印冰淇淋口味'''
        print(self.flavors)
'''1和2相当于以属性区分的id必须要写'''
Icecream_flavor=IceCreamStand('10','2')
Icecream_flavor.Ice_cream_flavor()

# text
class Admin(User):
    def __init__(self):
        super().__init__()
        self.privileges_list=['can add post','can delete post','can ban user']
        self.privileges=self.Privileges()
    class Privileges:
        def show_privileges(self):
            '''显示管理员权限'''
            print('you can do everything!')
    

showP=Admin()
showP.privileges.show_privileges()

class Die:
    def __init__(self,sides=6):
        self.sides=sides

    def roll_die(self):
        import random
        print(random.randint(1,self.sides))

stru6=Die(6)
stru6.roll_die()

stru10=Die(10)
stru10.roll_die()

array=['1','2','3','4','5','6','7','8','9','0','q','w','e','r','t']
my_ticket=0
new_number=''
while new_number!="1234":
    new_number=''
    from random import sample
    first_up=sample(array,4)
    for first in first_up:
        new_number+=first
    my_ticket+=1

print(f"你的号码是{new_number}")
if new_number=='1234':
    print('你他妈中大奖了！')
else:
    print("谢谢惠顾~")
print(f"你总共抽了{my_ticket}次才中奖")










