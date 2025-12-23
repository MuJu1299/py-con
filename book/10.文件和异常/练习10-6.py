def sum_and():
    while True:
        num1=input('请输入第一个数： ')
        num2=input('请输入第二个数： ')
        try:
            sum=int(num1)+int(num2)
        except ValueError:
            print("请确保你输入的是两个数而不是别的")
        else:
            print(f'你的计算结果为{sum}')
            break

# sum_and()

from pathlib import Path

contents=''
try:
    contents+=Path('book/10.文件和异常/text/cats.txt').read_text()
except FileNotFoundError:
    print("未找到cats的文件夹")
try:
    contents+='\n'+Path('book/10.文件和异常/text/dogs.txt').read_text()
except FileNotFoundError:
    print("未找到dogs的文件夹")
print(contents)

line="Row,row,row your boat,rowbt!"
print(line.count('row'))
print(line.count('row '))
print(line.lower().count('row'))
