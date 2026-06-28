# QUESTION - 1
# name = "ansh"
# age = 21
# print(f"My name is {name} and my age is {age}")

# QUESTION - 2
# user = input("Give me a number :- ")
# print("This is a number given by a user ",user)

# QUESTION - 3
# a = 22

# if a > 15:
#     print("I will do task A")
# else:
#     print("I will do task B")

# QUESTION - 4
# money = int(input("Please provide me a money : "))

# if money == 10 or money < 10:
#     print("I will buy chocobar or nothing else if i don't have enough money")
# else:
#     print("I will buy Mango doli")

# QUESTION - 5
# money = int(input("Provide me a money : - "))

# if money == 10 or money < 10:
#     print("I will buy a chocobar")
# elif money == 20:
#     print("I will buy a Mongo doli")
# else:
#     print("I will buy a cone")

# QUESTION - 6
# num1 = int(input("Give me a number1 : "))
# num2 = int(input("Give me a number2 : "))

# if num1 > num2:
#     print(f"{num1} is greater")
# else:
#     print(f"{num2} is greater")

# QUESTION - 7
# gender = input("Enter your gender : ")

# if gender == "male":
#     print("Hello, Good morning sir!!")
# else:
#     print("Hello, Good morning mam!!")

# QUESTION - 8
# num = int(input("Enter a number : "))

# if num % 2 == 0:
#     print("Number is a even number")
# else:
#     print("Number is a odd number")

# QUESTION - 9
# name = input("Enter you name : ")
# age = int(input("Enter you age : "))

# if age > 18:
#     print(f"Hey {name} you are valid for vote")
# else:
#     print(f"Sorry {name} you are not valid for vote")

# QUESTION - 10
# year = int(input("Enter a year : "))

# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")

# QUESTION - 11
# temp = int(input("Please tell me the freezer temperature : "))

# if temp < 0:
#     print("Freezing cold")
# elif temp == 0 or temp < 10:
#     print("Very cold")
# elif temp == 10 or temp < 20:
#     print("Cold")
# elif temp == 20 or temp < 30:
#     print("Pleasant")
# elif temp == 30 or temp < 40:
#     print("Hot")
# else:
#     print("Very Hot")

# QUESTION - 12
# a = range(1, 20)

# for i in a:
#     print(i)

# QUESTION - 13
# for i in range(20, 51):
#     print(i)

# QUESTION - 14
# for i in range(10, 0, -1):
#     print(i)

# QUESTION - 15
# for i in range(-5, -1):
#     print(i)

# QUESTION - 16
# for i in range(1, 11):
#     print("5 *",i, "=" ,5 * i)

# QUESTION - 17
# a = "ANSH BHARDWAJ"
# for i in range(len(a)):
#     print(a[i])

# QUESTION - 18
# for i in range(1, 21):
#     if i == 15:
#         break
#     else:
#         print(i)

# QUESTION - 19
# for i in range(1, 21):
#     if i == 15:
#         continue
#     else:
#         print(i)

# QUESTION - 20
# n = int(input("Enter a number : "))

# for i in range(n):
#     print("hello world")

# QUESTION - 21
# n = int(input("Enter a number : "))
# for i in range(1,n+1):
#     print(i)

# QUESTION - 22
# n = int(input("Enter a number : "))
# for i in range(n, 0, -1):
#     print(i)

# QUESTION - 23
# n = int(input("Enter a number : "))
# for i in range(n, (n * 10)+1, n):
#     print(i)

# QUESTION - 24
# n = int(input("Enter a number : "))
# sum = 0
# for i in range(n+1):
#     sum = sum + i
# print(sum)

# QUESTION - 25
# n = int(input("Enter a number : "))
# fact = 1
# for i in range(1, n+1):
#     fact = fact * i
# print(fact)

# QUESTION - 26
# n = int(input("Enter a number : "))
# sum = 0
# sum2 = 0
# for i in range(1, n):
#     if i % 2 == 0:
#         sum = sum + i
#     else:
#         sum2 = sum2 + i
# print("The sum of even number in a range is : ", sum)
# print("The sum of odd number in a range is : ", sum2)

# QUESTION - 27
# n = int(input("Enter a number : "))
# for i in range(1, n+1):
#     if n%i == 0:
#         print(i)

# QUESTION - 28
# n = int(input("Enter a number : "))
# sum = 0
# for i in range(1, n):
#     if n % i == 0:
#         sum = sum + i
#         print(i)
# if sum == n:
#     print("Your number is a perfect number")
# else:
#     print("Your number is not a perfect number") 

# QUESTION - 29
# n = int(input("Enter a number : "))
# count = 0
# for i in range(1, n+1):
#     if n % i == 0:
#         count = count + 1
# if count == 2:
#     print("Your number is a prime")
# else:
#     print("Your number is not prime")

# QUESTION - 28
# name = "ANSH"
# b = ""
# for i in range(len(name)-1, -1, -1):
#     b = b + name[i]
# print(b)

# QUESTION - 29
# name = "Akash"
# b = ""
# for i in range(len(name)-1, -1, -1):
#     b = b + name[i]
# if b == name:
#     print("It's a palindrome")
# else:
#     print("It's not a palindrome")

# QUESTION - 30
# a = "sdfsfnihf200232@#$%&"
# char = 0
# dig = 0
# spchr = 0
# for i in a:
#     if i.isdigit():
#         dig+=1
#     elif i.isalpha():
#         char+=1
#     else:
#         spchr+=1
# print(f"Your number of digits are {dig}")
# print(f"Your number of character are {char}")
# print(f"Your number of special character are {spchr}")

# QUESTION - 31
# a = 256
# while a > 0:
#     print(a % 10)
#     a = a // 10

# QUESTION - 32
# a = int(input("Enter a number : "))
# rev = 0
# while a > 0:
#     rev = rev * 10 + a % 10
#     a = a // 10
# print(rev)

# QUESTION - 33
# a = int(input("Enter a number : "))
# copy = a
# rev = 0
# while a > 0:
#     rev = rev * 10 + a % 10
#     a = a // 10
# if copy == rev:
#     print("Your number is palindrome")
# else:
#     print("Your number is not palindrome")

# QUESTION - 34
# import random
# num = random.randint(1, 10)
# tries = 0
# while True:
#     guess = int(input("Please enter a number between 1 and 10 : "))
#     if num == guess:
#         tries += 1
#         print(f"you are right you gussed the number in {tries} tries")
#         break
#     elif num < guess:
#         print("you go to little lower")
#         tries += 1
#     elif num > guess:
#         print("you go to little higher")
#         tries += 1
#     else:
#         print("you guess the wrong number please try again")
#         tries += 1

# QUESTION - 35
# def pallindrome(st):
#     rev = ""
#     for i in range(len(st)-1, -1, -1):
#         rev = rev + st[i]
#     if rev == st:
#         print("Pallindrome")
#     else:
#         print("Not a pallindrome")
# pallindrome("naman")

# QUESTION - 36
# a = [1, 2, 3, 4, 5, 6]

# for i in range(len(a)):
#     print(a[i])

# QUESTION - 37
# a = [-90, 34, -45, 26, 78, -35]

# print("Positive numbers are : ")
# for i in a:
#     if i >= 0:
#         print(i)
# print("Negative numbers are : ")
# for i in a:
#     if i < 0:
#         print(i)

# QUESTION - 38
# a = [1, 2, 3, 4, 5, 6]
# sum = 0
# for i in range(len(a)+1):
#     sum = sum + i
# avg = sum/len(a)
# print(avg)

# a = [1, 2, 3, 4, 5, 6, 547, 384, 3982, 39927720, 29378929, 2799273820, 29702028]
# count = 0
# for i in a:
#     # print(i)
#     count = count + 1
# print(count)

# LARGEST NUMBER FIND IN A LIST
# a = [38, 96, 76, 28, 48, 69]
# largest = a[0]
# index = 0
# for i in range(len(a)):
#     if a[i] > largest:
#         largest = a[i]
#         index = i
# print(f"The largest element {largest} and its index is {index}")        

# SECOND LARGEST NUMBER FIND IN A LIST
# a = [1, 96, 76, 28, 48, 69, 95]
# largest = a[0]
# index = 0
# secLargest = a[0]
# index2 = 0
# for i in range(len(a)):
#     if a[i] > largest:
#         secLargest = largest
#         largest = a[i]
#         index = i
#     elif a[i] > secLargest:
#         secLargest = a[i]
#         index2 = i
# print(f"The largest number is {largest} and its index is {index}")
# print(f"The secong largest number is {secLargest} and its index is {index2}")

# FING LARGEST AND SECOND LARGEST NUMBER IN A NORMAL NUMBER STORED IN A VARIABLE
# a = 100, 299, 39, 104, 95
# largest = a[0]
# sec_largest = a[0]
# for i in a:
#     if i > largest:
#         sec_largest = largest
#         largest = i
#     elif i > sec_largest:
#         sec_largest = i
# print(largest, sec_largest)

# a = [1, 2, 3, 4, 5]
# for i in range(len(a)-1):
#     if a[i] < a[i+1]:
#         continue
#     else:
#         print("Your list is not sorted")
#         break
# else:
#     print("Your list is sorted")

# SETS IN PYTHON
# a = {1, 2, 3, 4, 5}
# a.add(6)
# print(a)
# a.pop()
# print(a)
# a.remove(2)
# print(a)
# a.clear()
# print(a)

# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8}

# s = a.union(b)
# print(s)
# v = a|b # .union() and | both are same (|) this is the short cut of union
# print(v)

# c = a.intersection(b)
# print(c)

# DICTIONARY IN PYTHON
# a = {10:100,20:200,30:300,40:400}
# a[10] = 100 #updateing
# a[50] = 500 #creating
# del a[30] #Deleting
# print(a)

# QUES-1
# d1 = {10:100, 20:200, 30:300}
# d2 = {40:400, 50:500, 60:600}

# for i in d2:
#     d1[i] = d2[i]

# print(d1)

# QUES-2
# d1 = {10:100, 20:200, 30:300}
# sum = 0
# for i in d1:
#     sum = sum + d1[i]
# print(sum)

# QUES-3
# a = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,6,6,7,7,8,8]
# d = {}
# for i in a:
#     if i in d.keys():
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)

# QUES-4
d1 = {10:100,20:200,30:300,40:300}
d2 = {40:400,50:500,60:600,70:700}

for i in d2:
    if i in d1.keys():
        d1[i] += d2[i]
    else:
        d1[i] = d2[i]
print(d1)