#11. Reverse a Number
'''
num=input()
reversed_num=num[::-1]
print(reversed_num)
num=int(input())
reverse=0
while num>0:
    remainder=num%10
    reverse=(10*reverse)+remainder
    num=num//10
print(reverse)'''


#12. Check Whether or Not the Number is a Palindrome
'''
num=input()
reversed_num=num[::-1]
if reversed_num==num:
    print("Palindrome")
else:
    print("Not a palindrome")'''
    
    
#13. Check Whether a Given Number is an Armstrong Number or Not
'''
def is_armstrong(number):
    str_num=str(number)
    n=len(str_num)
    sum=0
    for i in str_num:
        sum+= int(i)**n
    if sum==number:
        return "Armstrong Number"
    else:
        return "Not an Armstrong Number"
print(is_armstrong(3711))'''
#using Recursion
'''
def is_armstrong(number):
    digit_len=len(str(number))
    return number==armstrong_helper(number,digit_len)
def armstrong_helper(number,digit_len):
    digit=number%10
    if digit==0:
        return 0
    return digit**digit_len + armstrong_helper(number//10,digit_len)
if is_armstrong(37165):
    print("Armstrong Number")
else:
    print("Not an armtsong number")
'''

#14. Find the Armstrong Number in a given Range 
'''
def is_armstrong(number):
    str_num=str(number)
    n=len(str_num)
    sum=0
    for i in str_num:
        sum+= int(i)**n
    if number==sum:
        return True
    else:
        return False
start=int(input())
end=int(input())
ans=[]
for num in range(start,end+1):
    if is_armstrong(num)==True:
        ans.append(num)
print(ans)    '''
    
#15. Find the Fibonacci Series up to Nth Term
'''
limit=int(input())
n1=0
n2=1
print(n1)
print(n2)
for i in range(2,limit):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3)'''
#using recursion
'''
def fibonacci(n):
    if n<=0:
        return "Number should be always positive"
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=int(input())   
for i in range(1,n+1):
    print(fibonacci(i))'''
    
    
#16. Factorial of a number
'''
def factorial(number):
    fact=1
    if number==0:
        return 1
    else:
        for i in range(1,number+1):
            fact=fact*i
        return fact
print(factorial(6))
#using recursion
def factorial_rec(n):
    if n==0:
        return 1
    else:
        return factorial_rec(n-1)*n
print(factorial_rec(6)) '''          


#17. Find the Power of a Number
'''
print(pow(2,3))
print(2**3)
base=int(input())
power=int(input())
ans=1
for i in range(1,power+1):
    ans=ans*base
print(ans)
#using recursion
def power_of_num(num,power):
    if power==0:
        return 1
    return num*power_of_num(num,power-1)
print(power_of_num(5,4))'''

#18. Factor of a number
'''
num=int(input())
for i in range(1,num+1):
    if num%i==0:
        print(i)'''
        
#19. Find the Prime Factors of a Number  
'''
num=int(input())
arr=[]
prime_nos=[2]
for i in range(1,num):
    if num%i==0:
        arr.append(i)
for j in arr:
    for k in range(2,int(j**0.5)+1):
        if j%k==0:
            break
        else:
            prime_nos.append(j)
print(prime_nos)'''

#20. Check Whether or Not the Number is a Strong Number
'''
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

num=input("Enter a Number:")
ans=0
for i in num:
    digit=int(i)
    ans+=factorial(digit)
if ans==int(num):
    print("Its a strong Number")
else:
    print("Not a strong number")
'''