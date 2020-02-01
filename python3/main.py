print("Please insert a number to convert kilometers into miles")


while True:
    kilometers = float(input("Please insert kilometer: "))
    mile_converter = kilometers * 0.62137119
    print("You entered {}, this is {} miles".format(kilometers, mile_converter))

    continuing_game = raw_input("Do you want to continue? Pleas enter yes or no: ")
    print(continuing_game)
    if continuing_game == "yes":
        continue
    else:
        break


