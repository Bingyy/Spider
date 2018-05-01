

```python
# 浏览器不是必须的
from urllib.request import urlopen
html = urlopen('http://pythonscraping.com/pages/page1.html')
```


```python
print(html.read())
```

    b'<html>\n<head>\n<title>A Useful Page</title>\n</head>\n<body>\n<h1>An Interesting Title</h1>\n<div>\nLorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n</div>\n</body>\n</html>\n'


urllib or urllib2?
在Python3.x下，urllib被分成几个子模块：

- urllib.request: for opening and reading URLs
- urllib.parse: for parsing URLs
- urllib.error: containing the exceptions raised by urllib.request
- urllib.robotparser for parsing robots.txt files


### BeautifulSoup简介

用于格式化、组织杂乱的HTML文档，用Python对象来表示XML结构。

`pip3 install beautifulsoup4`

bs4最常用的用法如下，用于解析HTML，将其表达为BS对象。然后就可以对对象进行操作了。


```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://pythonscraping.com/pages/page1.html')
```


```python
bsObj = BeautifulSoup(html.read())
```

    /Users/rick/anaconda3/lib/python3.6/site-packages/bs4/__init__.py:181: UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("lxml"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.
    
    The code that caused this warning is on line 193 of the file /Users/rick/anaconda3/lib/python3.6/runpy.py. To get rid of this warning, change code that looks like this:
    
     BeautifulSoup(YOUR_MARKUP})
    
    to this:
    
     BeautifulSoup(YOUR_MARKUP, "lxml")
    
      markup_type=markup_type))



```python
print(bsObj)
```

    <html>
    <head>
    <title>A Useful Page</title>
    </head>
    <body>
    <h1>An Interesting Title</h1>
    <div>
    Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
    </div>
    </body>
    </html>
    



```python
print(bsObj.h1) # 可以拿到单个标签内容
```

    <h1>An Interesting Title</h1>



```python
print(bsObj.body.h1)
```

    <h1>An Interesting Title</h1>



```python
print(bsObj.html.h1)
```

    <h1>An Interesting Title</h1>


### 可靠性

这一段提到的场景可以说是相当扎心了的，你写好爬虫，然后让它自己在那跑，但是一旦你不再盯着了，程序可能就崩溃了，你期待着数据都下好了，实际上并没有。怪谁？网站的开发者吗？不不不，还是怪你自己，没有预料到这个一定会发生的情形。


```python
html = urlopen('http://pythonscraping.com/pages/page1.html')
```

上面这句就有两个可能性出现问题：

- 页面不存在: 404
- 服务器不存在: 500


```python
try:
    html = urlopen('http://pythonscraping.com/pages/page2.html')
    if html is None:
        print('URL is not found')
    else:
        pass
except HTTPError as e:
    print(e)
else:
    pass # 如果在except这里已经return或者break了，else不执行
```


```python
BeautifulSoup(html.read())
```

    /Users/rick/anaconda3/lib/python3.6/site-packages/bs4/__init__.py:181: UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("lxml"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.
    
    The code that caused this warning is on line 193 of the file /Users/rick/anaconda3/lib/python3.6/runpy.py. To get rid of this warning, change code that looks like this:
    
     BeautifulSoup(YOUR_MARKUP})
    
    to this:
    
     BeautifulSoup(YOUR_MARKUP, "lxml")
    
      markup_type=markup_type))





    <html>
    <head>
    <title>A Useful Page</title>
    </head>
    <body>
    <h1>An Interesting Title</h1>
    <div class="body" id="fakeLatin">
    Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
    </div>
    </body>
    </html>




```python
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

# 这些都应该是自己重要的代码库片段，可重用
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title
```


```python
if title is None:
    print('Title could not be found')
else:
    print(title)
```

    <h1>An Interesting Title</h1>



```python
title = getTitle('http://pythonscraping.com/pages/page1.html')
```

    /Users/rick/anaconda3/lib/python3.6/site-packages/bs4/__init__.py:181: UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("lxml"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.
    
    The code that caused this warning is on line 193 of the file /Users/rick/anaconda3/lib/python3.6/runpy.py. To get rid of this warning, change code that looks like this:
    
     BeautifulSoup(YOUR_MARKUP})
    
    to this:
    
     BeautifulSoup(YOUR_MARKUP, "lxml")
    
      markup_type=markup_type))

