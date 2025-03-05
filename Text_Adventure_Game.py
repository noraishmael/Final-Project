# Define the game world

rooms = {

    "Entrance": {
        "description": "You are standing at the entrance. Where would you like to go next? You can go north and east.",
        "north": "Dining Room",
        "east": "Storage Room",
    },

    "Dining Room": {
        "description": "You are in the dining room. Where would you like to go next? You can go south and east.",
        "south": "Entrance",
        "east": "Kitchen",
    },

    "Storage Room": {
        "description": "You are in a small storage room. Where would you like to go next? You can go west.",
        "west": "Entrance",
    },

    "Kitchen": {
        "description": "You are in the kitchen. Where would you like to go next? You can go west.",
        "west": "Hallway",
    },
}


# Define where the player starts

current_room = "Entrance"

def display_room(room):
    
    # Print the description of the current room
    room_description = rooms[room]["description"]
    print("\n" + room_description)  

    # Show the player can move in different directions
    print("You can move:")

    # Print the possible directions explicitly
    if "north" in rooms[room]:
        print("  North")
    if "south" in rooms[room]:
        print("  South")
    if "east" in rooms[room]:
        print("  East")
    if "west" in rooms[room]:
        print("  West")



# Organise the game loop
while True:
    # Display the current room's details
    display_room(current_room)

    # Ask the player for input
    move = input("\nType 'move' if you would like to go to a different room or type 'quit' to stop playing: ").lower()

    # If the player wants to stop playing
    if move == "quit":
        print("Thanks for playing! Goodbye.")
        break
    elif move == "move":
        #Ask the player which direction he wants to move in?
        move = input("\nWhich direction would you like to move in?")

    # Check if the move is valid
    if move in rooms[current_room]:
        # Move the player
        current_room = rooms[current_room][move]
    else:
        # Tell the player the move is not valid
        print("\nYou can't move further in that direction. Please choose a different direction.")