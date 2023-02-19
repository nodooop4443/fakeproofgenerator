# name = "nodo"
# surname = "gulbiani"

# ammount = name.count("o")
# equal = surname.count("i")

# print(ammount)
# print(equal)
# print(ammount + equal)

# from turtle import *

# speed(1000)
# color("cyan")
# bgcolor("black")
# forward(200)


#while ციკლი

# i = 9

# while i < 30:
#     i  += 1
#     print(i)

# while b > 0:
#     left(b)
#     forward(b * 3)
#     b = b - 1


# i=0

# while i < 5:
#     print("youaredumb")
#     i += 2
#     print("youarestupid")


# name = "nika keshelava"

# i  = 0

# while i < 5:
#     print(name[i])
#     i += 1




# FOR ციკლი

# for i in range(1, 10, 1):
#     print(i)

# name = "nodo gulbiani"
# for i in name:
#     print(i)


# temps_str = ""

# my_list = ["q", "w", "g", "y"]

# for element in my_list:
#     temps_str += element
    
# print(temps_str)

  
# temp_num = 0
# numbers = [10, 20, 60, 80]

# for equal in numbers:
#     temp_num += equal
# print(temp_num)



# username = "nodo gulbiani"

# i = 0
# for char in username:
#     if char != " ":
#         if char in "aeiou":
#             print("ხმოვანი detected at position: ",char)
#         else:
#             print("თანხმოვანი detected at position: ", char)    
#     i += 1


# a = 5

# for i in range(a):

#     print(1 == 3)


# name = "nodo"

# print(len(name) + 3)

from turtle import *

speed(30)
width(7)
color("red")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

begin_fill()
forward(75)
left(90)
color("purple")
forward(100)
right(90)
forward(55)
right(90)
forward(100)
end_fill()

penup()
goto(200, 200)
pendown()
color("green")

begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

begin_fill()
penup()
goto(140, 120)
color("yellow")
pendown()
right(150)
forward(60)
right(90)
forward(40)
right(90)
forward(60)
right(90)
forward(40)
end_fill()

begin_fill()
penup()
goto(30, 118)
color("cyan")
pendown()
right(90)
forward(60)
right(90)
forward(40)
right(90)
forward(60)
right(90)
forward(40)
end_fill()



exitonclick()