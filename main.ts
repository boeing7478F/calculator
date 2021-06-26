input.onButtonPressed(Button.A, function () {
    if (change == 0) {
        counter += 1
        basic.showNumber(counter)
    }
    if (change == 1) {
        _2ndnumber += 1
        basic.showNumber(_2ndnumber)
    }
})
input.onButtonPressed(Button.AB, function () {
    operator += 1
    if (operator == 1) {
        basic.showLeds(`
            . . # . .
            . . # . .
            # # # # #
            . . # . .
            . . # . .
            `)
    } else {
        if (operator == 2) {
            basic.showLeds(`
                . . . . .
                . . . . .
                # # # # #
                . . . . .
                . . . . .
                `)
        } else if (operator == 3) {
            basic.showLeds(`
                . . # . .
                . . . . .
                # # # # #
                . . . . .
                . . # . .
                `)
        }
        if (operator == 4) {
            basic.showLeds(`
                # . . . #
                . # . # .
                . . # . .
                . # . # .
                # . . . #
                `)
        }
    }
})
input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
    change += 1
    if (change == 2) {
        if (operator == 1) {
            basic.showNumber(counter + _2ndnumber)
        } else if (operator == 2) {
            basic.showNumber(counter - _2ndnumber)
        } else if (operator == 3) {
            basic.showNumber(counter / _2ndnumber)
        } else if (operator == 4) {
            basic.showNumber(counter * _2ndnumber)
        }
    }
})
let change = 0
let operator = 0
let _2ndnumber = 0
let counter = 0
counter = 0
_2ndnumber = 0
operator = 0
change = 0
