#1) Returns sum of numbers if its greater than 20.
def sum20(a:int,b:int) -> int:
    total: int = a+b
    if total <=20:
        return a,b
    else:
        return total

print("Sum of 5 and 16 is: ",sum20(5,16))

#2) Returns area of circle
import math
def area_of_circle(radius: float) -> float:
    area: float =  math.pi * radius * radius
    return area
print("Area of Circle with radius 4.5 is: ",area_of_circle(4.5))

#3) Returns greater number
print("Lets find greater number between these two ->")
a = input("Enter a number: ")
b = input("Enter another number: ")
def greater_number(a: int, b: int) -> int:
    greaterNumber = max(a,b)
    return greaterNumber

print(f"Greater Number between {a} and {b} is: ",greater_number(a,b))

#4) Returns Greater number among three
def greater_number_three(a: int, b: int,c: int) -> int:
    greaterNumber = max(a,b,c)
    return greaterNumber

print("Greater number between 12,32,29 is: ",greater_number_three(12,32,29))

#6) Returns Factorial form of a number
def factorial_of_number(n: int) -> int:
    return math.factorial(n)

print("Factorial for number 5 is: ",factorial_of_number(5))

#7) Returns Fibonacci series upto a given number
def fibonacci_series(n: int) -> None:
    start,end = 0,1
    while start <= n:
        print(start, end=' ')
        start, end = end, start+end

print("Fibonacci Series of 34 -> ", end='')
fibonacci_series(34)