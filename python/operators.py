a = 10
b = 8
print("ARITHMETIC operators")
print('1.Addition')
print(a+b)
print()
print('2.subtraction')
print(a-b)
print('3.Multiplication')
print(a*b)
print('4.Division')
print(a/b)
print('5.Modulus')
print(a%b)
print('6.Exponentiation')
print(a**b)
print('7.floor Division')
print(a//b)

print("Comparision Operators")

print('1.Equal')
print(a == b)

print('2.Not Equal')
print(a != b)

print('3.Greater than')
print(a > b)

print('4.Lessthan')
print(a < b)

print('5.Greaterthan or Equal to')
print(a >= b)

print('6.Lessthan or Equal to')
print(a <= b)

print("Logical Operators")

print('1.AND...,Returns True if both statements are true')
print(a > 5 and a < 20)

print('2.OR...,Returns True if one of the statements is true')
print(a < 20 or a > 15)

print('3.NOT...,Reverse the result, returns False if the result is true')
print(not(a < 20 or a > 15))


print("ASSIGNMENT Operators")


import math

x = 10
print('1.=')
print(x)

print('2.+=')
x += 5
print(x)

print('3.-=')
x -= 5
print(x)

print('4.*=')
x *= 5
print(x)

print('5./=')
x /= 5
print(x)

print('6.%=')
x %= 5
print(x)

print('7.//=')
x //= 5
print(x)

print('8.**=')
x **= 5
print(x)

'''print('9.&=')
x &= 5
print(x)

print('10.|=')
x |= 5
print(x)

print('11.^=')
x ^= 5
print(x)

print('12.>>=')
x >>= 3
print(x)

print('13.<<=')
x <<= 5
print(x)'''


print("IDENTITY Operators")

M=10
N=10.35
print(id(M))
print(id(N))

print('1.IS')
print(type(M) is int)
print('2.IS NOT')
print(type(M) is not float)

print('1.IS')
print(type(N) is int)
print('2.IS NOT')
print(type(N) is  float)


print("MEMBERSHIP Operators")

print('1.IN')

vowels = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']
 
ch = input('Please Enter a Letter:\n')
 
if ch in vowels:
    print('You entered a vowel character')
else:
    print('You entered a consonants character')

print('2.NOT IN')

primes=(2,3,5,7,11)
print(1 not in primes)
print(3 not in primes)

print("UNARY MINUS OPERATOR(-)")

s=-50
print(s)
print(-s)
print()
print("Ternary Operator")
i, j = 10, 20
  
# Copy value of i in min if i < j else copy j 
min = i if i > j else j 
  
print(min)