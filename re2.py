import re

s = 'yanjingsuyan'

n1 = re.match('yan',s)
print('n1',n1)

n2 = re.search('yan',s)
print('n2',n2)

n3 = re.findall('yan',s)
print('n3',n3)

n4 = re.split('y',s)
print(n4)

n5 = re.sub('y','1',s)
print(n5)


s2 = 'bat bit but hat hit hut'

n6 = re.findall(r'\bb\w+',s2)
print('n6',n6)

s3= "33 i love you not because 12sd! 34er 56df e4 54434"

n7 = re.findall(r'\b\d',s3)
print('n7',n7)

s4 = "i love you not because\n12sd 34er 56\ndf e4 54434"
n8 = re.findall(r'\w+',s4)
print('n8',n8)

n9 = re.findall(r'\w+',s4,re.M)
print('n9',n9)

w1 = "abc"
w1_1 = re.match("A",w1,re.I).group()
print(w1_1)

w2 = '12 34\n56 78\n90'
w2_1 = re.findall( r'^\d+',w2,re.M)
print('w2_1',w2_1)

w2_2 = re.findall( r'\A\w+',w2,re.M)
print('w2_2',w2_2)

w2_3= re.findall(r'\d+$',w2,re.M)
print('w2_3',w2_3)

w2_4 = re.findall(r'\d+\Z',w2,re.M)
print('w2_4',w2_4)

s5 = "'bat', 'bit', 'but', 'hat', 'hit', 'hut‘"
s5_1 = re.findall(r'..t',s5)
print('s5_1',s5_1)

s6 = "awoeur awier !@# @#4_-asdf3$^&()+?><dfg$\n$"
s6_1 = re.findall(r'(.*?\S)',s6,re.DOTALL)
print('s6_1',s6_1)

s7 = '123456789\t123456789'
s7_1 = re.findall('\d*',s7)
print(s7_1)

s8 = """se234 1987-02-09 07:30:00
    1987-02-10 07:25:00"""

s8_1 = re.findall(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}',s8)
print('s8_1',s8_1)

s8_2 = re.findall(r'\d{4}-\d{2}-\d{2}|\d{2}:\d{2}\d{2',s8,re.M)
print('s8_2',s8_2)

print("----------------------------------------")

s9 = """693152032@qq.com, werksdf@163.com, sdf@sina.com
    sfjsdf@139.com, soifsdfj@134.com
    pwoeir423@123.com"""

s9_1 = re.sub(r'.+?@.+?.com','2554536822@qq.com',s9)
print('s9_1',s9_1)

s9_2 = re.sub(r'\w+@\w+.com','2554536822@qq.com',s9,re.S)
print('s9_2',s9_2)

s10 = "skjdfoijower \home   \homewer"

s10_1 = re.findall(r'\\home',s10)
print('s10_1',s10_1)

s11 = """i love you not because of who 234 you are, 234 but 3234ser because of who i am when i am with you"""

s11_1 = re.findall(r'\b[a-zA-Z]+\b',s11)
print('s11_1',s11_1)

s11_2 = re.findall(r'\b[a-zA-Z]+\b',s11)
print('s11_2',s11_2)

s12 = """xiasd@163.com, sdlfkj@.com sdflkj@180.com solodfdsf@123.com 
     sdlfjxiaori@139.com saldkfj.com oisdfo@.sodf.com.com @.com"""

s12_1 = re.findall(r'\w+@\w+.com',s12)
print('s12_1',s12_1)







