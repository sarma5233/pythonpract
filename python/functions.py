"""def first(a):
 def second(b):
  return a+b
 return second

adv = first(10)

print(adv(12))
"""

def Total_sum(nod,k):
    s = 0
    while(k > 0):  
        r = k % 10
        s += (r**nod)           # a**b is a raised to power b
        k //= 10
    return s                    # returns the calculated sum
    
def Number_of_digits(num):      # function to calculate number of digits in a number
    c = 0
    while (num>0):
        c+=1
        num//=10
    return c

def isArmstrong(n):
    k = n
    nod = Number_of_digits (k)         # calling a Number_of_digits function
    sum_of_digits = Total_sum (nod,k)  # calling Total_sum function from another function isArmstrong()
    if (sum_of_digits == n):
        return True
    return False
    
a = int(input("Enter the lower range  :"))
b = int(input("Enter the higher range :"))
print ("The Armstrong numbers in the given range",a, "and",b,"are")
for i in range(a,b+1):
    if(isArmstrong(i)):
        print (i)