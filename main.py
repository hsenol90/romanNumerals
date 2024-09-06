import myFuncs
import math

while True:
    number1 = int(input("Enter a number:"))

    onesPlaceOfRoman = myFuncs.Place(1, number1 % 10)
    tensPlaceOfRoman = myFuncs.Place(2, math.floor(number1 / 10) % 10)
    hundredsPlaceOfRoman = myFuncs.Place(3, math.floor(number1 / 100) % 10)
    thousandsPlaceOfRoman = myFuncs.thousandsPlace(math.floor(number1 / 1000))

    print(
        "Result: {}".format(
            thousandsPlaceOfRoman
            + hundredsPlaceOfRoman
            + tensPlaceOfRoman
            + onesPlaceOfRoman
        )
    )
