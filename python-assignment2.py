# QUESTION NO.1

x1="Python is a case sensitive language"
# (a) Length of the input string.
print(len(x1))
# (b)Reversed order of the string in one line code.
print(x1[::-1])
# (c) “a case sensitive” stored in new string.
x2=(x1[10:27])
print(x2)
# (d) “a case sensitive” replaced by “object oriented”.
print(var1.replace("a case sensitive","object oriented"))
# (e) index of substring “a”
print(var1.index("a"))
# (f)white spaces removed from the given input string.
print(var1.replace(" ",""))

# QUESTION NO.2

print("Enter your good name")
x1=input()
print("Hey",v1," Here!")
print("Enter your SID")
x2=int(input())
print("My SID is ",x2)
print("Enter your Branch")
x3=input()
print("Enter your CGPA")
x4=int(input())
print("I am from ",x3,"department and my CGPA is",x4)

# QUESTION NO.3

a=56
b=10
print("The value of","a&b = ",a&b)
print("The value of","a|b = ",a|b)
print("The value of","a^b = ",a^b)
print("The value of","a<<2 = ",a<<2,"\nThe value of","b<<2 = ",b<<2)
print("The value of","a>>2 = ",a>>2,"\nThe value of","b>>4 = ",b>>4)


# QUESTION NO.4

print("Enter any sentence of your choice:-")
x1=input()
if "name" in x1:
    print("Yes")
else:
    print("No")

# QUESTION NO.5

print("This program is used to determine if the three sides entered by the use can form a triangle or not. ")
print("Enter first side of triangle:-")
side1=int(input())
print("Enter second side of triangle:-")
side2=int(input())
print("Enter third side of triangle:-")
side3=int(input())

A=side1<side2+side3
B=side2<side1+side3
C=side3<side2+side1

Result=str(A&B&C)
print("The sides entered by the use can form a triangle?")
Result=Result.replace("True","YES")
Result=Result.replace("False","NO")
print("The Answer is ",Result)

# QUESTION NO.6

a=int(input("Enter the value of a:-"))
b=int(input("Enter the value of b:-"))
c=(a^b)
d=bin(c)
count=0
for i in d[2:]:
    if i=="1":
        count+=1
print(count)
