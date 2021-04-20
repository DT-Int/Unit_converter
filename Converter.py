
def getInputFromUser():
    print("Main Manu => 1-Make conversion 2-Quit")
    mainMenu = int(input("Choose an option from the main menu: "))

    if mainMenu == 1:
        amount = float(input("Enter the amount to be converted: "))
        fromUnit = input("Enter the unit you want to convert from: ")
        toUnit = input("Enter the unit you want to convert to: ")
        return {"mainMenu":mainMenu, "amount":amount, 
                "fromUnit":fromUnit, "toUnit":toUnit}
     
    elif mainMenu == 2:
        return {"mainMenu":mainMenu}


def convertUnit():
    while True:
        userInput = getInputFromUser()
        if userInput.get("mainMenu") == 2:
            break
        amount = userInput.get("amount")
        fromUnit = userInput.get("fromUnit")
        toUnit = userInput.get("toUnit")

        if fromUnit == "meter":
            if toUnit == "feet":
                print(amount * 3.28)
            elif toUnit == "inch":
                print(amount * 39.37)

        elif fromUnit == "feet":
            if toUnit == "meter":
                print(amount * 0.3048)
            elif toUnit == "inch":
                print(amount * 12)
        
        elif fromUnit == "inch":
            if toUnit == "feet":
                print(amount * 0.0833)
            elif toUnit == "meter":
                print(amount * 0.0254)
            
        elif fromUnit == "bit":
            if toUnit == "byte":
                print(amount * 0.125)
            
        elif fromUnit == "byte":
            if toUnit == "bit":
                print(amount * 8)

convertUnit()