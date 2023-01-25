def on_button_pressed_a():
    global Score
    Score += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global Score
    Score = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global Score
    Score += -1
input.on_button_pressed(Button.B, on_button_pressed_b)


Score = 0
while True:
    if Score >= 0:
        basic.show_number(Score)
    else: 
        Score = 0