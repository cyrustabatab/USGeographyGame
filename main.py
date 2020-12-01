import turtle
import pandas as pd

file_name = '50_states.csv'
states_to_coordinates = {}
with open(file_name,'r') as f:
    for i,line in enumerate(f):
        if i == 0:
            continue
        state,x,y = line.split(',')
        states_to_coordinates[state.lower()]= (int(x),int(y))




screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(725,491)

image = 'blank_states_img.gif'
screen.addshape(image)

def get_mouse_click_coor(x,y):
    print(x,y)
turtle.shape(image)
turtle.onscreenclick(get_mouse_click_coor)
'''
pen = turtle.Turtle()
pen.ht()
pen.speed('fastest')
pen.penup()
font = ('Arial',5,'bold')

states_guessed = 0
guessed_states = set()
win_font = ('Arial',20,'bold')

choice = 'yes'
num_states = 50
while choice != 'no':
    while states_guessed != num_states:

        state = screen.textinput(f"{states_guessed}/50 States Correct","What's another state?")
        if state is None or state == 'exit':
            choice = 'no'
            break
        state = state.lower()
        if state in states_to_coordinates:
            pen.goto(states_to_coordinates[state])
            pen.write(state.title(),font=font)
            states_guessed += 1
            guessed_states.add(state)
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




missed_states = [state for state in states_to_coordinates if state not in guessed_states]

new_data = pd.DataFrame(missed_states)
new_data.to_csv('states_to_learn.csv')
    
'''

screen.mainloop()









