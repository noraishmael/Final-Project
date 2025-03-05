# Prompt the user for inputs
place = input("Enter a place: ")
adjective = input("Enter an adjective: ")
animal = input("Enter an animal: ")
emotion = input("Enter an emotion: ")
color = input("Enter a color: ")
creature = input("Enter a creature: ")
weather = input("Enter a type of weather: ")

# Create a template
template = ("Today I went to the " + place + ". I saw a " + adjective + " " + animal +
        "jumping up and down and running around. It was very" + emotion +
        ". Then a" + color + creature + "appeared. We all danced together in the " + weather + "."
)


# Print the completed story
print(template)