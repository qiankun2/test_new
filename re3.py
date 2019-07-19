import re
#习题集一

#习题2 判断是否匹配成功,并输出相应的信息

s1 = "1huhongqiang"

s1_1 = re.findall(r'^\w+$',s1)
if s1_1:
    print('匹配成功',s1_1)
else:
    print('匹配失败')

s1_2 = re.match(r'^\w+$',s1).group()
if s1_2:
    print('匹配成功',s1_2)
else:
    print('匹配失败')

#习题2 找出s2字符串中是否有连续的5个数字，并打印出来

s2 = '1234aadd222222'

s2_1 = re.findall(r'\d{5}',s2)
print('s2_1',s2_1)

s2_2 = re.match(r'\d{5}',s2)
print('s2_2',s2_2)

s2_3 = re.search(r'\d{5}',s2).group()
print('s2_3',s2_3)

#习题3 找出一个字符串中的连续5个数字，要求数字前后必须是非数字
s3 = "12567 12345d"

s3_1 = re.search(r'\D(\d{5})\D',s3)
print('s3_1',s3_1)

#习题4 统计一个文件有多少个单词
with open('a.txt','r') as f:
    s4 = f.read()
s4_1 = re.findall(r'\b\w+',s4)
print('s4_',len(s4_1))

#习题5:把a1b23c4d非字符内容拼成一个字符串
s5 = "a1b23c4d"

s5_1 = re.findall(r'[^a-zA-Z]',s5)
print('s5_1',"".join(s5_1))
