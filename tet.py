# 第一个简单的爬取图片的程序
import urllib.request # python自带的爬操作url的库
import re # 正则表达式
 
print('开始')
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
  # [^\s]*? 表示最小匹配， 两个括号表示列表中有两个元组
  # imageList = re.findall(r'(https:[^\s]*?(png))"', page)
  imageList = re.findall(r'(http:[^\s]*?(jpg|png|gif))"', page)
  x = 0
  # 循环列表
  for imageUrl in imageList:
    try:
      print('content: %s' % imageUrl[0])
      # 这个image文件夹需要先创建好才能看到结果
      image_save_path = './image/%d.png' % x
      # 下载图片并且保存到指定文件夹中
      urllib.request.urlretrieve(imageUrl[0], image_save_path)
      x = x + 1
    except:
      continue
  pass
if __name__ == '__main__':
  # 指定要爬取的网站
  url = "http://www.cssmoban.com"
  # 得到该网站的源代码
  page = getHtmlCode(url)
  # 爬取该网站的图片并且保存
  getImage(page)
  # print(page)

