#This is single line comment
print("The single line comment in python is done by using '#'")
'''This is
Multiline comment
'''
print("Multiline comment is given by ''' ")
""" This is
also Multiline comment
"""
print('Multiline comment is also given  by """ ')

a=10
b=30.5
c="Vihaan"
d=3+5j

print("a=",a," ",type(a))
print("b=",b," ",type(b))
print("c=",c," ",type(c))
print("d=",d," ",type(d))

e=int(a)+int(b)
print("e=",e,type(e))

x=input("Enter x ")
y=input("Enter y ")
z=int(x)+int(y) #if you dont typecast then compiler think input as string so it concatenate it.
print(x,"+",y,"=",z, type(z))

f=input("Enter complex : ")
g=a+complex(f)
print(g,type(g))


