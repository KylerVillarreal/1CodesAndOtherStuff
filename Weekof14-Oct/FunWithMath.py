# Starting off
print(22 / 7)
print(355 / 113)
import math

print(9801 / (2206 * math.sqrt(2)))
def archimedes(numSides):
    innerAngleB = 360.0 / numSides
    halfAngleA = innerAngleB / 2
    oneHalfSideS = math.sin(math.radians(halfAngleA))
    sideS = oneHalfSideS * 2
    polygonCircumference = numSides * sideS
    pi = polygonCircumference / 2
    return pi


print(archimedes(8))
print(archimedes(16))

for sides in range(8, 100, 8):
    print(sides, archimedes(sides))

# experiment with the loop above alongside the actual value of pi. How many sides does it take to make the two close?

# Accumulators

acc = 0
for x in range(1, 6):
    acc = acc + x

print(acc)

# compute the sum of the first 100 even numbers
# compute the sum of the first 50 odd numbers
# compute the average of the first 100 odd numbers
# write a function that returns the average of the first N numbers, where N is a parameter
# write a function called factorial that computes the product of the first N numbers, where N is a parameter
# Each number in the Fibonacci sequence is the sum of the previous two numbers.
#  The first two numbers in the sequence are 1 and 1. Compute the 10th Fibonacci number
# write a function to compute the Nth Fibonacci number, where N is a parameter
#  You may assume that N will be greater than or equal to 3.

acc = 0
for k in range(1, 100):
    acc = acc + k

print(acc)

acc = 0
for q in range(1,50):
    acc = acc + q

print(acc)


# A Monte Carlo Simulation

import random

print(random.random())

# Boolean expressions
# >  greater than
# >= greater than or equal to
# < less than
# <= less than or equal to
# == the same as [equal to]
# != NOT equal to

catWeight = 15
print(catWeight != 15)
tableWeight = 30

# compound Boolean operators
# and (both must be true or it will all be false if one is false)
# or  (if one is true, it is considered true)
# not (opposite, think like it's a negative)

print(not catWeight < 20)


# Decision making -- Selection statements
a = 5
b = 10
c = 75

if a <= b :
    c = 45

print(c)

if a > b:
    c = 45
    if b > c:
        a = 25
    else:
        a = -25
else:
    c = 1050
    if b == a:
        c = 25


print(a, b, c)


d = 55
e = 72
f = 44
ans = 0

if d > e:
    ans = 12
else:
    if d == e:
        ans = 50
    else:
        if f < d * e:
            ans = 100
        else:
            ans = 75
print(ans)

def showmontePi(numDarts):
    scn = turtle.Screen()
    t = turtle.Turtle()

    scn.setworldcoordinates(-2, -2, 2, 2)

    t.penup()
    t.goto(-1, 0)
    t.pendown()
    t.goto(1, 0)

    t.penup()
    t.goto(0, 1)
    t.pendown()
    t.goto(0, -1)

    inCircle = 0
    t.penup()
    for i in range(numDarts):
        x = random.random()
        y = random.random()

        distance = math.sqrt(x**2 + y**2)

        t.goto(x, y)
        if distance <= 1:
            inCircle = inCircle + 1
            t.color("blue")
        else:
            t.color("red")

        t.dot()

    pi =inCircle / numDarts * 4
    scn.exitonclick()
    return pi
import turtle
showmontePi(1000)

print(montePi(10000))

# My task:
# Modify the simulation to plot points in the entire circle
# You will have to adjust the calculated value of pi accordingly.



