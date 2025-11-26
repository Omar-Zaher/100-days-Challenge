import turtle

t1 = turtle.Turtle()
print(t1)
t1.shape("turtle")
t1.color("Green")
my_screen = turtle.Screen()
#print(my_screen.canvheight)
my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()


table.add_column("Numbers",[1,2,3,4,5])
table.add_column("Coffee", ["Espresso","Americano","Latte","Cappuccino","Mocha"])

print(table)