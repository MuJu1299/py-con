from pathlib import Path

all_name=''
while True:
    in_name=input('请输入你的名字(输入stop停止): ')
    
    if in_name!="stop":
        all_name+=str(in_name.lstrip())+'\n'
    else:
        break
    Path('book/10.文件和异常/text/python_name.txt').write_text(all_name)