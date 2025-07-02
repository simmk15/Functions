def weather(season):
    if season=="autumn":
        print("The weather is pleasent!")
    elif season=="spring":
        print("It is a bloomy weather!")
    else:
        print(season,"is the weather")
season=input("Enter a weather=")
weather(season)