
#inputs and outputs in python
3+2
5
a='the'
b=3
c='musketeers'
print(a,b,c)
the 3 musketeers
print(a +str(b) +c)
the3musketeers
print(a + b+ c) # this is an error
TypeError: can only concatenate str (not "int") to str

num=5
print('my num is ',num)
my num is  5
s = 'my num is' + str(num)
print(s)
my num is 5

x=input(s) # syntax
#Binds that value to a variable
text = input("type anything")
type anything 5
print(5*text)
55555

text = input("type anything")
type anything howdy
print(5*text)
howdy howdy howdy howdy howdy

#input always returns str
num1=input("Type a number: ")
Type a number: 3
print(5*num1)
33333

num2=int(input("Type a number: "))
Type a number: 3
print(5*num2)
15

question = input('choose a verb: ')
choose a verb: run
print('I can' ,question,'better than you')
I can run better than you
print(5*(' '+question))
run run run run run

# Newton's method for cube root
x = int(input('What x to find the cube root of ? '))
What x to find the cube root of ? 27
g = int(input('what guess to start with? '))
what guess to start with? 5
print('Current estimate cubed = ',g**3)
Current estimate cubed =  125
next_g = g - ((g**3 -x)/(3*g**2))
print('Next guess too try = ',next_g)
Next guess too try =  3.6933333333333334

