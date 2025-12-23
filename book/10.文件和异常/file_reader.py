from pathlib import Path

path=Path('book/10.文件和异常/text/digits.txt')
if path.exists():
    contents = path.read_text()
    lines=contents.splitlines()
    pi_string=''
    for line in lines:
        pi_string+=line.lstrip()
    print(f'{pi_string[:22]}')
    print(len(pi_string))
else:
    print(f"文件 {path} 不存在")



