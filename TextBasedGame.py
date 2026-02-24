# Ricardo Villarreal
# IT 140 Project Two
# Dragon Ball Text Adventure Game


def show_instructions():
    print("======================================")
    print(" Dragon Ball Text Adventure Game")
    print(" Collect all 6 items before Majin Buu!")
    print("======================================")
    print("Move commands: go North, go South, go East, go West")
    print("To pick up an item: get 'item name'")
    print("--------------------------------------")


def show_status(current_room, inventory, rooms):
    print("\nYou are in:", current_room)
    print("Inventory:", inventory)

    if "item" in rooms[current_room]:
        print("You see:", rooms[current_room]["item"])

    print("--------------------------------------")


def main():

    rooms = {

        "Home": {
            "North": "North City",
            "South": "Kame House",
            "East": "Capsule Corp",
            "West": "Training Room"
        },

        "Training Room": {
            "East": "Home",
            "item": "Vegeta"
        },

        "North City": {
            "South": "Home",
            "East": "East City",
            "item": "Supreme Kai"
        },

        "East City": {
            "West": "North City",
            "item": "Majin Buu"  # Villain
        },

        "Capsule Corp": {
            "West": "Home",
            "North": "Food Market",
            "item": "Sealing Jar"
        },

        "Food Market": {
            "South": "Capsule Corp",
            "item": "Burger"
        },

        "Kame House": {
            "North": "Home",
            "East": "Kai's Lookout",
            "item": "Potara"
        },

        "Kai's Lookout": {
            "West": "Kame House",
            "item": "Senzu Beans"
        }
    }

    current_room = "Home"
    inventory = []
    required_items = 6

    show_instructions()

    while True:

        show_status(current_room, inventory, rooms)

        move = input("Enter your move: ")

        # Movement
        if move.lower().startswith("go "):
            direction = move[3:].title()

            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]

                # Check for villain
                if rooms[current_room].get("item") == "Majin Buu":
                    if len(inventory) == required_items:
                        print("\nYou used all the items and defeated Majin Buu!")
                        print("Congratulations! You win!")
                    else:
                        print("\nMajin Buu defeated you...")
                        print("GAME OVER")
                    break
            else:
                print("You can't go that way!")

        # Get Item
        elif move.lower().startswith("get "):
            item_name = move[4:]

            if "item" in rooms[current_room] and item_name == rooms[current_room]["item"]:
                inventory.append(item_name)
                del rooms[current_room]["item"]
                print(item_name, "added to inventory!")
            else:
                print("That item is not here.")

        else:
            print("Invalid command.")

# Run game
if __name__ == "__main__":
    main()