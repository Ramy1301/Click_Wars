input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    Score += 1
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    Score = 0
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    Score += -1
})
let Score = 0
while (true) {
    if (Score >= 0) {
        basic.showNumber(Score)
    } else {
        Score = 0
    }
    
}
