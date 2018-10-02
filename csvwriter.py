import csv

with open('data.csv', 'w') as csvfile:
	writer = csv.writer(csvfile, delimiter=',') # 修改字段之间的分隔符 

	# 一次写一行
	writer.writerow(['id','name','age'])
	writer.writerow(['10001','Mike','20'])
	writer.writerow(['10002','Bob','22'])
	writer.writerow(['10003','Jordan','21'])

	# 同时写入多行
	writer.writerows([['10004','Ada','25'],['10005','Dick','24']])

# 上面写入的数据是列表型数据，头部名称也是一样的方式写入
# 爬取的数据更多是字典型的，所以下面这个写法是更加常用的
with open('data.csv', 'a') as csvfile:
	fieldnames = ['id','name','age']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writerow({'id':'10005','name':'Cherry','age':22})

# 写入包含中文的数据，加上编码即可
with open('data.csv','a', encoding='utf-8') as csvfile:
	fieldnames = ['id','name','age']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writerow({'id':'10006','name':'李四', 'age':26})

# 读取csv文件
with open('data.csv','r',encoding='utf-8') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		print(type(row))
		print(row)
