#21. Check Whether or Not the Number is a Perfect Number (sum of its divisors is equal to itself)
'''
num=int(input())
sum=0
for i in range(1,num//2+1):
    if num%i==0:
        sum+=i
if sum==num:
    print("Its a Perfect Number")
else:
    print("Its not a perfect number")'''
#using recusrion
'''
def get_sum(num,i=1):
    if i>num//2:
        return 0
    if num%i==0:
        return i+get_sum(num,i+1)
    else:
        return get_sum(num,i+1)
num=int(input())
if get_sum(num)==num:
    print("Perfect Number")
else:
    print("Not a perfect Number")'''
     
     
#22. Check for Perfect Square
'''
import math
num=int(input())
root=int(math.sqrt(num))
if root*root==num:
    print("Perfect Square Root")
#OR
def perfect_num(n):
    i=0
    while i*i<=num:
        if i*i==num:
            return True
        else:
            i+=1
    return False
if perfect_num(num)==True:
    print("Perfect Square Number")
else:
    print("Not a perfect square")'''
    
    
#23. Check Whether or Not the Number is an Automorphic Number (Its square ends with the number itself)
'''
num=int(input())
square=num*num
string_square=str(square)
string_num=str(num)
if string_square.endswith(string_num):
    print("Its an Automorphic Number")
else:
    print("Not an Automorphic Number")
#Or (without built in function)
len_num=len(string_num)
if string_square[-len_num:]==string_num:
    print("Its an Automorphic Number")
else:
    print("Not an Automorphic Number")'''
    
    
#24. Check Whether or Not a Number is a Harshad Number (A Number that is divisible by the sum of it's digits is known as a Harshad number.)
'''
num=input()
sum=0
for i in num:
    sum+=int(i)
if int(num)%sum==0 and sum!=0:
    print("Harshad Number")
else:
    print("Not a Harshad Number")'''
    
    
#25. Check Whether or Not the Number is an Abundant Number
# A Number that is smaller than the sum of all it's factors except the number itself is known as an Abundant number.
'''num=int(input())
sum=0
for i in range(1,num):
    if num%i==0:
        sum+=i
if sum>num:
    print("Abundant Number")
else:
    print("Not an Abundant Number")'''
    
    
#26. Check Whether or Not the Two Numbers  are Friendly Pairs 
#The numbers whose ( sum of divisors ) / number ratio is same are known as Friendly Pair Numbers.
'''
n1=int(input("Enter first numbers"))
n2=int(input("Enter second numbers"))

def sum_of_divisors(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    return int(sum//num)
if sum_of_divisors(n1)==sum_of_divisors(n2):
    print("Two Numbers  are Friendly Pairs")
else:
    print("Not Friendly Pairs")'''
    

#27. HCF or GCD of Two Numbers
'''
num1=int(input("Enter two numbers:"))
num2=int(input())
def hcf(a,b):
    while b: #till b=0
        a,b=b,a%b
    return a
#print(hcf(num1,num2))
#OR RECURSION
def recursive(a,b):
    if b==0:
        return a
    else:
        return recursive(b,a%b)
print(recursive(num1,num2))'''


#27. LCM of Two Numbers (lcm * hcf)=(a*b)
'''
num1=int(input("Enter two numbers:"))
num2=int(input())
def hcf(a,b):
    while b: #till b=0
        a,b=b,a%b
    return a
hcf_of_numbers=hcf(num1,num2)
print(abs(num1*num2)//hcf_of_numbers)'''


#28. Binary to Decimal Conversion
'''
binary_no=input()
sum=0
n=len(binary_no)-1
for i in binary_no:
    sum+= int(i)*2**n
    n=n-1
    
print(sum)'''


#29. Octal To Decimal Conversion
'''
octal_no=input()
sum=0
n=len(octal_no)-1
for i in octal_no:
    sum+= int(i)*8**n
    n=n-1
print(sum)'''


#30. Hexadecimal to Decimal Conversion
'''
hexadecimal_no=input()
n=len(hexadecimal_no)-1
sum=0
for digit in hexadecimal_no:
    if '0'<= digit <='9':
        value=digit
    elif 'A'<= digit <='F':
        value=ord(digit)-ord('A')+10 #ord calculates ascii value
    elif 'a'<= digit <='f':
        value=ord(digit)-ord('a')+10
    sum+=int(value)*16**n
    n=n-1
print(sum)'''
