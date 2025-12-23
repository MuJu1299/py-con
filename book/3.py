bicycles=['trek','cannondale','redline','specialized']
print(bicycles[0].title())
print(bicycles[-1].title())
print(bicycles[-2].title())
# 依次打印姓名
names=['bob','stave','eric','jan','lucy']
print(f"{names[0]},{names[1]},{names[2]},{names[-1]}".title())
# 问候语
print(f"Good night,{names[0]}!")

names.append('panmu')
print(names[-1])

names.insert(0,'Alicy')
print(names[0])

# pop（）中括号内默认为-1 
del names[0]
print(names)
new_names=names.pop()
print(names)

print(f'Do you want to eat food with me for this night?{names[0].title()}!')

dinna=['a','b','c']
dinna[2]="d"

dinna.insert(0,"0")
dinna.insert(1,"2")
dinna.append("3")
print(dinna)

print(dinna.pop(0))
print(dinna.pop(1))
print(dinna.pop())
print(dinna.pop())
print(dinna)
del dinna[0]
del dinna[0]
print(dinna)
# p39:test
trave=['beijing','shanghai','xian','janpanese','moon']
print(trave)
print(sorted(trave))
print(sorted(trave,reverse=True))
print(trave)
trave.sort()
print(trave)
trave.reverse()
print(trave)
print(trave)