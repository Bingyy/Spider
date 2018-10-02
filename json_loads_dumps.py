import json

string = '''
[
	{
		"name": "Bob",
		"gender": "male",
		"birthday": "1992-10-18"
	},

	{
		"name": "Selina",
		"gender": "female",
		"birthday": "1995-10-28"
	}
]
'''
print(type(string))

data = json.loads(string) # 加载为json对象
print(data)
print(type(data)) # 最外围是list，所以这里也是list类型

# 基于索引获取对应内容
print(data[0]['name'])
print(data[0].get('name')) # 推荐使用get

# 读取json文本 --> 转换成对象，对象可以直接操作
with open('data.json','r') as file:
	string = file.read()
	data = json.loads(string)
	print(data)


# 对象保存到json文本
data = [
	{
		"name": "张三",
		"gender": "male",
		"birthday": "1992-10-18"
	},

	{
		"name": "Selina",
		"gender": "female",
		"birthday": "1995-10-28"
	}
]
# 这样可以保证输出为中文
with open('data.json','a', encoding='utf-8') as file:
	string = json.dumps(data,indent=2, ensure_ascii=False)
	file.write(string)
