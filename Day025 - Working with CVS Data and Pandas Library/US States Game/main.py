import turtle
from turtle import Turtle,Screen
import pandas as pd

image = "blank_states_img.gif"
screen = Screen()
screen.title("U.S States Game")
screen.addshape(image)
turtle.shape(image)
turtle_to_write = Turtle()
#variable to keep track of score
#score = 0 - from previus implementation
data = pd.read_csv("50_states.csv")
#print(data)
list_of_states = data.state.tolist()
#print(list_of_states)
#list_of_xcor = data.x.tolist()
#print(list_of_xcor)
#list_of_ycor = data.y.tolist()
#print(list_of_ycor)
states_already_guessed = []

while len(states_already_guessed) < 50:
    answer_state = (screen.textinput(title=f"{len(states_already_guessed)}/50 States Correct",prompt="What's another "
                                                                                                     "state's name? "
                                                                                                     "")).title()
    if answer_state == "Exit":
        # states_to_learn.csv
        missing_states = [state for state in list_of_states if state not in states_already_guessed]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in list_of_states and answer_state not in states_already_guessed:
        states_already_guessed.append(answer_state)
        #score += 1 from previus implemetation
        #state_index = list_of_states.index(answer_state)- previus solution with lists
        turtle_to_write.penup()
        turtle_to_write.hideturtle()
        state_data = data[data.state == answer_state]
        turtle_to_write.goto(int(state_data.x), int(state_data.y))
        turtle_to_write.write(answer_state)
        #alternativa
        #turtle_to_write.write(state_data.state.item())






