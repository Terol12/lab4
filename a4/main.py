import re


def IsValidNumber(cardNumber):
    return cardNumber.isdigit() and len(cardNumber) in [13, 15, 16]


def getCheckSum(cardNumber):
    checkSum = 0
    for i in range(len(cardNumber) - 2, -1, -2):
        product = int(cardNumber[i]) * 2
        if product > 9:
            checkSum += product - 9
        else:
            checkSum += product

    for i in range(len(cardNumber) - 1, -1, -2):
        checkSum += int(cardNumber[i])

    return checkSum


def isValidCheckSum(checkSum):
    return checkSum % 10 == 0


def getCardType(cardNumber):
    if (len(cardNumber) == 13 or len(cardNumber) == 16) and cardNumber.startswith("4"):
        return "Visa"
    elif len(cardNumber) == 15 and (cardNumber.startswith("34") or cardNumber.startswith("37")):
        return "American Express"
    elif len(cardNumber) == 16 and re.match(r'^5[1-5]', cardNumber):
        return "Master Card"
    else:
        return "Invalid"


cardNumber = input("Enter Card Number: ").strip()
if IsValidNumber(cardNumber):
    if isValidCheckSum(getCheckSum(cardNumber)):
        print("Valid")
        card_type = getCardType(cardNumber)
        if card_type != "Invalid":
            print(card_type)
        else:
            print("Unknown card type")
    else:
        print("Invalid checksum")
else:
    print("Invalid card number format")