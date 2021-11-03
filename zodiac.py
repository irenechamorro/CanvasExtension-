def main():
    x = True
    while x:
        symptom = input("whats wrong? type in a symptom you're feeling")
        zodiac_sign = input("what is your zodiac sign? ")

        if zodiac_sign == "capricorn":
            print("shhh dont let anyone know you're feeling", symptom, ". you're a capricorn")
            symptom = input("whats wrong? type in a symptom you're feeling")
            zodiac_sign = input("what is your zodiac sign? ")
        elif zodiac_sign == "sagittarius":
            print("you're a sagitarius, you don't have real feelings.")
            symptom = input("whats wrong? type in a symptom you're feeling")
            zodiac_sign = input("what is your zodiac sign? ")
        elif zodiac_sign == "scorpio":
            print("OH you're a scorpio, of course you're feeling", symptom, ".") 
            symptom = input("whats wrong? type in a symptom you're feeling")
            zodiac_sign = input("what is your zodiac sign? ")
        elif zodiac_sign == "aquarius":
            print("suppress suppress suppress luv.")
            symptom = input("whats wrong? type in a symptom you're feeling")
            zodiac_sign = input("what is your zodiac sign? ")
        elif zodiac_sign == "pisces":
            print("") 
        elif zodiac_sign == "aries":
            print("you ARE the problem") 
            symptom = input("whats wrong? type in a symptom you're feeling")
        elif zodiac_sign == "taurus":
            symptom = input("whats wrong? type in a symptom you're feeling")
        elif zodiac_sign == "gemini":
            symptom = input("whats wrong? type in a symptom you're feeling")
        elif zodiac_sign == "cancer":
            symptom = input("whats wrong? type in a symptom you're feeling")
        elif zodiac_sign == "virgo":
            symptom = input("whats wrong? type in a symptom you're feeling")
        elif zodiac_sign == "libra":
            print("It's just a bones day for you :(")  
        elif zodiac_sign == "leo":
            symptom = input("whats wrong? type in a symptom you're feeling")
        else:
            print("idk dude")
            symptom = input("whats wrong? type in a symptom you're feeling")
            zodiac_sign = input("What is your zodiac sign? ")
    


main()