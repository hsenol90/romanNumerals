def Place(digit, number):

    if digit == 1:
        firstNum = "I"
        secondNum = "V"
        thirdNum = "X"

    elif digit == 2:
        firstNum = "X"
        secondNum = "L"
        thirdNum = "C"

    elif digit == 3:
        firstNum = "C"
        secondNum = "D"
        thirdNum = "M"

    output = ""
    if number == 1:
        output = firstNum
    elif number == 2:
        output = 2 * firstNum
    elif number == 3:
        output = 3 * firstNum
    elif number == 4:
        output = firstNum + secondNum
    elif number == 5:
        output = secondNum
    elif number == 6:
        output = secondNum + firstNum
    elif number == 7:
        output = secondNum + 2 * firstNum
    elif number == 8:
        output = secondNum + 3 * firstNum
    elif number == 9:
        output = firstNum + thirdNum
    else:
        output = ""
    return output


def thousandsPlace(number):

    thousand = "M"
    fourThousand = "I̅V̅"

    output = ""
    if number == 1:
        output = thousand
    elif number == 2:
        output = 2 * thousand
    elif number == 3:
        output = 3 * thousand
    elif number == 4:
        output = fourThousand
    else:
        output = ""
    return output
