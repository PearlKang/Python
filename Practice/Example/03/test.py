"""
Author: ByungWoo Kang
Date: 2021-09-20 ~
이 프로그램은 문자형 테스트 입니다.
"""

"""""""""  test  """""""""
a = 'test'
print(a)
print('')

a = "test"
print(a)
print('')

a = '"test"'
print(a)
print('')

a = "'test'"
print(a)
print('')
"""""""""  test  """""""""


a = "Hello World"
print(a)
print('')

a = 'Python is fun'
print(a)
print('')

a = """Life is too short, You need python"""
print(a)
print('')

a = '''Life is too short, You need python'''
print(a)
print('')

a = "Python's favorite food is perl"
print(a)
print('')

a = '"Python is very easy." he says.'
print(a)
print('')

a = 'Python\'s favorite food is perl'
print(a)
print('')

a = "\"Python is very easy.\" he says."
print(a)
print('')

a = "Life is too short\nYou need python"
print(a)
print('')

a = '''
Life is too short
You need python
'''
print(a)
print('')

a = """
Life is too short
You need python
"""
print(a)
print('')

head = "Python"
tail = " is fun!"
print(head + tail + "\n")

a = "Python"
print(a*2 + "\n")

print("=" * 50)
print("My Program")
print("=" * 50)
print('')

a = "Life is too short"
print(len(a))
print('')

a = "You need python"
print(len(a))
print('')

a = "Life is too short, You need Python"
print(a)
print(a[0])
print(a[-1])
b = a[0] + a[1] + a[2] + a[3]
print(b)
print(a[0:4])
print(a[0:3])
print(a[19:])
print(a[0:])
print(a[:17])
print(a[:])
print(a[19:-7])
print('')

a = "20010331Rainy"
date = a[:8]
weather = a[8:]
print(a)
print(date)
print(weather)
print('')

a = "20010331Rainy"
year = a[:4]
day = a[4:8]
weather = a[8:]
print(a)
print(year)
print(day)
print(weather)
print('')

a = "Pithon"
print(a)
#a[1] = "y"
#print(a)
print(a[:1] + 'y' + a[2:])

print("I eat %d apples." % 3)
print("I eat %s apples." % "five")
print('')

number = 3
print("I eat %d apples." % number)
print('')

number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days." % (number, day))
print('')

print("I have %s apples" % 3)
print("rate is %s" % 3.234)
print("Error is %d%%" % 98)
print('')

print("%10s" % "hi")
print("%-10sjane" % "hi")
print('')

print("%0.4f" % 3.42134234)
print("%10.4f" % 3.42134234)
print('')

print("I eat {0} apples".format(3))
print("I eat {0} apples".format("five"))
print('')

number = 3
print("I eat {0} apples".format(number))
print('')

number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days.".format(number, day))
print('')

print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3))
print('')

print("I ate {0} apples. so I was sick for {day} days.".format(10, day=3))
print('')

print("{0:<10}".format("hi"))
print("{0:>10}".format("hi"))
print("{0:^10}".format("hi"))
print("{0:=^10}".format("hi"))
print("{0:*<10}".format("hi"))
print("{0:!>10}".format("hi"))
print('')

y = 3.42134234
print("{0:0.4f}".format(y))
print("{0:10.4f}".format(y))
print('')

print("{{ and }}".format())
print('')

name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
print('')

age = 30
print(f'나는 내년이면 {age+1}살이 된다.')
print('')

d = {'name':'홍길동', 'age':30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')
print('')

print(f'{"hi":<10}')
print(f'{"hi":>10}')
print(f'{"hi":^10}')
print('')

print(f'{"hi":=^10}')
print(f'{"hi":!<10}')
print('')

y = 3.42134234
print(f'{y:0.4f}')
print(f'{y:10.4f}')
print('')

print(f'{{ and }}')
print('')

print("{0:!^12}".format('python'))
print(f'{"python":!^12}')
print('')

a = "hobby"
print(a.count('b'))
print('')

a = "Python is the best choice"
print(a.find('b'))
print(a.find('k'))
print('')

a = "Life is too short"
print(a.index('t'))
#print(a.index('k'))
print('')

print(",".join('abcd'))
print(",".join(['a', 'b', 'c', 'd']))
print('')

a = "hi"
print(a.upper())
a = "HI"
print(a.lower())
a = " hi "
print('')
print(a)
print(a.lstrip())
print(a.rstrip())
print(a.strip())
print('')

a = "Life is too short"
print(a)
print(a.replace("Life", "Your leg"))
print('')

a = "Life is too short"
print(a)
print(a.split())
b = "a:b:c:d"
print(b)
print(b.split(':'))
