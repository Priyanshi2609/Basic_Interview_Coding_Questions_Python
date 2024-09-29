#31. Decimal to binary conversion 
'''
decimal_no=int(input())
result=decimal_no
binary_no=""
while result>0:
    rem=result%2
    binary_no=str(rem)+binary_no
    result=result//2
if decimal_no==0:
    binary_no=0
print(binary_no)'''

#32. Decimal to octal conversion
'''
decimal_no=int(input())
result=decimal_no
octal_no=""
while result>0:
    rem=result%8
    octal_no=str(rem)+octal_no
    result=result//8
if decimal_no==0:
    octal_no=0
print(octal_no)'''

#33. Decimal to hexadecimal conversion
'''
hex_dict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
decimal_no=int(input())
result=decimal_no
hexadecimal_no=""
while result>0:
    rem=result%16
    if 9<rem<=15:
        hexadecimal_no=hex_dict[rem]+hexadecimal_no
    else:
        hexadecimal_no=str(rem)+hexadecimal_no
    result=result//16
if decimal_no==0:
    hexadecimal_no=0
print(hexadecimal_no)'''

#34. Binary to Octal Conversion
'''
binary_no=input()
def get_decimal(binary_no):
    n=len(binary_no)-1
    decimal_no=0
    for i in binary_no:
        decimal_no+=int(i)*2**n
        n=n-1
    return decimal_no
def dec_to_octal(decimal_no):
    result=decimal_no
    octal_no=""
    while result>0:
        rem=result%8
        octal_no=str(rem)+octal_no
        result=result//8
    if decimal_no==0:
        octal_no=0
    return octal_no
decimal_number=get_decimal(binary_no)
octal_number=dec_to_octal(decimal_number)
print(f"The Conversion of {binary_no} Binary to Octal is {octal_number}")'''

#35. Octal To Binary Conversion
'''
octal_num=input("Octal Number:")
decimal_no=0
n=len(octal_num)-1
for i in octal_num:
    decimal_no+= int(i)*8**n
    n=n-1
def dec_to_binary(decimal_no):
    result=decimal_no
    binary_no=""
    while result>0:
        rem=result%2
        binary_no=str(rem)+binary_no
        result=result//2
    if decimal_no==0:
        binary_no=0
    return binary_no
print(dec_to_binary(decimal_no))  '''

#36. Quadrants in which a given coordinate lies 
'''
x=int(input("Enter x co-ordinate"))
y=int(input("Enter y co-ordinate"))
if x==0 and y==0:
    print("The point lies at origin")
elif x==0 and y!=0:
    print("The point lies at y axis")
elif y==0 and x!=0:
    print("The point lies at x axis")
elif x>0 and y>0:
    print("The point lies in First Quadrant")
elif x<0 and y>0:
    print("The point lies in Second Quadrant")
elif x<0 and y<0:
    print("The point lies in Third Quadrant")
else:
    print("The point lies in Fourth Quadrant")'''
    
#37. Which n people can occupy r seats in a classroom (Use permutation formula { factorial(n) / factorial(n-r) })
'''
def get_factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
n=int(input("Enter the number of people"))
r=int(input("Enter number of seats"))
print(get_factorial(n)//get_factorial(n-r))'''

#38. Maximum Number Of Handshakes ((N-1) * N ) / 2
'''
n=int(input("Enter number of people:"))
number_of_handshakes=((n-1)*n)//2
print(number_of_handshakes)'''

#39. Replace All 0’s With 1 In A Given Integer
'''
number=int(input())
string=str(number)
new_string=""
for i in string:
    if i=='0':
        new_string=new_string+'1'
    else:
        new_string=new_string+i
print(new_string)'''

#40. Addition of two fractions
# Input numbers
'''
n1 = int(input('Enter numerator 1: '))
n2 = int(input('Enter numerator 2: '))
d1 = int(input('Enter denominator 1: '))
d2 = int(input('Enter denominator 2: '))

# Function to calculate HCF (GCD)
def get_hcf(a, b):
    while b:
        a, b = b, a % b
    return a

# Calculate LCM of the denominators
lcm = (d1 * d2) // get_hcf(d1, d2)

# Calculate the numerators for the addition
numerator_sum = (n1 * (lcm // d1)) + (n2 * (lcm // d2))

# Print the results
print(f"LCM of the denominators: {lcm}")
print(f"Sum of the fractions: {numerator_sum}/{lcm}")

# Simplify the fraction if possible
hcf_numerator = get_hcf(numerator_sum, lcm)
simplified_numerator = numerator_sum // hcf_numerator
simplified_denominator = lcm // hcf_numerator

print(f"Simplified sum of the fractions: {simplified_numerator}/{simplified_denominator}"'''
