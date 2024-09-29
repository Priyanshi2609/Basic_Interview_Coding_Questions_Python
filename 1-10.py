#1.Check if a Number is Positive and Negative 
'''
num=int(input("Enter a number"))
if num>0:
    print("The number is Positive")
elif num<0:
    print("The number is Negative")
else:
    print("The number is Neutral")        
'''    

#2. Check Whether a Number is Even or Odd
'''
num=int(input("Enter a number:"))
if num%2==0:
    print("Even Number")
else:
    print("Odd Number")    

print("Even" if num%2==0 else "Odd")'''


#3. Find the Sum of The First N Natural Numbers 
'''
num=int(input("Enter a number:"))
sum=0
for i in range(1,num+1):
    sum+=i
print(sum) 

print(num*(num+1)/2)  #less time complexity

#recursive
def getSum(num):
    if num==1:
        return 1
    return num+getSum(num-1)
print(getSum(num))'''


#4. Find the Sum of the Numbers in a Given Range
'''
num1=int(input())
num2=int(input())
sum=0
for i in range(num1,num2+1):
    sum+=i
print(sum)    

#recursion
def getSum(num1,num2):
    if num1==num2:
        return num2
    return num1+getSum(num1+1,num2)
print(getSum(5,19))
'''
 
#5. Find the Greatest of Two Numbers
'''
num1=int(input('Enter first number:'))
num2=int(input('Enter second number:'))
if num1>num2:
    print(num1)
else:
    print(num2)    
    
print(num1 if num1>num2 else num2)  #ternary
print(max(num1,num2))  #inbuilt max() function
'''

#6. Find the Greatest of the Three Numbers
'''
num1=int(input())
num2=int(input())
num3=int(input())
if num1>=num2 and num1>=num3:
    print(num1)
elif num2>=num1 and num2>=num3:
    print(num2)
else:
    print(num3)        

#ternary    
max=num1 if num1>=num2  else num2
max=num3 if num3>=max else max
print(max)'''


#7. Check if a Year is a Leap Year or Not 
'''
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Example usage:
year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
'''
    
    
#8. Check Whether a Number is a Prime or Not 
'''
num=int(input())
prime=True
if num<=1:
    prime=False
for i in range(2,int(num**0.5)+1):
    if num%i==0:
        prime=False
        break     
   
print(prime)'''


#9. Print Prime Numbers In a Given Range
'''
def is_prime(num):
    prime=True
    if num<=1:
        prime=False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            prime=False
            break    
    return prime 
start=int(input())
end=int(input())
prime_nos=[]
for num in range(start,end+1):
    if is_prime(num)==True:
        prime_nos.append(num)
print(prime_nos)'''       
                    

#10. Sum of Digits of a Number 
'''
def sum_of_digits(number):
    total_sum = 0
    while number > 0:
        digit = number % 10  # Extract the last digit
        total_sum += digit    # Add the digit to the sum
        number = number // 10  # Remove the last digit
    return total_sum

# Example Usage
num = int(input("Enter a number: "))
result = sum_of_digits(num)
print(f"Sum of digits: {result}")'''