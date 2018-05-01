
### 进阶的爬虫知识积累：HTML解析

> 很简单，你只需要去掉不像David的部分。 -- 米开朗琪罗

虽然网络爬虫很多方面并不像雕塑，但是在提取有用信息方面却值得用同样的态度来对待。有很多种方式去掉我们不感兴趣的内容，直到拿到我们想要的数据为止。在**复杂的**HTML文档中，找寻我们需要的知识点是本章的主题。

但是，首先需要明确你需要的数据是什么，否则会陷入一个盲目的状态。

看下面这个写法：

`bsObj.findAll('table')[4].findAll('tr')[2].find('td').findAll('div')[1].find('a')`,这种写法会使得爬虫很虚弱，网页轻微变动，就能崩溃这种写法的爬虫。

面临目标数据藏得很深，或者组织很散漫的数据时，记住，不要马上开始挖掘，而是深呼吸，想好对策再下手。

### BS用法详解

- 通过属性查找tag
- 树形索引

CSS文件对于爬虫是有好处的，记得CSS中的`class`,`id`吗？


```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://pythonscraping.com/pages/warandpeace.html')
bsObj = BeautifulSoup(html)
```

    /Users/rick/anaconda3/lib/python3.6/site-packages/bs4/__init__.py:181: UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("lxml"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.
    
    The code that caused this warning is on line 193 of the file /Users/rick/anaconda3/lib/python3.6/runpy.py. To get rid of this warning, change code that looks like this:
    
     BeautifulSoup(YOUR_MARKUP})
    
    to this:
    
     BeautifulSoup(YOUR_MARKUP, "lxml")
    
      markup_type=markup_type))



```python
nameList = bsObj.findAll('span',{'class':'green'}) # 拿到所有span且CSS类为green的标签
```


```python
for name in nameList:
    print(name.get_text())
```

    Anna
    Pavlovna Scherer
    Empress Marya
    Fedorovna
    Prince Vasili Kuragin
    Anna Pavlovna
    St. Petersburg
    the prince
    Anna Pavlovna
    Anna Pavlovna
    the prince
    the prince
    the prince
    Prince Vasili
    Anna Pavlovna
    Anna Pavlovna
    the prince
    Wintzingerode
    King of Prussia
    le Vicomte de Mortemart
    Montmorencys
    Rohans
    Abbe Morio
    the Emperor
    the prince
    Prince Vasili
    Dowager Empress Marya Fedorovna
    the baron
    Anna Pavlovna
    the Empress
    the Empress
    Anna Pavlovna's
    Her Majesty
    Baron
    Funke
    The prince
    Anna
    Pavlovna
    the Empress
    The prince
    Anatole
    the prince
    The prince
    Anna
    Pavlovna
    Anna Pavlovna



```python
temp = bsObj.findAll('span',{'class','red'})
```


```python
# for some in temp:
#     print(some.get_text(),'\n')
```

### 小总结

上面是通过`bsObj.findAll(tagName, tagAttributes)`拿到一个内容列表，接着用`name.get_text()`拿到我们需要的内容，不包含尖刀标签。

但是要记住，`get_text()`函数不要常用，因为查询内容，在bsObj中要容易很多。那保留完整的tag结构的文档，是很重要的。

### find() vs. findAll()

find返回的是搜索到的第一个值。

95%的情况下，二者都只需要用到前两个参数：

- tag
- attributes

注意tag可以是多个。

`findAll({'h1','h2','h3'},{'class': 'green', 'class':'red'})`

第三个参数是`recursive`，默认为`True`.

第四个参数是`text`，可以根据指定text内容做过滤。

至于二者共同的最后一个参数是`keyword`,但是这个参数比较鸡肋。正则表达式或者Lambda表达式会更好用。**注意findAll**倒数第二个参数是`limit`，在“取出前多少items”这种情况下可用。


```python
nameList = bsObj.findAll(text='the prince') # 测试了一下 需要是精确匹配才行
```


```python
print(len(nameList))
```

    7


### BS的四类对象

- BeautifulSoup对象
- Tag对象，通过`find`,`findAll`得到的结果
- NavigableString对象
- Comment对象，能够找到`<!--like this-->`这类数据

### 导航树

目前为止用到的查找函数都是根据尖刀标签的名字和属性，但是如果我们需要的是根据数据在文档中的位置呢？

#### children和descendants的区别

孩子就是下一代，后代是指很多代。清楚了吧！



```python
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://pythonscraping.com/pages/page3.html')
bsObj = BeautifulSoup(html)
```

    /Users/rick/anaconda3/lib/python3.6/site-packages/bs4/__init__.py:181: UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("lxml"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.
    
    The code that caused this warning is on line 193 of the file /Users/rick/anaconda3/lib/python3.6/runpy.py. To get rid of this warning, change code that looks like this:
    
     BeautifulSoup(YOUR_MARKUP})
    
    to this:
    
     BeautifulSoup(YOUR_MARKUP, "lxml")
    
      markup_type=markup_type))



```python
for child in bsObj.find('table',{'id':'giftList'}).children:
    print(child)
```

    
    
    <tr><th>
    Item Title
    </th><th>
    Description
    </th><th>
    Cost
    </th><th>
    Image
    </th></tr>
    
    
    <tr class="gift" id="gift1"><td>
    Vegetable Basket
    </td><td>
    This vegetable basket is the perfect gift for your health conscious (or overweight) friends!
    <span class="excitingNote">Now with super-colorful bell peppers!</span>
    </td><td>
    $15.00
    </td><td>
    <img src="../img/gifts/img1.jpg"/>
    </td></tr>
    
    
    <tr class="gift" id="gift2"><td>
    Russian Nesting Dolls
    </td><td>
    Hand-painted by trained monkeys, these exquisite dolls are priceless! And by "priceless," we mean "extremely expensive"! <span class="excitingNote">8 entire dolls per set! Octuple the presents!</span>
    </td><td>
    $10,000.52
    </td><td>
    <img src="../img/gifts/img2.jpg"/>
    </td></tr>
    
    
    <tr class="gift" id="gift3"><td>
    Fish Painting
    </td><td>
    If something seems fishy about this painting, it's because it's a fish! <span class="excitingNote">Also hand-painted by trained monkeys!</span>
    </td><td>
    $10,005.00
    </td><td>
    <img src="../img/gifts/img3.jpg"/>
    </td></tr>
    
    
    <tr class="gift" id="gift4"><td>
    Dead Parrot
    </td><td>
    This is an ex-parrot! <span class="excitingNote">Or maybe he's only resting?</span>
    </td><td>
    $0.50
    </td><td>
    <img src="../img/gifts/img4.jpg"/>
    </td></tr>
    
    
    <tr class="gift" id="gift5"><td>
    Mystery Box
    </td><td>
    If you love suprises, this mystery box is for you! Do not place on light-colored surfaces. May cause oil staining. <span class="excitingNote">Keep your friends guessing!</span>
    </td><td>
    $1.50
    </td><td>
    <img src="../img/gifts/img6.jpg"/>
    </td></tr>
    
    



```python
for child in bsObj.find('table',{'id':'giftList'}).descendants:
    print(child)
```

    
    
    <tr><th>
    Item Title
    </th><th>
    Description
    </th><th>
    Cost
    </th><th>
    Image
    </th></tr>
    <th>
    Item Title
    </th>
    
    Item Title
    
    <th>
    Description
    </th>
    
    Description
    
    <th>
    Cost
    </th>
    
    Cost
    
    <th>
    Image
    </th>
    
    Image
    
    
    
    <tr class="gift" id="gift1"><td>
    Vegetable Basket
    </td><td>
    This vegetable basket is the perfect gift for your health conscious (or overweight) friends!
    <span class="excitingNote">Now with super-colorful bell peppers!</span>
    </td><td>
    $15.00
    </td><td>
    <img src="../img/gifts/img1.jpg"/>
    </td></tr>
    <td>
    Vegetable Basket
    </td>
    
    Vegetable Basket
    
    <td>
    This vegetable basket is the perfect gift for your health conscious (or overweight) friends!
    <span class="excitingNote">Now with super-colorful bell peppers!</span>
    </td>
    
    This vegetable basket is the perfect gift for your health conscious (or overweight) friends!
    
    <span class="excitingNote">Now with super-colorful bell peppers!</span>
    Now with super-colorful bell peppers!
    
    
    <td>
    $15.00
    </td>
    
    $15.00
    
    <td>
    <img src="../img/gifts/img1.jpg"/>
    </td>
    
    
    <img src="../img/gifts/img1.jpg"/>
    
    
    
    
    <tr class="gift" id="gift2"><td>
    Russian Nesting Dolls
    </td><td>
    Hand-painted by trained monkeys, these exquisite dolls are priceless! And by "priceless," we mean "extremely expensive"! <span class="excitingNote">8 entire dolls per set! Octuple the presents!</span>
    </td><td>
    $10,000.52
    </td><td>
    <img src="../img/gifts/img2.jpg"/>
    </td></tr>
    <td>
    Russian Nesting Dolls
    </td>
    
    Russian Nesting Dolls
    
    <td>
    Hand-painted by trained monkeys, these exquisite dolls are priceless! And by "priceless," we mean "extremely expensive"! <span class="excitingNote">8 entire dolls per set! Octuple the presents!</span>
    </td>
    
    Hand-painted by trained monkeys, these exquisite dolls are priceless! And by "priceless," we mean "extremely expensive"! 
    <span class="excitingNote">8 entire dolls per set! Octuple the presents!</span>
    8 entire dolls per set! Octuple the presents!
    
    
    <td>
    $10,000.52
    </td>
    
    $10,000.52
    
    <td>
    <img src="../img/gifts/img2.jpg"/>
    </td>
    
    
    <img src="../img/gifts/img2.jpg"/>
    
    
    
    
    <tr class="gift" id="gift3"><td>
    Fish Painting
    </td><td>
    If something seems fishy about this painting, it's because it's a fish! <span class="excitingNote">Also hand-painted by trained monkeys!</span>
    </td><td>
    $10,005.00
    </td><td>
    <img src="../img/gifts/img3.jpg"/>
    </td></tr>
    <td>
    Fish Painting
    </td>
    
    Fish Painting
    
    <td>
    If something seems fishy about this painting, it's because it's a fish! <span class="excitingNote">Also hand-painted by trained monkeys!</span>
    </td>
    
    If something seems fishy about this painting, it's because it's a fish! 
    <span class="excitingNote">Also hand-painted by trained monkeys!</span>
    Also hand-painted by trained monkeys!
    
    
    <td>
    $10,005.00
    </td>
    
    $10,005.00
    
    <td>
    <img src="../img/gifts/img3.jpg"/>
    </td>
    
    
    <img src="../img/gifts/img3.jpg"/>
    
    
    
    
    <tr class="gift" id="gift4"><td>
    Dead Parrot
    </td><td>
    This is an ex-parrot! <span class="excitingNote">Or maybe he's only resting?</span>
    </td><td>
    $0.50
    </td><td>
    <img src="../img/gifts/img4.jpg"/>
    </td></tr>
    <td>
    Dead Parrot
    </td>
    
    Dead Parrot
    
    <td>
    This is an ex-parrot! <span class="excitingNote">Or maybe he's only resting?</span>
    </td>
    
    This is an ex-parrot! 
    <span class="excitingNote">Or maybe he's only resting?</span>
    Or maybe he's only resting?
    
    
    <td>
    $0.50
    </td>
    
    $0.50
    
    <td>
    <img src="../img/gifts/img4.jpg"/>
    </td>
    
    
    <img src="../img/gifts/img4.jpg"/>
    
    
    
    
    <tr class="gift" id="gift5"><td>
    Mystery Box
    </td><td>
    If you love suprises, this mystery box is for you! Do not place on light-colored surfaces. May cause oil staining. <span class="excitingNote">Keep your friends guessing!</span>
    </td><td>
    $1.50
    </td><td>
    <img src="../img/gifts/img6.jpg"/>
    </td></tr>
    <td>
    Mystery Box
    </td>
    
    Mystery Box
    
    <td>
    If you love suprises, this mystery box is for you! Do not place on light-colored surfaces. May cause oil staining. <span class="excitingNote">Keep your friends guessing!</span>
    </td>
    
    If you love suprises, this mystery box is for you! Do not place on light-colored surfaces. May cause oil staining. 
    <span class="excitingNote">Keep your friends guessing!</span>
    Keep your friends guessing!
    
    
    <td>
    $1.50
    </td>
    
    $1.50
    
    <td>
    <img src="../img/gifts/img6.jpg"/>
    </td>
    
    
    <img src="../img/gifts/img6.jpg"/>
    
    
    
    



```python
for sibling in bsObj.find('table',{'id':'giftList'}).tr.next_siblings: # 第一行不在此列
    print(sibling)
```

    
    
    <tr class="gift" id="gift1"><td>
    Vegetable Basket
    </td><td>
    This vegetable basket is the perfect gift for your health conscious (or overweight) friends!
    <span class="excitingNote">Now with super-colorful bell peppers!</span>
    </td><td>
    $15.00
    </td><td>
    <img src="../img/gifts/img1.jpg"/>
    </td></tr>
    
    
    <tr class="gift" id="gift2"><td>
    Russian Nesting Dolls
    </td><td>
    Hand-painted by trained monkeys, these exquisite dolls are priceless! And by "priceless," we mean "extremely expensive"! <span class="excitingNote">8 entire dolls per set! Octuple the presents!</span>
    </td><td>
    $10,000.52
    </td><td>
    <img src="../img/gifts/img2.jpg"/>
    </td></tr>
    
    
    <tr class="gift" id="gift3"><td>
    Fish Painting
    </td><td>
    If something seems fishy about this painting, it's because it's a fish! <span class="excitingNote">Also hand-painted by trained monkeys!</span>
    </td><td>
    $10,005.00
    </td><td>
    <img src="../img/gifts/img3.jpg"/>
    </td></tr>
    
    
    <tr class="gift" id="gift4"><td>
    Dead Parrot
    </td><td>
    This is an ex-parrot! <span class="excitingNote">Or maybe he's only resting?</span>
    </td><td>
    $0.50
    </td><td>
    <img src="../img/gifts/img4.jpg"/>
    </td></tr>
    
    
    <tr class="gift" id="gift5"><td>
    Mystery Box
    </td><td>
    If you love suprises, this mystery box is for you! Do not place on light-colored surfaces. May cause oil staining. <span class="excitingNote">Keep your friends guessing!</span>
    </td><td>
    $1.50
    </td><td>
    <img src="../img/gifts/img6.jpg"/>
    </td></tr>
    
    


### 为了爬虫的健壮性

上面的写法实际上是不够健壮的，页面改动后，可能就不是我们需要的内容了。而为了让爬虫更加健壮，需要更多利用属性来做，属性是相对稳定些的。

- next_siblings
- previous_siblings

这些函数都先混个脸熟。

要明确一个观点是：从你所在的标签出发到你想要找到的标签，这条路是弯弯曲曲的。所以，需要用到：

- .previous_sibling
- .next_sibling
- .parent
- .parents

等等，这些不是方法，而是属性，不要用调用方法的方式来使用。

运用之妙，存乎一心，具体的小模块，要通过分解学习，实际操练然后熟练掌握。


```python
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://pythonscraping.com/pages/page3.html')
bsObj = BeautifulSoup(html)

temp = bsObj.find('img',{'src': '../img/gifts/img1.jpg'}).parent.previous_sibling.get_text()
print(temp)
```

    
    $15.00
    


    /Users/rick/anaconda3/lib/python3.6/site-packages/bs4/__init__.py:181: UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("lxml"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.
    
    The code that caused this warning is on line 193 of the file /Users/rick/anaconda3/lib/python3.6/runpy.py. To get rid of this warning, change code that looks like this:
    
     BeautifulSoup(YOUR_MARKUP})
    
    to this:
    
     BeautifulSoup(YOUR_MARKUP, "lxml")
    
      markup_type=markup_type))


### 正则表达式

> 假设你有一个问题需要用正则表达式来解决，那么，现在你有两个问题了。

正则表达式很强大，很强大。

你指定的规则，通过正则表达式能够精确找到对应的数据。

`aa*bbbb(cc)*(d| )`.

下面自然进入实践环节。

# 识别邮件地址

[A-Za-z0-9\._+]+ : 加号表示至少有一个

完整组合出来的邮件地址规则是：

[A-Za-z0-9\._+]+@[A-Za-z]+\.(com|org|edu|net)

### 12个常见的正则表达式在Python中的用法

1. *: 与前面的字符相同的字符，0个或多个
2. +: 与前面的字符相同的字符，1个或多个
3. []: 从中括号内随便选**一个**
4. (): 括号就是用来管理优先级的
5. {m,n}: 前面的字符出现m~n次，注意这是可取m,n
6. [^]: 非，不在括号内的字符，比如：[^A-Z]*，就表示只要不是大写字母即可，apple, lowercase等都满足
7. |: 或
8. .: 任意单个字符均可，比如：b.d ==> bid, bad, bzd, b$d, b d都行
9. ^: 表明此符号后面的字符是首字符，比如：^a ==> apple, asdf
10. \: 转义字符
11. \$: 表明此符号前面的字符是结束字符
12. ?!: 不包含，使用小心


```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re # 引入正则表达式包

html = urlopen('http://pythonscraping.com/pages/page3.html')
bsObj = BeautifulSoup(html)
images = bsObj.findAll('img',{'src':re.compile('\.\.\/img\/gifts\/img.*\.jpg')}) #正则表达式用在这里哦~~
```

    /Users/rick/anaconda3/lib/python3.6/site-packages/bs4/__init__.py:181: UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("lxml"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.
    
    The code that caused this warning is on line 193 of the file /Users/rick/anaconda3/lib/python3.6/runpy.py. To get rid of this warning, change code that looks like this:
    
     BeautifulSoup(YOUR_MARKUP})
    
    to this:
    
     BeautifulSoup(YOUR_MARKUP, "lxml")
    
      markup_type=markup_type))



```python
for image in images:
    print(image['src'])
```

    ../img/gifts/img1.jpg
    ../img/gifts/img2.jpg
    ../img/gifts/img3.jpg
    ../img/gifts/img4.jpg
    ../img/gifts/img6.jpg


正则表达式是个直达电梯，能够精准，快速帮我们锁定到需要的目标元素。

### 标签的属性获取

`myTag.attrs`,返回的是一个字典，然后能够通过字典的使用方法拿到具体的属性值。比如：`myTag.attrs['src']`

### Lambda表达式

本质上说，Lambda表达式就是一类函数，这类函数能够传递到其他函数当作参数或者变量使用。

在BS中的`findAll`函数中，我们就可以传递特定类型的函数。这类特定函数就是接收`tag`对象当作参数，返回布尔值。

`soup.findAll(lambda tag: len(tag.attrs) == 2)`

### BS之外

虽然本书主要通过BS来讲解爬虫开发，但是如果有些场景下搞不定，可以去看`lxml`和`HTML Parser`管不管用，这些都是老牌的哦！
