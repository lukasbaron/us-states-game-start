import turtle
import pandas

screen = turtle.Screen()
state = turtle.Turtle()

screen.title("US game quiz")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")

correct_answers = []
all_states = data["state"].to_list()


def set_text():
    state.hideturtle()
    state.penup()
    state.goto(x_pos, y_pos)
    state.write(answer_state)


game_on = True
while game_on:
    answer_state = screen.textinput(title=f"{len(correct_answers)}/50 States correct", prompt="What is another state name?")
    answer_state = answer_state.title()
    correct = data[data["state"] == answer_state]
    if answer_state not in correct_answers and answer_state in all_states:
        correct_answers.append(answer_state)
    else:
        continue
    x_pos = int(correct["x"])
    y_pos = int(correct["y"])
    set_text()

    if len(correct_answers) == 50:
        print("Well done")
        game_on = False





screen.exitonclick()