from pathlib import Path
import json
path=Path('book/10.文件和异常/text/sum.json')
if path.exists():
    
    content2=path.read_text(encoding='utf-8')
    sum2=json.loads(content2)
    question=input(f"请问你的名字是{sum2["name"]}吗？如果是请回答'yes',不是请回答'no'。")
    if question=='yes':
        print(f"你的名字是：{sum2['name']}")
        print(f"你的年龄是：{sum2['age']}")
        print(f"你最喜欢的数是：{sum2['favorate_sum']}")
    else:
        favorate_sum1=input('请输入你最喜欢的数： ')
        name=input('请输入你的名字： ')
        age=input('请输入你的年龄： ')
        news={"favorate_sum":favorate_sum1,"name":name,"age":age}
        content1=json.dumps(news)
        path.write_text(content1)
        print('数据已保存！')
        
        print(f"你的名字是：{sum2['name']}")
        print(f"你的年龄是：{sum2['age']}")
        print(f"你最喜欢的数是：{sum2['favorate_sum']}")

else:
    favorate_sum1=input('请输入你最喜欢的数： ')
    name=input('请输入你的名字： ')
    age=input('请输入你的年龄： ')
    news={"favorate_sum":favorate_sum1,"name":name,"age":age}
    content1=json.dumps(news)
    path.write_text(content1)
    print('数据已保存！')




