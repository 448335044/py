from bs4 import BeautifulSoup # BeautifulSoup是python处理HTML/XML的函数库，是Python内置的网页分析工具
import urllib.request # python自带的爬操作url的库
 
 
# 该方法传入url,返回url的html的源代码
def getHtmlCode(url):
  # 以下几行注释的代码在本程序中有加没加效果一样,但是为了隐藏自己避免被反爬虫可以假如这个伪装的头部请求
  headers = {
    'User-Agent': 'Mozilla/5.0(Linux; Android 6.0; Nexus 5 Build/MRA58N) \
    AppleWebKit/537.36(KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'
  }
  # 将headers头部添加到url，模拟浏览器访问
  url = urllib.request.Request(url, headers=headers)
 
  # 将url页面的源代码保存成字符串
  page = urllib.request.urlopen(url).read()
  # 字符串转码
  page = page.decode('UTF-8')
  return page
 
 
# 该方法传入html的源代码，通过截取其中的img标签，将图片保存到本机
def getImage(page):
  # 按照html格式解析页面
  soup = BeautifulSoup(page, 'html.parser')
  # 格式化输出DOM树的内容
  print(soup.prettify())
  # 返回所有包含img标签的列表，因为在Html文件中图片的插入呈现形式是<img src="..." alt=".." />
  imgList = soup.find_all('img')
  x = 0
  # 循环找到的图片列表，注意，这里手动设置从第2张图片开始，是因为我debug看到了第一张图片不是我想要的图片
  for imgUrl in imgList[1:]:
    # print(imgUrl)
    # print('正在下载： %s ' % imgUrl.get('data-original'))
    # 得到scr的内容，这里返回的就是Url字符串链接，如'https://img2020.cnblogs.com/blog/1703588/202007/1703588-20200716203143042-623499171.png'
    image_url = imgUrl.get('data-original-src')
    print(111)
    print(image_url)
    # print(image_url)
    # 这个image文件夹需要先创建好才能看到结果
    image_save_path = './image2/%d.png' % x
    # 加判断,因为没有image_url就报错了,中断了程序执行 (或者try...except捕获异常也可以)
    if image_url != None:
      # 下载图片并且保存到指定文件夹中
      urllib.request.urlopen(image_url, image_save_path)
      x = x + 1
if __name__ == '__main__':
  # 指定要爬取的网站
  url = 'https://www.jianshu.com/p/c894ea00dfec'
  # 得到该网站的源代码
  page = getHtmlCode(url)
  # 爬取该网站的图片并且保存
  getImage(page)