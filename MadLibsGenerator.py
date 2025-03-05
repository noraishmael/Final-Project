import random

def madlib():
    # print welcome message
    print("\nWelcome to BadLibs, the sub-standard, bargain-basement alternative to a brand name we can't legally reuse.\n")
    
    while True:
        playgame = input("Would you like to play a game (y/n)? ")
        if playgame.lower() == 'y':
            # Set up the wrapper text for the mad lib
            listText1 = [ "The ", "An awful ", "A lonely "]
            listText2 = [" fell ", " lurked ", " pondered " ]
            listText3 = [" before ", " after ", " while "]
            listText4 = [" a friend.", " for a long, long time.", " slowly."]

            # Request user input of noun, adjective and verb
            noun = input("Enter a noun (the name of a person or object): ")
            adjective = input("Enter an adjective (a word describing how an action was carried out): ")
            verb = input("Enter a verb (action ending in -ing): ")

            # Randomly select which parts of the mad lib to use
            num1 = random.randint(0, len(listText1) -1)
            num2 = random.randint(0, len(listText2) -1)
            num3 = random.randint(0, len(listText3) -1)
            num4 = random.randint(0, len(listText4) -1)
            
            # Display madlib
            print(listText1[num1] + noun + listText2[num2] + adjective + listText3[num3] + verb + listText4[num4])
        elif playgame.lower() == 'n':
            print("OK, OK, I get it. The branded version is waaaaay better. Thanks for giving us a try.")
            break
        else:
                print("Please just enter y or n.")


madlib()