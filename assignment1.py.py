#Name :Yash Vishwari
#Enrollment No:0176EC231037
#Batch :6 (MTF) 
#Batch time: 12:10pm - 1:50pm 

#Basic If–Else Problems:

#Question 1: Write a program to check whether a number is positive, negative, or zero.

num = int(input("Enter a Valid Number :"))

if num>0:
    print(f"The Number {num} is positive")

elif num<0:
    print(f"The Number {num} is negative")

else :
     print("The Number is Zero")

#Question 2:Write a program to check whether a number is even or odd

num = int(input("Enter a Valid Number :"))

if num%2 ==0:
    print(f"The Number {num} is even")

else :
     print(f"The Number {num} is odd")

#Question 3:Write a program to check if a given year is a leap year or not     

year = int(input("Enter a Valid Year: "))

if (year %400 ==0)or( year %100 != 0 and year%4 ==0 ) :
    print(f"Given Year {year} is a leap year")

else:
     print(f"Given Year {year} is not a leap year")    

#Question 4:Write a program to find the greatest of two numbers.

num1 = int(input("Enter the First Number :"))
num2 = int(input("Enter the Second Number :"))

if num1>num2 :
    print(f"The First Number {num1} is the Greatest")

elif num1<num2 :
    print(f"The Second Number {num2} is the Greatest")

else :
    print("Both Numbers are equal")    

#Question 5:Write a program to check whether a person is eligible to vote (age >= 18)

age =int(input("Enter the person's age :"))

if age>=18:
    print("The person is eligible to vote")

else :
      print("The person is not eligible to vote")
   
#Question 6:Write a program to check whether a given character is a vowel or consonant.
char = input("Enter a Valid character :").lower()[0]

if  char =='a' or char =='e' or char =='i' or char =='o' or char =='u':
    print("Given character is a vowel")

else:
    print("Given character is a consonant")

#Question 7:Write a program to check if a number is divisible by 5

num = int(input("Enter a Valid Number :"))
if num%5 ==0:
    print(f"Given number {num} is divisible by 5")

else:
    print(f"Given number {num} is not divisible by 5")    

#Question 8:Write a program to determine whether a given number is a single-digit, two-digit, or more than two-digit.

num = int(input("Enter a Valid Number :"))   
if num>-10 and num<10 :
    print(f"The number {num} is a single digit number")  

elif num>-100 and num<100 :
    print(f"The number {num} is a two digit number")      

else:
    print(f"The number {num} is a more than two digit number")    


#Question 9:Write a program to check whether a student has passed or failed (passing marks = 40)

marks = int(input("Enter Student's marks :"))

if marks>=40:
    print("The Student has passed")

else:
    print("The Student has failed")

#Question 10:Write a program to find whether the entered number is a multiple of both 3 and 7.    

num = int(input("Enter a Valid Number :"))
if num%3 ==0 and num%7 ==0:
    print(f"Given number {num} is a multiple of both 3 and 7")

else:
     print(f"Given number {num} is not a multiple of both 3 and 7")





#Ladder If & Nested If:

#Question 11:Write a program to find the greatest among three numbers
num1 = int(input("Enter the First Number :"))
num2 = int(input("Enter the Second Number :"))
num3 = int(input("Enter the Third Number :"))

if num1>num2 and num1>num3:
    print(f"First Number {num1} is the greatest")

elif num2>num1 and num2>num3:
    print(f"Second Number {num2} is the greatest")    

elif num3>num1 and num3>num2:
    print(f"Third Number {num3} is the greatest")    

else:
    print("All three numbers are equal")   



#Question 12:Write a program to classify a person based on age: Child (<13), Teenager (13-19), Adult (20-59), Senior (60+

age =int(input("Enter the person's age :"))

if age<13:
    print("Child")

elif age>=13 and age<=19:
    print("Teenager")

elif age>=20 and age<=59:
    print("Adult")

else:
    print("Senior")

#Question 13:Write a program to assign grades based on marks:90-100: A,75-89: B, 50-74: C, 35-49: D, <35: Fail.

marks = int(input("Enter the marks :"))
if marks>=90 :
    print("Grade A")

if marks>=75 and marks<=89 :
    print("Grade B")

if marks>=50 and marks<=74 :
    print("Grade C")

if marks>=35 and marks<=49 :
    print("Grade D")

else:
    print("Fail")

#Question 14:Write a program to check the type of triangle (equilateral, isosceles, or scalene) based on sides.

side1 = int(input("Enter the first side of triangle :"))
side2 = int(input("Enter the second side of triangle :"))
side3 = int(input("Enter the third side of triangle :"))

if side1 ==side2 ==side3:
    print("Triangle is an Equilateral triangle")

if (side1 ==side2 and side1 !=side3) or (side1 ==side3 and side1 != side2) or (side2 ==side3 and side2!= side1):
    print("Triangle is an Isosceles triangle")

else :
    print("Triangle is an Scalene triangle")


#Question 15:Write a program to check if a character is uppercase, lowercase, digit, or special symbol

char = input("Enter the Character :")[0]

if ord(char) >=65 and ord(char) <=90:
    print("Given character is a Uppercase character")
    
elif ord(char) >=97 and ord(char) <=122:
    print("Given character is a Lowercase character")

elif ord(char) >=48 and ord(char) <=57:
    print("Given character is a Digit")

else:
    print("Given character is a special symbol")



#Question 16:Write a program to calculate electricity bill based on units:Up to 100 units: ₹5 per unit,101–200 units: ₹7 per unit,Above 200 units: ₹10 per unit

electricityunits = int(input("Enter the electricity units : "))

if electricityunits<=100:
    bill = electricityunits*5
    print(f"Electricity bill is {bill} Rs")

elif electricityunits<=200:
    bill = (100*5)+(electricityunits-100)*7
    print(f"Electricity bill is {bill} Rs")

else:
    bill = (100*5)+(100*7)+(electricityunits-200)*10
    print(f"Electricity bill is {bill} Rs")


#Question 17:Write a program to determine the largest of four numbers using nested if

num1 = int(input("Enter the First Number :"))
num2 = int(input("Enter the Second Number :"))
num3 = int(input("Enter the Third Number :"))
num4 = int(input("Enter the Fourth Number :"))


if num1>num2:
    if num1>num3:
        if num1>num4:
            print(f"Number {num1} is the largest")
        else:
            print(f"Number {num4} is the largest")

    else:
        if num3>num4: 
            print(f"Number {num3} is the largest")       

        else:
            print(f"Number {num4} is the largest")

elif num2>num1:
    if num2>num3:
        if num2>num4:
            print(f"Number {num2} is the largest")            
        else:
            print(f"Number {num4} is the largest")               

    else:
        if num3>num4: 
            print(f"Number {num3} is the largest")       

        else:
            print(f"Number {num4} is the largest")

elif num3>num4:
    if num3>num1:
         print(f"Number {num3} is the largest")     
    else:
        print(f"Number {num1} is the largest")

elif num4>num3:
    if num4>num1:
         print(f"Number {num4} is the largest")     
    else:
        print(f"Number {num1} is the largest")


else:
    print("All Four Numbers are equal")

#Question 18:Write a program to check if a given year is a century year and also a leap year
year = int(input("Enter a Valid Year: "))

if year %100 ==0:
    if year%400 ==0:
        print(f"Given year {year} is a century year and also a leap year")
        

else:
     print(f"Given year {year} is not an year which is both a century year and a leap year")




#Question 19:Write a program to classify BMI value: Underweight (<18.5), Normal (18.5-24.9), Overweight (25-29.9),Obese (30+)

bmi = float(input("Enter BMI value :"))
if bmi<18.5:
    print("Underweight")

elif bmi>=18.5 and bmi<=24.9:
    print("Normal")

elif bmi>=25 and bmi<=29.9:
    print("Overweight")

else:
    print("Obese")


#Question 20:Write a program to display the smallest number among three using nested if

num1 = int(input("Enter the First Number :"))
num2 = int(input("Enter the Second Number :"))
num3 = int(input("Enter the Third Number :"))

if num1<num2:
    if num1<num3:
        print(f"Number {num1} is the smallest")
    else:
        print(f"Number {num3} is the smallest")

elif num2<num1:
    if num2<num3:
        print(f"Number {num2} is the smallest") 
    else:
        print(f"Number {num3} is the smallest")
              
elif num3>num1:
    print(f"Number {num1} is the smallest")

elif num3<num1:
    print(f"Number {num3} is the smallest")

else:
    print("All Three Numbers are equal")





#For Loop Problems:

#Question 21:Write a program using a for loop to print all Armstrong numbers between 100 and 999. (Armstrong number:sum of cubes of digits equals the number itself. Example: 153 => 1³+5³+3³ = 153).
start = 100
end = 999
ans =[]

for i in range(start,end+1):
    sum =0
    num =i
    for j in range(0,3):
        dig = i%10
        sum+=(dig**3)
        i//=10

    if sum == num:
        ans.append(num)
    
    
print(f"All Armstrong numbers between {start} and {end} \n {ans} ")


#Question 22:Write a program to generate and display the first n prime numbers using a for loop

n= int(input("Enter the value of n :"))
ans =[]
start =2
for i in range (0,n):
    isprime =True
    j =2
    
    while j*j<=start:
        if start %j ==0:
            start+=1
            j=2
 
        else:
            j+=1
   
    ans.append(start)
    start +=1    
print(f"First {n} prime numbers are \n {ans}")

#Question 23:Write a program to display all numbers from 1 to 500 that are divisible by 3, but the sum of their digitsshould not exceed 10.
ans =[]
start =1
end = 500
for i in range(start,end+1):
    if i%3 ==0:
        num =i
        dig =0
        if i<10:
            dig =1
        elif i<100:
            dig =2
        else:
            dig =3 
        sum =0;           
        for j in range(0,dig):
            sum += i%10
            i//=10

        if sum<=10:
            ans.append(num)

print(f"All numbers from 1 to 500 that are divisible by 3, but the sum of their digits not exceed 10 are \n {ans}")

#Question 24:Write a program using a for loop to print a pyramid of stars (*) of height n. Example for n=4:
n= int(input("Enter the value of n :"))
for i in range(0,n):
    for j in range(0,n-(i+1)):
        print("  " ,end ="")
    for j in range(0,(i*2)+1):
        print("* ",end ="")    
    print()


#Question 25:Write a program to accept a string and check whether it is a pangram (contains all 26 alphabets at least once)using a for loop.
str = input("Enter a String:").lower()
totalalphabets =[]

for ch in str:
    if ch not in totalalphabets:
        totalalphabets.append(ch)

if len(totalalphabets) ==26:
    print("Given String is a pangram")

else:
    print("Given String is not a pangram")

#Question 26:Write a program using a for loop to print all twin primes between 1 and 100. (Twin primes: pairs of primenumbers with a difference of 2, e.g., (3,5), (11,13)).

start =1
end =100
prev =-1
ans =[]

for i in range(start+1,end+1):
    isprime = True

    for j in range(2,int(i**0.5)+1):
        if i%j ==0:
            isprime =False
            break        
    
    if isprime:
        if prev !=-1 and i-prev ==2: 

            ans.append([prev,i])            
        prev =i    
print(f"All twin prime numbers between {start} and {end}  \n{ans}")

#Question 27:Write a program that accepts a number from the user and prints whether it is a Harshad number (numberdivisible by the sum of its digits) using a for loop
num = int(input("Enter a Valid Number :"))
dummy = num
sum =0
digits =0
for i in range(0,num):
    if dummy ==0:
        break
    digits+=1
    dummy //=10
dummy = num
for i in range(0,digits):
    sum +=dummy%10
    dummy //=10

if num !=0 and num%sum ==0:
    print(f"Given number {num} is a Harshad number")

else:
    print(f"Given number {num} is not a Harshad number")


#Question 28:Write a program to generate Pascal’s Triangle up to n rows using a for loop.

n= int(input("Enter the number of rows:"))

for r in range(1,n+1):
    element =1 
    for j in range(0,n-r):
        print("  ",end="")
    for c in range(0,r):
        if c ==0 or c== r-1 :
            print("1   ",end ="")
        else:
            element *= ((r-c)/c)
            entry =int(element)
            print(f"{entry}   " ,end ="")

    print()

#Question 29
n= int(input("Enter the value of n :"))
seriessum =0
for i in range(1,n+1):
    seriessum += (i**2)
print(f"Sum of the series is {seriessum}")


#Question 30:Write a program that accepts a number from the user and prints whether it is a Strong number (sum of factorials of digits = number itself) using a for loop. Example: 145 => 1! + 4! + 5! = 145.
num = int(input("Enter a Valid Number :"))
digits =0
dummy =num
sum =0
for i in range(0,num):
    if dummy ==0:
        break
    digits += 1
    dummy //=10

dummy = num

for i in range(0,digits):
    ele =dummy%10
    dummy//=10
    fact =1
    for no in range(2,ele+1):
        fact *= no
    sum +=fact

if sum == num:
    print(f"Given Number {num} is a Strong number")

else :
      print(f"Given Number {num} is not a Strong number")  




# While Loop Problems:

#Question 31:Write a program using a while loop to find the reverse of a number and check if the reversed number is prime. Example: Input = 73 → Reverse = 37 → Prime
num = int(input("Enter a Valid Number :"))
reverse=0
while num>0:
    digit =num%10
    num //=10
    reverse = (reverse*10) +digit 
i=1
while num>=i**2:
    if num %i ==0:
        print(f"The reversed num {reverse} is not a prime number")

print(f"The reversed num {reverse} is a prime number")



#Question 32:Write a program that continues to accept numbers from the user until the sum of digits of all numbers entered becomes greater than 100.
sum =0
while sum<=100:
    num =int(input("Enter a Valid Number :"))
    digits =0
    dummy =num
    while dummy>0:
        digits +=1
        dummy//=10

    while digits>0:
        sum += num%10
        num//=10
        digits-=1

print(f"Sum of digits ={sum}")


#Question 33:Write a program using a while loop to check whether a number is a Duck number (a number containing zero but not starting with zero, e.g., 202, 1203).
num =int(input("Enter a Valid Number :"))
digits =0
dummy =num
containzero =False
while dummy>0:
    ele = dummy%10
    if ele ==0:
        break
    dummy//=10
if dummy>0:
    print(f"Given Number {num} is a duck number") 
else:
    print(f"Given Number {num} is not a duck number") 
    



#Question 34:Write a program using a while loop to accept a number and check if it is a Happy number. (A number is happy if repeatedly replacing it with the sum of squares of its digits eventually reaches 1). Example: 19 is a happy number.

num = int(input("Enter a number :"))
original =num
fast =num
slow =num


while slow!=1:
    sum =0
    dummy =slow
    while dummy>0:
        digit = dummy%10
        sum += (digit**2)
        dummy //=10
    slow = sum
    dummy = fast
    sum =0
    while dummy>0:
        digit = dummy%10
        sum += (digit**2)
        dummy //=10
    fast =sum
    dummy =fast
    sum =0
    while dummy>0:
        digit = dummy%10
        sum += (digit**2)
        dummy //=10
    fast =sum

    if fast == slow :
        break
   

if slow==1  :
    print(f"Given number {original} is a happy number")

else:
    print(f"Given number {original} is not a happy number")    

#Question 35:Write a program using a while loop to find the largest prime factor of a given number

num = int(input("Enter a Valid Number :"))
i=2
largestprimefactor =-1
while i <=num/2:
    if num%i ==0:
        isprime =True
        j =2
        while j*j<=i:
            if i%j ==0:
                isprime =False
                break
        if isprime:
            largestprimefactor = i            
    i+=1

print(f"Largest Prime factor of {num} is {largestprimefactor}")    

#Question 36:Write a program to repeatedly accept a string from the user until the string entered is a palindrome

while True:
    str = input("Enter a String :").strip()
    end = len(str)-1
    start =0
    ispalindrome =True
    while start<=end:
        if str[start] !=str[end]:
            ispalindrome = False
            break

        start+=1
        end-=1

    if ispalindrome:
        print(f"Given String {str} is a palindrome")  
        break
    else:
        print(f"Given String {str} is not a palindrome")    


#Question 37:Write a program using a while loop to compute the sum of digits of a number until the result becomes a single-digit number (Digital root). Example: 9875 => 9+8+7+5=29 => 2+9=11 => 1+1=2.

num = int(input("Enter a number :"))
while num>=10:
    dummy =num
    sum =0
    while dummy>0:
        digit = dummy%10
        sum += (digit)
        dummy //=10

    num = sum

print(f"Final Single digit number {num}")

#Question 38:. Write a program using a while loop to generate the Collatz sequence for a given number. (Rule: If n is even=> n/2, if odd => 3n+1. Continue until n=1).
num = int(input("Enter a number :"))
sequence =[]
dummy = num
while dummy !=1:
    sequence.append(dummy)
    if dummy %2 ==0:
        dummy //=2

    else:
        dummy = (3*dummy)+1
sequence.append(dummy)

print(f"Collatz sequence of {num} \n {sequence}")

#Question 39:Write a program using a while loop to accept a number and check whether it is a Kaprekar number.(Kaprekar number: if square of the number can be split into two parts whose sum equals the number.Example: 45²=2025 => 20+25=45)

num = int(input("Enter a number :"))
sqr = num**2
iskaprekar = False
part1 =0
part2 =0
digits =[]
dummy = sqr
while dummy>0:
    digits.append(dummy%10)
    dummy //=10
digits.reverse()
j=1
while j<len(digits):
    part1=0
    part2 =0
    for i in range(0,j):
        part1 = (part1*10)+digits[i]

    for i in range(j,len(digits)):
        part2 = (part2*10)+digits[i]    
    
    if part1+part2 == num:
       
        iskaprekar = True
        break
    j+=1
   
if iskaprekar ==True or num ==1:
    print(f"Given number {num} is a Kaprekar number")

else:
     print(f"Given number {num} is not a Kaprekar number")    

 
#Question 40:Write a program to simulate an ATM machine using a while loop where a user can:
#• Check balance
#• Deposit money
#• Withdraw money (only if balance is sufficient)
#• Exit
#Continue until the user chooses to exit.

balance = 0 
while True:
    print("--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice = int(input("Enter a valid choice : "))
    if choice <1 or choice >4:
        print("Invalid Choice Please Enter a Valid Choice")
        continue
    elif choice == 1:
        print(f"Your current balance is:{balance}Rs")
    
    elif choice == 2:
        amount = float(input("Enter amount to deposit  Rs:"))
        if amount > 0:
            balance += amount
            print(f"Rs{amount} deposited successfully.")
        else:
            print("Invalid amount. Deposit must be positive.")
            continue

    elif choice == 3:
        amount = float(input("Enter amount to withdraw: $"))
        if amount <= balance and amount>0:
            balance -=amount
            print(f"Rs {amount} withdrwan successfully")

    else:
        print("Thank you for using the ATM. Goodbye!")
        break
    













