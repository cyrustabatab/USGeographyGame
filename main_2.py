import turtle
import pandas as pd
import random

file_name = '50_states.csv'
states_to_coordinates = {}
states = []
with open(file_name,'r') as f:
    for i,line in enumerate(f):
        if i == 0:
            continue
        state,x,y = line.split(',')
        state = state.lower()
        states_to_coordinates[state]= (int(x),int(y))
        states.append(state)


screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(725,491)

image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)


random.shuffle(states)
pen = turtle.Turtle()
pen.ht()
pen.speed('fastest')
pen.penup()
font = ('Arial',5,'bold')


marker = turtle.Turtle()
marker.speed('fastest')
marker.shape('circle')
marker.penup()

states_guessed = 0
#guessed_states = set()
win_font = ('Arial',20,'bold')
small_font = ("Arial",5,'normal')

choice = 'yes'
num_states = 50

i= 0
small_states = {'connecticut','rhode island','delaware','maryland'}
current_state = states[i]
if current_state in small_states:
    marker.shapesize(0.3,0.3)
marker.goto(states_to_coordinates[current_state])
previously_small_state =current_state in small_states
while choice != 'no':

    while states_guessed != num_states:

        state = screen.textinput(f"{states_guessed}/50 States Correct","Enter State Name:")
        if state is None or state == 'exit':
            choice = 'no'
            break
        state = state.lower()
        if state == current_state:
            i += 1
            pen.goto(states_to_coordinates[current_state])

            pen.write(state.title(),font=font if current_state not in small_states else small_font)
            if i != 50:
                current_state = states[i]
                if current_state in small_states and not previously_small_state:
                    marker.shapesize(0.3,0.3)
                elif current_state not in small_states and previously_small_state:
                    marker.shapesize(1,1)
            marker.goto(states_to_coordinates[current_state])
            states_guessed += 1

    else:
        pen.goto(0,0)
        pen.color('green')
        pen.write('YOU WIN',font=win_font)
        try:
            choice = screen.textinput("Play Again","Play Again?").lower()
        except:
            choice = None

        while choice not in ('yes','no'):
            try:
                choice = screen.textinput("Play Again","Please type yes or no?").lower()
            except:
                choice = None

        
        if choice == 'yes':
            pen.color('black')
            pen.clear()
            current_state = 1
            states_guessed = 0
            guessed_states.clear()





