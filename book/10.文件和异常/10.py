from pathlib import Path

path=Path('book/10.文件和异常/text/python_story.txt')
learning_python=path.read_text()
print(learning_python)

all_news=''
for line in learning_python.splitlines():
    all_news+=line.lstrip()
print(all_news)

print(learning_python.replace('python','c'))