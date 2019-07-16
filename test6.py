from enum import Enum

Month = Enum("Month",("一","二","三","四","五","六","七","八","九","十"))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

class meiju(Enum):
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    f = 6

print(meiju(3))
print(meiju["a"])

m = meiju.d
print(m.name)
print(m.value)

