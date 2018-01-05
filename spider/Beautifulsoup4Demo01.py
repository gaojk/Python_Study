# Author:Jing Lv
# 爬取博客内容

from bs4 import BeautifulSoup
import requests

# 请求首页后获取整个html页面
r = requests.get("https://www.cnblogs.com/nbkhic/")
blog_content = r.content
# print(blog_content) # 获取页面html的所有内容

# 用html.parser解析html
soup = BeautifulSoup(blog_content, "html.parser")
# 获取所有的class属性为dayTitle，返回Tag类
times = soup.find_all(class_="dayTitle")
# for time in times:
#     print(time.a.string)  # 获取a标签的文本
# 获取博客的标题
titles = soup.find_all(class_="postTitle")
# for title in titles:
#     print(title.a.string)
# 获取博客的内容摘要
descs = soup.find_all(class_="postCon")
# for desc in descs:
#     # tag的contents属性可以将tag的子节点以列表的方式输出
#     c = desc.div.contents[0]  # 取第一个
#     print(c)

for time, title, desc in zip(times, titles, descs):
    print(time.a.string)
    print(title.a.string)
    print(desc.div.contents[0])
    print('--------------------------------------------------------------------------')
