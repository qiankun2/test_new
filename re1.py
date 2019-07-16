import re
s = r"010\12345"
s2 = "cart"

if re.match("ca.*t",s2):
    print("ok")
else:
    print("no")

s4 = "03/19/76"

if re.match("\d\d[-./]\d\d[-./]\d\d",s4):
    print("ok")
else:
    print("no")

s5 = "gray"
s6 = "grey"
if re.match("gray|grey",s5 and s6):
    print('ok')
else:
    print('no')

if re.match('gr(e|a)y',s5 and s6):
    print('ok')
else:
    print('no')

ss = "zozzozzoz"
print(re.match('zoz?',ss))

str = 'www.baidu.com'

str1,str2,str3= str.split('.')[0]
print(str1,str2,str3)

str5 = 'www.baidu.com'
print(str5.split('.',1))

str6 = 'aaabbbccc'
print(str6.split('c',1))

str6 = 'a b  c'
print(str6.split())

str7 = '010-12345'
me = re.match('(^\d{3})(-)(\d{3,8}$)',str7)

print(me)
print(me.group(0))
print(me.group(1))
print(me.group(2))
print(me.group(3))

