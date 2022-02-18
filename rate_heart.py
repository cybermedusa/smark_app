import turtle
import pandas as pd
from smark_app import db_connection

# Average application rate
rate_df = pd.read_sql('select * from rates', con=db_connection)
avg_rate = round(rate_df['value'].mean(), 2)
# print(avg_rate)

turtle_obj = turtle.Turtle()
turtle_obj.color('red')
turtle_obj.width(2)

def curve():
    for i in range(200):
        turtle_obj.right(1)
        turtle_obj.forward(1)

def heart():
    turtle_obj.left(140)
    turtle_obj.forward(113)
    curve()
    turtle_obj.left(120)
    curve()
    turtle_obj.forward(50)

def text():
    turtle_obj.up()
    turtle_obj.setpos(-50, 89)
    turtle_obj.down()
    turtle_obj.write("7.5 / 10", font=('Verdana', 24, 'bold'))

heart()
text()
turtle.done()

